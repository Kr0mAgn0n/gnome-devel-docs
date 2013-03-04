#include <gtk/gtk.h>

static void
new_window (GSimpleAction *action,
            GVariant      *parameter,
            gpointer       user_data)
{
  g_print ("This does nothing. It is only a demonstration.\n");
}

static void
quit (GSimpleAction *action,
      GVariant      *parameter,
      gpointer       user_data)
{
  GApplication *application = user_data;

  g_application_quit (application);
}

static void
startup (GtkApplication *application,
         gpointer        user_data)
{
  static const GActionEntry actions[] = {
    { "new", new_window },
    { "quit", quit }
  };

  GMenu *menu;

  g_action_map_add_action_entries (G_ACTION_MAP (application), actions, G_N_ELEMENTS (actions), application);

  menu = g_menu_new ();
  g_menu_append (menu, "New", "app.new");
  g_menu_append (menu, "Quit", "app.quit");
  gtk_application_set_app_menu (application, G_MENU_MODEL (menu));
  g_object_unref (menu);
}

static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  GtkWidget *window;

  window = gtk_application_window_new (app);

  gtk_window_set_application (GTK_WINDOW (window), GTK_APPLICATION (app));
  gtk_window_set_title (GTK_WINDOW (window), "Hello GNOME");

  gtk_widget_show_all (GTK_WIDGET (window));
}

int
main (int argc, char **argv)
{
  GtkApplication *app;
  int status;

  app = gtk_application_new ("org.gtk.example",G_APPLICATION_FLAGS_NONE);
  g_signal_connect (app, "startup", G_CALLBACK (startup), NULL);
  g_signal_connect (app, "activate", G_CALLBACK (activate), NULL);
  status = g_application_run (G_APPLICATION (app), argc, argv);
  g_object_unref (app);
  return status;
}
