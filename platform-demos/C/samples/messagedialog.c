#include <gtk/gtk.h>



/* Callback function in which reacts to the "response" signal from the user in
 * the message dialog window.
 * This function is used to interact with the user in the terminal.
 */
static void
on_response (GtkDialog *dialog,
             gint       response_id,
             gpointer   user_data)
{
  /* If the button clicked gives response OK (response_id being -5) */
  if (response_id == GTK_RESPONSE_OK) 
     g_print ("*boom*\n");

  /* If the button clicked gives response CANCEL (response_id being -6) */
  else if (response_id == GTK_RESPONSE_CANCEL)
     g_print ("good choice\n");

  /* If the message dialog is destroyed (for example by pressing escape) */
  else if (response_id == GTK_RESPONSE_DELETE_EVENT)
     g_print ("dialog closed or cancelled\n");

  /* Destroy the dialog after one of the above actions have taken place */
  gtk_widget_destroy (GTK_WIDGET (dialog));

}



/* Callback function for the response signal "activate" related to the SimpleAction
 * message_action.
 * This function is used to cause the message dialog window to popup.
 */
static void
message_cb (GSimpleAction *simple,
            GVariant      *parameter,
            gpointer       user_data)
{
   /* the parent variable in this case represents the window */
   GtkWidget *message_dialog;
   GtkWindow *parent = user_data;
   
   /* Create a new message dialog, and set the parameters as follows:
    * Dialog Flags - make the constructed dialog modal 
    * (modal windows prevent interaction with other windows in the application)
    * Message Type - nonfatal warning message
    * Buttons Type - use the ok and cancel buttons
    * message_format - text that you want the user to see in the window 
    */
   message_dialog = gtk_message_dialog_new (parent, GTK_DIALOG_MODAL, 
                                            GTK_MESSAGE_WARNING, 
                                            GTK_BUTTONS_OK_CANCEL, 
                                            "This action will cause the universe to stop existing.");

   gtk_widget_show_all (message_dialog);

   g_signal_connect (GTK_DIALOG (message_dialog), "response", 
                    G_CALLBACK (on_response), NULL);

}



static void
activate (GtkApplication *app,
          gpointer        user_data)
{
  GtkWidget *window;
  GtkWidget *label;

  GSimpleAction *message_action;

  /* Create a window with a title and a default size */
  window = gtk_application_window_new (app);
  gtk_window_set_title (GTK_WINDOW (window), "GMenu Example");
  gtk_window_set_default_size (GTK_WINDOW (window), 400, 200);

  /* Create a label and add it to the window */
  label = gtk_label_new ("This application goes boom!");
  gtk_container_add (GTK_CONTAINER (window), label);

  /* Create a new simple action, giving it a NULL parameter type. It will 
   * always be NULL for actions invoked from a menu. (e.g clicking on an "ok" 
   * or "cancel" button)
   */
  message_action = g_simple_action_new ("message", NULL); 

  /* Connect the "activate" signal to the appropriate callback function */
  g_signal_connect (message_action, "activate", G_CALLBACK (message_cb), 
                    GTK_WINDOW (window));

  /* Adds the message_action to the overall action map. An Action map is an 
   * interface that contains a number of named GAction instances 
   * (such as message_action) 
   */
  g_action_map_add_action (G_ACTION_MAP (window), G_ACTION (message_action));

  gtk_widget_show_all (window);
}



/* Callback function for the response signal "activate" from the "quit" action 
 * in the function directly below.
 */ 
static void
quit_cb (GSimpleAction *simple,
         GVariant      *parameter,
         gpointer       user_data)
{
  GApplication *application = user_data;

  g_application_quit (application);
}



/* Startup function for the menu we are creating in this sample */
static void
startup (GApplication *app,
         gpointer      user_data)
{
  GMenu *menu;
  GSimpleAction *quit_action;

  /* Initialize the GMenu, and add a menu item with label "Message" and action 
   * "win.message". Also add another menu item with label "Quit" and action 
   * "app.quit" 
   */
  menu = g_menu_new ();
  g_menu_append (menu, "Message", "win.message");
  g_menu_append (menu, "Quit", "app.quit");

  /* Create a new simple action for the application. (In this case it is the 
   * "quit" action.
   */
  quit_action = g_simple_action_new ("quit", NULL);

  /* Ensure that the menu we have just created is set for the overall application */
  gtk_application_set_app_menu (GTK_APPLICATION (app), G_MENU_MODEL (menu));

  g_signal_connect (quit_action, 
                    "activate", 
                    G_CALLBACK (quit_cb), 
                    app);

  g_action_map_add_action (G_ACTION_MAP (app), G_ACTION (quit_action));

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
