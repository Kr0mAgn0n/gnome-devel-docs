#include <gtk/gtk.h>

typedef struct _AppWidgets AppWidgets;

struct _AppWidgets
{
   GtkWidget *window;
   GtkWidget *image;
};

void on_open_button_clicked (GtkWidget *button, gpointer data);

int main( int   argc,
          char *argv[] )
{
    GtkWidget *scroll_window = NULL;
    GtkWidget *open_button = NULL;
    GtkWidget *hbox = NULL;
    GtkWidget *vbox;
    AppWidgets app_widgets;
 
    gtk_init (&argc, &argv);
    
    app_widgets.window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
    gtk_window_set_default_size (GTK_WINDOW (app_widgets.window), 400, 400);
    gtk_window_set_title (GTK_WINDOW (app_widgets.window), "Image Viewer Demo");
    g_signal_connect (app_widgets.window, "destroy", G_CALLBACK (gtk_main_quit), NULL);

    /* Sets the image.*/
    app_widgets.image = gtk_image_new_from_file ("gtk_test.png");

    /* Make window scrollable. */
    scroll_window = gtk_scrolled_window_new (NULL, NULL); 
    gtk_scrolled_window_add_with_viewport (GTK_SCROLLED_WINDOW (scroll_window), app_widgets.image);

    /* Button's box. */
    hbox = gtk_box_new (GTK_HORIENTATION_HORIZONTAL, 5);

    open_button = gtk_button_new_with_label( "Open...");
    gtk_box_pack_start (GTK_BOX (hbox), open_button, TRUE, TRUE, 0);
    g_signal_connect (open_button, "clicked",
                      G_CALLBACK (on_open_button_clicked), &app_widgets);

    /* Main window layout. */
    vbox = gtk_box_new (GTK_HORIENTATION_VERTICAL, 0);

    gtk_box_pack_start (GTK_BOX (vbox), scroll_window, TRUE, TRUE, 0);
    gtk_box_pack_start (GTK_BOX (vbox), hbox, FALSE, FALSE, 0);

    gtk_container_add (GTK_CONTAINER (app_widgets.window), vbox);

    gtk_widget_show_all  (app_widgets.window);
    
    gtk_main ();
    
    return 0;
}
void on_open_button_clicked (GtkWidget *button, gpointer data)
{
   GtkWidget *file_chooser_dialog = NULL;
   GtkFileFilter *filter = NULL;
   GFile *file = NULL;
   char *filename;
   AppWidgets *app_widgets = (AppWidgets *) data;

   file_chooser_dialog = gtk_file_chooser_dialog_new ("Open file",
                                         GTK_WINDOW (app_widgets->window),
                                         GTK_FILE_CHOOSER_ACTION_OPEN,
                                         GTK_STOCK_CANCEL, GTK_RESPONSE_CANCEL,
                                         GTK_STOCK_OPEN, GTK_RESPONSE_ACCEPT,
                                         NULL);

   /* Show just image files. */
   filter = gtk_file_filter_new ();
   gtk_file_filter_add_pixbuf_formats (filter);
   gtk_file_chooser_add_filter (GTK_FILE_CHOOSER (file_chooser_dialog), filter); 

   if (gtk_dialog_run (GTK_DIALOG (file_chooser_dialog)) == GTK_RESPONSE_ACCEPT)
   {
      file = gtk_file_chooser_get_file (GTK_FILE_CHOOSER (file_chooser_dialog));
      filename = g_file_get_basename (file);
      gtk_image_set_from_file (GTK_IMAGE (app_widgets->image), filename);
      
      g_free (filename);
   }
   gtk_widget_destroy (file_chooser_dialog);
}
