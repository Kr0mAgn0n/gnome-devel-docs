#include <gtk/gtk.h>



/*Signal handler for the "toggled" signal of the RadioButton*/
static void
button_toggled_cb (GtkWidget *button,
                   gpointer   user_data)
{
  char *b_state;
  const char *button_label;

  if (gtk_toggle_button_get_active (GTK_TOGGLE_BUTTON (button)))
          b_state = "on";
  else {
          b_state = "off";
          g_print ("\n");
  }

  button_label = gtk_button_get_label (GTK_BUTTON (button));

  g_print ("%s was turned %s\n", button_label, b_state);
}



static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  GtkWidget *grid;
  GtkWidget *window;

  GtkWidget *button1;
  GtkWidget *button2;
  GtkWidget *button3;

  /*Create a window with a set title and default size.
  Also, set a border width for the amount of space to leave
  inside the window*/
  window = gtk_application_window_new (app);
  gtk_window_set_title (GTK_WINDOW (window), "RadioButton Example");
  gtk_window_set_default_size (GTK_WINDOW (window), 250, 100);
  gtk_container_set_border_width (GTK_CONTAINER(window), 20);


  /*Create an initial radio button*/
  button1 = gtk_radio_button_new_with_label (NULL, "Button 1");

  /*Create a second radio button, and add it to the same group as Button 1*/
  button2 = gtk_radio_button_new_with_label_from_widget (GTK_RADIO_BUTTON (button1), 
                                                         "Button 2");

  /*Create a third button, and add it to the same group as Button 1*/
  button3 = gtk_radio_button_new_with_label_from_widget (GTK_RADIO_BUTTON (button1), 
                                                         "Button 3");


  /*Create a grid, attach the buttons, and position them accordingly*/
  grid = gtk_grid_new ();
  gtk_grid_attach (GTK_GRID (grid), button1, 0, 0, 1, 1);
  gtk_grid_attach (GTK_GRID (grid), button2, 0, 1, 1, 1);
  gtk_grid_attach (GTK_GRID (grid), button3, 0, 2, 1, 1);

  /*Be sure to set the initial state of each button*/
  gtk_toggle_button_set_active (GTK_TOGGLE_BUTTON (button2), TRUE);
  gtk_toggle_button_set_active (GTK_TOGGLE_BUTTON (button1), FALSE);
  gtk_toggle_button_set_active (GTK_TOGGLE_BUTTON (button3), FALSE);

  /*Connect the signal handlers (aka Callback functions) to the buttons*/
  g_signal_connect (GTK_TOGGLE_BUTTON (button1), "toggled", 
                    G_CALLBACK (button_toggled_cb), window);
  g_signal_connect (GTK_TOGGLE_BUTTON (button2), "toggled", 
                    G_CALLBACK (button_toggled_cb), window);
  g_signal_connect (GTK_TOGGLE_BUTTON (button3), "toggled", 
                    G_CALLBACK (button_toggled_cb), window);

  gtk_container_add (GTK_CONTAINER (window), GTK_WIDGET (grid));

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
