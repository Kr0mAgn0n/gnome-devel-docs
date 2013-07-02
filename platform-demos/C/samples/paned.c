#include <gtk/gtk.h>

static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  GtkWidget *paned;
  GtkWidget *window;
  GtkWidget *image1;
  GtkWidget *image2;

  window = gtk_application_window_new (app);
  gtk_window_set_title (GTK_WINDOW (window), "Paned Example");
  gtk_window_set_default_size (GTK_WINDOW (window), 450, 350);

  paned = gtk_paned_new (GTK_ORIENTATION_HORIZONTAL);
  image1 = gtk_image_new_from_file ("gnome-image.png");
  image2 = gtk_image_new_from_file ("tux.png");

  gtk_paned_add1 (GTK_PANED (paned), image1);
  gtk_paned_add2 (GTK_PANED (paned), image2);

  gtk_container_add (GTK_CONTAINER (window), paned);

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
