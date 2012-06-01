#include <gtk/gtk.h>


static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  GtkWidget *window;
  GtkWidget *linkbutton;

  window = gtk_application_window_new (app);

  gtk_window_set_title (GTK_WINDOW (window), "GNOME LinkButton");
  gtk_window_set_default_size (GTK_WINDOW (window), 250, 50);
  
  linkbutton = gtk_link_button_new ("Link to GNOME live!");
  gtk_link_button_set_uri (GTK_LINK_BUTTON(linkbutton), "http://live.gnome.org");

  gtk_container_add (GTK_CONTAINER (window), GTK_WIDGET (linkbutton));

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
