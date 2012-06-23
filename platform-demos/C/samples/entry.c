#include <gtk/gtk.h>

/*This is the callback function. It is a handler function
which reacts to the signal. In this case, it will grab the
text input from the entry box and print out a line to the user.*/
static void
on_activate (GtkEntry *entry,
             gpointer  user_data)
{
  const char *name;
  name = gtk_entry_get_text (entry);

  g_print ("\nHello %s!\n\n", name);
}

static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  GtkWidget *window;
  GtkWidget *entry_box;

  /*Create a window with a title, a default size,
  and a set border width*/
  window = gtk_application_window_new (app);
  gtk_window_set_title (GTK_WINDOW (window), "What is your name?");
  gtk_window_set_default_size (GTK_WINDOW (window), 300, 100);
  gtk_container_set_border_width(GTK_CONTAINER(window), 10);

  /*create a new entry box, and add it to the window*/
  entry_box = gtk_entry_new ();
  gtk_container_add (GTK_CONTAINER (window), entry_box);

  /*connecting the clicked signal to the callback*/
  g_signal_connect(GTK_ENTRY (entry_box), "activate", G_CALLBACK (on_activate), NULL);

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
