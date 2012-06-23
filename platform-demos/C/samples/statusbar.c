#include <gtk/gtk.h>



/*Callback function in which pushes an item onto the statusbar*/
static void 
push_item(GtkWidget *widget,
          gpointer   data)
{
  GtkWidget *status_bar = data;
  guint context_id = gtk_statusbar_get_context_id (GTK_STATUSBAR (status_bar), 
                                                   "Statusbar example");

  /*Count is used to keep track of the amount of items 
  the user is pushing/popping*/
  static int count = 1;
  char hold_output[20];
  
  /*This is a safer form of the standard sprintf() function. The output is 
  gauranteed in this case to not exceed 20 characters, and the result is stored 
  into the 'hold_output' variable*/
  g_snprintf(hold_output, 20, "Item %d", count++);
  gtk_statusbar_push(GTK_STATUSBAR (status_bar), 
                     context_id, 
                     hold_output);
}



/*Callback function that is used to pop an item off the statusbar*/
static void 
pop_item(GtkWidget *widget,
         gpointer   data )
{
  GtkWidget *status_bar = data;
  guint context_id = gtk_statusbar_get_context_id (GTK_STATUSBAR (status_bar), 
                                                   "Statusbar example");

  gtk_statusbar_pop(GTK_STATUSBAR (status_bar), context_id);
}



static void
activate (GtkApplication *app,
          gpointer        user_data)
{
    GtkWidget *window;
    GtkWidget *grid;
    GtkWidget *push_button;
    GtkWidget *pop_button;
    GtkWidget *status_bar;

    guint context_id;

    /*Create a window with a title, border width, and a default size**/
    window = gtk_application_window_new (app);
    gtk_window_set_default_size (GTK_WINDOW (window), 220, 100);
    gtk_window_set_title (GTK_WINDOW (window), "Statusbar Example");
    gtk_container_set_border_width (GTK_CONTAINER(window), 10);
    
    /*Create the status bar, which is held in the global variable*/
    status_bar = gtk_statusbar_new ();      
    
    /*Create a context id, which is used to uniquely identify 
    the source of a message*/
    context_id = gtk_statusbar_get_context_id (GTK_STATUSBAR (status_bar), 
                                               "Statusbar example");

    /*Create the buttons with labels*/
    push_button = gtk_button_new_with_label ("push item");
    pop_button = gtk_button_new_with_label ("pop last item");
    
    /*Create the grid, and attach the buttons/statusbar accordingly*/
    grid = gtk_grid_new ();
    gtk_grid_attach (GTK_GRID (grid), push_button, 0,1,1,1);
    gtk_grid_attach (GTK_GRID (grid), pop_button, 0,2,1,1);
    gtk_grid_attach (GTK_GRID (grid), status_bar, 0,3,1,1);
    
    /*Connecting the clicked signals to the corresponding callback functions*/
    g_signal_connect (GTK_BUTTON (push_button), "clicked", 
                      G_CALLBACK (push_item), status_bar);
    g_signal_connect (GTK_BUTTON (pop_button), "clicked", 
                      G_CALLBACK (pop_item), status_bar);
    
    /*Attach the grid holding the child widgets onto the window, and show all*/
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
