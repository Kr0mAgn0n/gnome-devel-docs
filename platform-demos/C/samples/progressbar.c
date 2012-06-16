#include <gtk/gtk.h>

/*Global variable used to keep track of the progressbar's state*/
guint sourceID;


/*A function that pulses the progressbar once each time it is called*/
static gboolean
pulse (gpointer   user_data)
{
  GtkWidget *progress_bar = user_data;

  gtk_progress_bar_pulse (GTK_PROGRESS_BAR (progress_bar));
  
  return TRUE;
}



/*A function that causes the progressbar to start pulsing, or stop, according
to how many key-press-events have taken place*/
static gboolean
key_press_event (GtkWidget *widget,
                 GdkEvent *event,
                 gpointer user_data)
{
  GtkWidget *progress_bar = user_data;

  if (sourceID == 0) 
     sourceID = g_timeout_add (100, pulse, GTK_PROGRESS_BAR (progress_bar));
  else {
     g_source_remove (sourceID);
     sourceID = 0;
  }

  return TRUE;
}



static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  GtkWidget *window;
  GtkWidget *progress_bar;

  /*Create a window with a title, and a default size*/
  window = gtk_application_window_new (app);
  gtk_window_set_title (GTK_WINDOW (window), "ProgressBar Example");
  gtk_window_set_default_size (GTK_WINDOW (window), 220, 20);
 
  /*Create a progressbar and add it to the window*/
  progress_bar = gtk_progress_bar_new ();
  gtk_container_add (GTK_CONTAINER (window), progress_bar);

  /*Use the created pulse function every 100 milliseconds*/
  sourceID = g_timeout_add (100, pulse, GTK_PROGRESS_BAR (progress_bar));

  /*connecting the key-press signal to the callback*/
  g_signal_connect (GTK_WINDOW (window), 
                    "key-press-event", 
                    G_CALLBACK (key_press_event), 
                    progress_bar);
 
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
