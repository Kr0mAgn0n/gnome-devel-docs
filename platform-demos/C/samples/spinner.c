#include <gtk/gtk.h>

 /*Global variable used to indicate active state of the
spinner. TRUE = active, FALSE = not-active. This is because
there isn't a current function for C that does this for us*/
gboolean active;


/*This is the callback function. It is a handler function
which reacts to the signal. In this case, it will cause the
spinner to start and stop according to how many times the user
presses the spacebar.*/
static gboolean
key_pressed_event (GtkWidget *widget,
                   GdkEvent  *event,
                   gpointer   user_data)
{
  GtkWidget *spinner = user_data;
  guint keyval;

  /*Extracts the keyval from an event. And stores it in the  variable
  "keyval" (we give the function the address). In this case, the
  event is GdkEventKey, a key press event*/
  gdk_event_get_keyval (event, &keyval);

  /*Grabbing the boolean value from the spinner*/
  g_object_get (GTK_SPINNER (spinner), "active", &active, NULL);

  if (keyval == GDK_KEY_space) {
     if (active) {
         gtk_spinner_stop (GTK_SPINNER (spinner));
     }
     else {
         gtk_spinner_start (GTK_SPINNER (spinner));
     }
  }

return TRUE;
}


static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  GtkWidget *window;
  GtkWidget *spinner;

  /*Create a window with a title, border width and a default size*/
  window = gtk_application_window_new (app);

  gtk_window_set_title (GTK_WINDOW (window), "Spinner Example");
  gtk_window_set_default_size (GTK_WINDOW (window), 200, 200);
  gtk_container_set_border_width(GTK_CONTAINER(window), 30);

  /*Create a spinner, with extra horizontal and vertical space*/
  spinner = gtk_spinner_new ();
  gtk_spinner_start (GTK_SPINNER (spinner));
  //gtk_widget_set_hexpand (spinner, TRUE);
  //gtk_widget_set_vexpand (spinner, TRUE);

  gtk_container_add (GTK_CONTAINER (window), spinner);

  /*connecting the clicked signal to the callback*/
  g_signal_connect (GTK_WINDOW (window), "key-press-event", G_CALLBACK (key_pressed_event), spinner);

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
