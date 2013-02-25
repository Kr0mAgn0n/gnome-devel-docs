#include <gtk/gtk.h>



/*This is the callback function. It is a handler function which 
reacts to the signal. In this case, it will cause the button label's 
string to reverse.*/
static void
button_clicked (GtkButton *button,
                gpointer   user_data)
{
  const char *old_label;
  char *new_label;

  old_label = gtk_button_get_label (button);
  new_label = g_utf8_strreverse (old_label, -1);

  gtk_button_set_label (button, new_label);
  g_free (new_label);
}



static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  GtkWidget *window;
  GtkWidget *button;

  /*Create a window with a title and a default size*/
  window = gtk_application_window_new (app);
  gtk_window_set_title (GTK_WINDOW (window), "GNOME Button");
  gtk_window_set_default_size (GTK_WINDOW (window), 250, 50);

  /*Create a button with a label, and add it to the window*/
  button = gtk_button_new_with_label ("Click Me");
  gtk_container_add (GTK_CONTAINER (window), button);

  /*Connecting the clicked signal to the callback function*/
  g_signal_connect (GTK_BUTTON (button),
                    "clicked", 
                    G_CALLBACK (button_clicked), 
                    G_OBJECT (window));

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
