#include <gtk/gtk.h>



/* This is the callback function. 
 * It is a handler function which reacts to the signal. 
 * In this case, it will notify the user the value of their spinbutton 
 * as a label.
 */
static void
spin_clicked (GtkSpinButton *spinbutton,
              gpointer       user_data)
{
   GtkWidget *label = user_data;
   gint value = gtk_spin_button_get_value_as_int (spinbutton);

   /* %d - Is used when printing integers.
    * Note: Using g_strdup_printf returns a string that must be freed. 
    * (In which is done below)
    */
   gchar *str = g_strdup_printf ("The number you selected is %d.", value);
   gtk_label_set_text (GTK_LABEL (label), str);

   g_free(str);
}



static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  /* Declare variables */
  GtkWidget *window;
  GtkWidget *label;
  GtkWidget *grid;
  GtkWidget *spin_button;
  GtkAdjustment *adjustment;


  /* Create a window with a title, a border width, and a default size */
  window = gtk_application_window_new (app);
  gtk_window_set_title (GTK_WINDOW (window), "SpinButton Example");
  gtk_window_set_default_size (GTK_WINDOW (window), 210, 70);
  gtk_container_set_border_width (GTK_CONTAINER (window), 5);

  /* Create a label to be shown in the window */
  label = gtk_label_new ("Choose a number");

  /* Create an adjustment representing an adjustable bounded value */
  adjustment = gtk_adjustment_new (0, 0, 100, 1, 0, 0);


  /* Create a spin button that is to be as wide as possible */
  spin_button = gtk_spin_button_new (adjustment, 1, 0);
  gtk_widget_set_hexpand (spin_button, TRUE);
  
  /* Connecting the "value-changed" signal for the spinbutton 
   * to the appropriate callback function. 
   */
  g_signal_connect (spin_button, 
                    "value-changed", 
                    G_CALLBACK (spin_clicked), 
                    label);


  /* Create a grid and arrange everything accordingly */
  grid = gtk_grid_new ();
  gtk_grid_set_column_spacing (GTK_GRID (grid), 10);
  gtk_grid_set_column_homogeneous (GTK_GRID (grid), TRUE);
  gtk_grid_attach (GTK_GRID (grid), spin_button, 0, 0, 1, 1);
  gtk_grid_attach (GTK_GRID (grid), label, 0, 1, 1, 1);
  

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
