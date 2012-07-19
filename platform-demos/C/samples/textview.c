#include <gtk/gtk.h>



static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  /* Declare variables */
  GtkWidget *window;
  GtkWidget *text_view;
  GtkWidget *scrolled_window;

  GtkTextBuffer *buffer;


  /* Create a window with a title, and a default size */
  window = gtk_application_window_new (app);
  gtk_window_set_title (GTK_WINDOW (window), "TextView Example");
  gtk_window_set_default_size (GTK_WINDOW (window), 220, 200);


  /* The text buffer represents the text being edited */
  buffer = gtk_text_buffer_new (NULL);
  

  /* Text view is a widget in which can display the text buffer. 
   * The line wrapping is set to break lines in between words.
   */
  text_view = gtk_text_view_new_with_buffer (buffer);
  gtk_text_view_set_wrap_mode (GTK_TEXT_VIEW (text_view), GTK_WRAP_WORD); 


  /* Create the scrolled window. Usually NULL is passed for both parameters so 
   * that it creates the horizontal/vertical adjustments automatically. Setting 
   * the scrollbar policy to automatic allows the scrollbars to only show up 
   * when needed. 
   */
  scrolled_window = gtk_scrolled_window_new (NULL, NULL);
  gtk_scrolled_window_set_policy (GTK_SCROLLED_WINDOW (scrolled_window), 
                                  GTK_POLICY_AUTOMATIC, 
                                  GTK_POLICY_AUTOMATIC); 
  /* The function directly below is used to add children to the scrolled window 
   * with scrolling capabilities (e.g text_view), otherwise, 
   * gtk_scrolled_window_add_with_viewport() would have been used
   */
  gtk_container_add (GTK_CONTAINER (scrolled_window), 
                                         text_view);
  gtk_container_set_border_width (GTK_CONTAINER (scrolled_window), 5);
 
  
  gtk_container_add (GTK_CONTAINER (window), scrolled_window);

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
