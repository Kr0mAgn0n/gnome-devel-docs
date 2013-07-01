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

  if (gtk_combo_box_get_active (combo_box) != 0) {
    gchar *distro = gtk_combo_box_text_get_active_text (GTK_COMBO_BOX_TEXT(combo_box));
    g_print ("You chose %s\n", distro);
    g_free (distro);
  }

}


static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  gint i;
  GtkWidget *view;
  GtkWidget *window;
  GtkWidget *combo_box;

  /* Create a window with a title, border width, and a default size. Setting the
   * size to -1 means to use the "natural" default size.
   * (the size request of the window)
   */
  window = gtk_application_window_new (app);
  gtk_window_set_title (GTK_WINDOW (window), "Welcome to GNOME");
  gtk_window_set_default_size (GTK_WINDOW (window), 200, -1);
  gtk_container_set_border_width (GTK_CONTAINER (window), 10);


  /* Create the combo box and append your string values to it. */
  combo_box = gtk_combo_box_text_new ();
  const char *distros[] = {"Select distribution", "Fedora", "Mint", "Suse"};

 
  /* G_N_ELEMENTS is a macro which determines the number of elements in an array.*/ 
  for (i = 0; i < G_N_ELEMENTS (distros); i++){
  	gtk_combo_box_text_append_text (GTK_COMBO_BOX_TEXT (combo_box), distros[i]);
  }

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
