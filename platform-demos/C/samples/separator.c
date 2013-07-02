#include <gtk/gtk.h>

static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  GtkWidget *grid;
  GtkWidget *window;
  GtkWidget *label1;
  GtkWidget *label2;
  GtkWidget *label3;
  GtkWidget *hseparator;
  GtkWidget *vseparator;

  window = gtk_application_window_new (app);
  gtk_window_set_title (GTK_WINDOW (window), "Separator Example");

  label1 = gtk_label_new ("Below, a horizontal separator.");
  label2 = gtk_label_new ("On the right, a vertical separator.");
  label3 = gtk_label_new ("On the left, a vertical separator.");

  vseparator = gtk_separator_new (GTK_ORIENTATION_VERTICAL);
  hseparator = gtk_separator_new (GTK_ORIENTATION_HORIZONTAL);

  grid = gtk_grid_new ();

  gtk_grid_attach (GTK_GRID (grid), label1, 0, 0, 3, 1);
  gtk_grid_attach (GTK_GRID (grid), hseparator, 0, 1, 3, 1);
  gtk_grid_attach (GTK_GRID (grid), label2, 0, 2, 1, 1);
  gtk_grid_attach (GTK_GRID (grid), vseparator, 1, 2, 1, 1);
  gtk_grid_attach (GTK_GRID (grid), label3, 2, 2, 1, 1);

  gtk_grid_set_column_homogeneous (GTK_GRID (grid), TRUE);

  gtk_container_add (GTK_CONTAINER (window), grid);

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
