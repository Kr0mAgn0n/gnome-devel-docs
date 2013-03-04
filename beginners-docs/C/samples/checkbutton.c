#include <gtk/gtk.h>

/* signal handler for "toggled" signal of the CheckButton */
static void
toggled_cb (GtkToggleButton *toggle_button,
            gpointer         user_data)
{
  GtkWindow *window = user_data;

  if (gtk_toggle_button_get_active (toggle_button))
      gtk_window_set_title (window, "CheckButton Example");
  else
      gtk_window_set_title (window, "");
}

static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  GtkWidget *window;
  GtkWidget *checkbutton;

  window = gtk_application_window_new (app);
  gtk_window_set_title (GTK_WINDOW (window), "CheckButton Example");
  gtk_window_set_default_size (GTK_WINDOW (window), 300, 100);

  checkbutton = gtk_check_button_new_with_label ("Show Title");
  gtk_toggle_button_set_active (GTK_TOGGLE_BUTTON (checkbutton), TRUE);
  g_signal_connect (GTK_TOGGLE_BUTTON (checkbutton), "toggled", G_CALLBACK (toggled_cb), window);
  gtk_container_add (GTK_CONTAINER (window), checkbutton);
  gtk_widget_show_all (window);
}

int
main (int argc, char **argv)
{
  GtkApplication *app;
  int status;

  app = gtk_application_new ("org.example.checkbutton", G_APPLICATION_FLAGS_NONE);
  g_signal_connect (app, "activate", G_CALLBACK (activate), NULL);
  status = g_application_run (G_APPLICATION (app), argc, argv);
  g_object_unref (app);

  return status;
}
