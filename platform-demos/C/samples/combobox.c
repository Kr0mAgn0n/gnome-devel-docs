#include <gtk/gtk.h>



/* This is the callback function. It is a handler function which reacts to the
 * signal. In this case, if the row selected is not the first one of the
 * ComboBox, we write its value in the terminal for the user.
 */
static void
on_changed (GtkComboBox *widget,
            gpointer   user_data)
{
  GtkComboBox *combo_box = widget;

  /* This will return the index of the currently active
   * item within the ComboBox.
   */
  gint value = gtk_combo_box_get_active (combo_box);

  /* Equate the index to the list of the choices you put up and
   * print what happened to the user.
   */
  switch (value) {
     case 1:
       g_print ("You chose Fedora.\n");
       break;
     case 2:
       g_print ("You chose Mint.\n");
       break;
     case 3:
       g_print ("You chose Suse.\n");
       break;
     default:
       /* Nothing else will happen in the terminal otherwise */
       break;
   }
}



static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  GtkWidget *window;
  GtkWidget *combo_box;
  GtkWidget *view;

  /* Create a window with a title, border width, and a default size. Setting the
   * size to -1 means to use the "natural" default size.
   * (the size request of the window)
   */
  window = gtk_application_window_new (app);
  gtk_window_set_title (GTK_WINDOW (window), "Welcome to GNOME");
  gtk_window_set_default_size (GTK_WINDOW (window), 200, -1);
  gtk_container_set_border_width (GTK_CONTAINER (window), 10);

  /* Create the combo box and append your string values to it. Note that the
   * values in our combo box are to be this:
   * @ Position 0 - "Select distribution"
   * @ Position 1 - "Fedora"
   * @ Position 2 - "Mint"
   * @ Position 3 - "Suse"
   * (For a more advanced approach, try putting these into a string array)
   * Furthermore, we give the gtk_combo_box_text_append function a NULL id for
   * the parameter as it is not needed.
   */
  combo_box = gtk_combo_box_text_new ();
  gtk_combo_box_text_append (GTK_COMBO_BOX_TEXT (combo_box), NULL, "Select distribution");
  gtk_combo_box_text_append (GTK_COMBO_BOX_TEXT (combo_box), NULL, "Fedora");
  gtk_combo_box_text_append (GTK_COMBO_BOX_TEXT (combo_box), NULL, "Mint");
  gtk_combo_box_text_append (GTK_COMBO_BOX_TEXT (combo_box), NULL, "Suse");

  /* Choose to set the first row as the active one by default, from the beginning */
  gtk_combo_box_set_active (GTK_COMBO_BOX (combo_box), 0);

  /* Connect the signal emitted when a row is selected to the appropriate
   * callback function.
   */
  g_signal_connect (combo_box,
                    "changed",
                    G_CALLBACK (on_changed),
                    NULL);

  /* Add it to the window */
  gtk_container_add (GTK_CONTAINER (window), combo_box);

  gtk_widget_show_all (window);
}



int
main (int argc, char **argv)
{
  GtkApplication *app;
  int status;

  app = gtk_application_new ("org.gtk.example", G_APPLICATION_FLAGS_NONE);
  g_signal_connect (app, "activate", G_CALLBACK (activate), NULL);
  status = g_application_run (G_APPLICATION (app), argc, argv);
  g_object_unref (app);

  return status;
}
