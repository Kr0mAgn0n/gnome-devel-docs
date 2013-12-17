#include <gtk/gtk.h>



/* Callback function for the "copy" action */
static void
copy_callback (GSimpleAction *simple,
            GVariant      *parameter,
            gpointer       user_data)
{
   g_print ("\"Copy\" activated\n");
}



/* Callback function for the "paste" action */
static void
paste_callback (GSimpleAction *simple,
            GVariant      *parameter,
            gpointer       user_data)
{
   g_print ("\"Paste\" activated\n");
}



/* Callback function for the "shape" action */
static void
shape_callback (GSimpleAction *simple,
            GVariant      *parameter,
            gpointer       user_data)
{
   /* We first gather the value of the GVariant instance with a string type.
    * The overall goal here is to see if shape is set to line, triangle, etc,
    * and put that value within the variable "answer".
    */
   const gchar *answer = g_variant_get_string (parameter, NULL);
   g_printf ("Shape is set to %s.\n", answer);
   /* Note that we set the state of the action */
   g_simple_action_set_state (simple, parameter);
}



/* Callback function in which closes the about_dialog created below */
static void
on_close (GtkDialog *dialog,
          gint       response_id,
          gpointer   user_data)
{
  gtk_widget_destroy (GTK_WIDGET (dialog));
}



/* Callback function for the about action (see aboutdialog.c example) */
static void
about_callback (GSimpleAction *simple,
            GVariant      *parameter,
            gpointer       user_data)
{
   GtkWidget *about_dialog;

   about_dialog = gtk_about_dialog_new ();

   const gchar *authors[] = {"GNOME Documentation Team", NULL};
   const gchar *documenters[] = {"GNOME Documentation Team", NULL};

   /* Fill in the about_dialog with the desired information */
   gtk_about_dialog_set_program_name (GTK_ABOUT_DIALOG (about_dialog), "AboutDialog Example");
   gtk_about_dialog_set_copyright (GTK_ABOUT_DIALOG (about_dialog), "Copyright \xc2\xa9 2012 GNOME Documentation Team");
   gtk_about_dialog_set_authors (GTK_ABOUT_DIALOG (about_dialog), authors);
   gtk_about_dialog_set_documenters (GTK_ABOUT_DIALOG (about_dialog), documenters);
   gtk_about_dialog_set_website_label (GTK_ABOUT_DIALOG (about_dialog), "GNOME Developer Website");
   gtk_about_dialog_set_website (GTK_ABOUT_DIALOG (about_dialog), "http://developer.gnome.org");

   /* The "response" signal is emitted when the dialog receives a delete event,
    * therefore we connect that signal to the on_close callback function
    * created above.
    */
   g_signal_connect (GTK_DIALOG (about_dialog), "response",
                    G_CALLBACK (on_close), NULL);

   /* Show the about dialog */
   gtk_widget_show (about_dialog);
}



static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  GtkWidget *window;

  GSimpleAction *copy_action;
  GSimpleAction *paste_action;
  GSimpleAction *shape_action;
  GSimpleAction *about_action;

  /* Create a window with a title and a default size */
  window = gtk_application_window_new (app);
  gtk_window_set_title (GTK_WINDOW (window), "MenuBar Example");
  gtk_window_set_default_size (GTK_WINDOW (window), 200, 200);

  /* Begin creating the "copy" action.
   * Note that it is an action without a state.
   */
  copy_action = g_simple_action_new ("copy", NULL);
  /* Connected to a callback function */
  g_signal_connect (copy_action, "activate", G_CALLBACK (copy_callback),
                    GTK_WINDOW (window));
  /* Added to the window */
  g_action_map_add_action (G_ACTION_MAP (window), G_ACTION (copy_action));

  /* Begin creating the "paste" action.
   * Note that it is an action without a state.
   */
  paste_action = g_simple_action_new ("paste", NULL);
  /* Connect the action to a callback function */
  g_signal_connect (paste_action, "activate", G_CALLBACK (paste_callback),
                    GTK_WINDOW (window));
  /* Add it to the window */
  g_action_map_add_action (G_ACTION_MAP (window), G_ACTION (paste_action));

  /* Begin creating the "shape" action.
   * Note that it is an action with a state.
   * First we state that the parameter type of the simple action is a string.
   * When using g_variant_type_new, it is appropriate to free the return value
   * once you're done with it.
   */
  GVariantType *type_string = g_variant_type_new ("s");
  /* parameters for the g_simple_action_new_stateful are: (name, parameter type,
   * initial state).
   */
  shape_action = g_simple_action_new_stateful ("shape", type_string,
                                               g_variant_new_string ("line"));
  /* Connect the action to a callback function */
  g_signal_connect (shape_action, "activate", G_CALLBACK (shape_callback),
                    GTK_WINDOW (window));
  /* Add it to the window */
  g_action_map_add_action (G_ACTION_MAP (window), G_ACTION (shape_action));
  g_variant_type_free (type_string);

  /* Begin creating the "about" action.
   * Note that it is an action without a state.
   */
  about_action = g_simple_action_new ("about", NULL);
  /* Connect the action to a callback function */
  g_signal_connect (about_action, "activate", G_CALLBACK (about_callback),
                    GTK_WINDOW (window));
  /* Add it to the window */
  g_action_map_add_action (G_ACTION_MAP (window), G_ACTION (about_action));

  gtk_widget_show_all (window);
}



/* Callback function for the "new" action */
static void
new_callback (GSimpleAction *simple,
         GVariant      *parameter,
         gpointer       user_data)
{
  g_print ("You clicked \"New\"\n");
}



/* Callback function for the "quit" action */
static void
quit_callback (GSimpleAction *simple,
         GVariant      *parameter,
         gpointer       user_data)
{
  GApplication *application = user_data;

  g_print ("You clicked \"Quit\"\n");
  g_application_quit (application);
}



/* Callback function for the "state" action */
static void
state_callback (GSimpleAction *simple,
         GVariant      *parameter,
         gpointer       user_data)
{
   /* The two possibilies in this case for the "answer" variable are either
    * "on" or "off".
    */
   const gchar *answer = g_variant_get_string (parameter, NULL);
   /* We print the information to the user */
   g_printf ("State is set to %s.\n", answer);
   /* Note that we set the state of the action */
   g_simple_action_set_state (simple, parameter);
}



/* Callback function for the "awesome" action */
static void
awesome_callback (GSimpleAction *simple,
         GVariant      *parameter,
         gpointer       user_data)
{
  GVariant *action_state = g_action_get_state (G_ACTION (simple));
  gboolean active = g_variant_get_boolean (action_state);
  GVariant *new_state = g_variant_new_boolean (!active);
  /* Set the new state for the action.
   * (Keeps track of whether it was last checked or unchecked).
   */
  g_simple_action_set_state (simple, new_state);

  if (active)
     g_print ("You unchecked \"Awesome\"\n");
  else
     g_print ("You checked \"Awesome\"\n");
}



/* Startup function for the menu we are creating in this sample */
static void
startup (GApplication *app,
         gpointer      user_data)
{
  /* Initialize variables */
  GSimpleAction *new_action;
  GSimpleAction *quit_action;
  GSimpleAction *state_action;
  GSimpleAction *awesome_action;

  GtkBuilder *builder;

  GError *error = NULL;

  /* Begin creating the "new" action.
   * Note that it is an action without a state.
   */
  new_action = g_simple_action_new ("new", NULL);
  g_signal_connect (new_action, "activate", G_CALLBACK (new_callback), app);
  /* It is added to the overall application */
  g_action_map_add_action (G_ACTION_MAP (app), G_ACTION (new_action));

  /* Begin creating the "quit" action.
   * Note that it is an action without a state.
   */
  quit_action = g_simple_action_new ("quit", NULL);
  g_signal_connect (quit_action, "activate", G_CALLBACK (quit_callback), app);
  /* It is added to the overall application */
  g_action_map_add_action (G_ACTION_MAP (app), G_ACTION (quit_action));

  /* Begin creating the "state" action.
   * Note that it is an action with a state.
   */
  GVariantType *type_string2 = g_variant_type_new ("s");
  state_action = g_simple_action_new_stateful ("state", type_string2,
                                               g_variant_new_string ("off"));
  g_signal_connect (state_action, "activate", G_CALLBACK (state_callback), app);
  /* It is added to the overall application */
  g_action_map_add_action (G_ACTION_MAP (app), G_ACTION (state_action));
  g_variant_type_free (type_string2);

  /* Begin creating the "awesome" action.
   * Note that it is an action with a state.
   */
  awesome_action = g_simple_action_new_stateful ("awesome", NULL, g_variant_new_boolean (FALSE));
  g_signal_connect (awesome_action, "activate", G_CALLBACK (awesome_callback), app);
  /* It is added to the overall application */
  g_action_map_add_action (G_ACTION_MAP (app), G_ACTION (awesome_action));

  /* A builder to add the User Interface designed with GLADE to the grid: */
  builder = gtk_builder_new ();
  /* Get the file (if it is there):
   * Note: you must make sure that the file is in the current directory for
   * this to work. The function used here returns a non-null value within
   * our variable "error" if an error is indeed found.
   */
  gtk_builder_add_from_file (builder, "menubar.ui", &error);
  if (error != NULL) {
     g_print ("%s\n", error->message);
     g_error_free (error);
  }

  /* Extract the menubar */
  GObject *menubar = gtk_builder_get_object (builder, "menubar");
  gtk_application_set_menubar (GTK_APPLICATION (app), G_MENU_MODEL (menubar));

  /* Extract the appmenu */
  GObject *appmenu = gtk_builder_get_object (builder, "appmenu");
  gtk_application_set_app_menu (GTK_APPLICATION (app), G_MENU_MODEL (appmenu));
}



/* Startup function for the application */
int
main (int argc, char **argv)
{
  GtkApplication *app;
  int status;

  app = gtk_application_new ("org.gtk.example", G_APPLICATION_FLAGS_NONE);
  g_signal_connect (app, "activate", G_CALLBACK (activate), NULL);
  g_signal_connect (app, "startup", G_CALLBACK (startup), NULL);
  status = g_application_run (G_APPLICATION (app), argc, argv);
  g_object_unref (app);

  return status;
}
