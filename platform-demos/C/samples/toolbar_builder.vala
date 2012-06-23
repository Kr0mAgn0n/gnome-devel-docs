/* This is the Window */
class MyWindow : Gtk.ApplicationWindow {

	/* Declare these two ToolButtons, as we will get them
	 * from the ui file (see lines 32 and 33), so we can
	 * hide() and show() them as needed.*/
	Gtk.ToolButton fullscreen_button;
	Gtk.ToolButton leave_fullscreen_button;

	/* Contstructor */
	internal MyWindow (MyApplication app) {
		Object (application: app, title: "Toolbar Example");

		this.set_default_size (400, 200);
		var grid = new Gtk.Grid ();
		this.add (grid);
		grid.show ();

		/* add the toolbar from the ui file */
		var builder = new Gtk.Builder ();
		try {
			builder.add_from_file ("toolbar_builder.ui");
		}
		/* Handle the exception */
		catch (Error e) {
			error ("Unable to load file: %s", e.message);
		}

		grid.attach (builder.get_object ("toolbar") as Gtk.Toolbar, 0, 0, 1, 1);

		/* get these objects from the ui file so we can toggle between them */
		fullscreen_button = builder.get_object ("fullscreen_button") as Gtk.ToolButton;
		leave_fullscreen_button = builder.get_object ("leave_fullscreen_button") as Gtk.ToolButton;

		/* create the "undo" window action action */
		var undo_action = new SimpleAction ("undo", null);
		undo_action.activate.connect (undo_callback);
		this.add_action (undo_action);

		/* create the "fullscreen" window action */
		var fullscreen_action = new SimpleAction ("fullscreen", null);
		fullscreen_action.activate.connect (fullscreen_callback);
		this.add_action (fullscreen_action);
	}

	void undo_callback (SimpleAction simple, Variant? parameter) {
			print ("You clicked \"Undo\".\n");
	}

	void fullscreen_callback (SimpleAction simple, Variant? parameter) {
		if ((this.get_window ().get_state () & Gdk.WindowState.FULLSCREEN) != 0) {
			this.unfullscreen ();
			leave_fullscreen_button.hide ();
			fullscreen_button.show ();
		}
		else {
			this.fullscreen ();
			fullscreen_button.hide ();
			leave_fullscreen_button.show ();
		}
	}
}

/* This is the application */
class MyApplication : Gtk.Application {
	protected override void activate () {
		new MyWindow (this).show ();
	}

	protected override void startup () {
		base.startup ();

		/* Create the "new" action and add it to the app*/
		var new_action = new SimpleAction ("new", null);
		new_action.activate.connect (new_callback);
		this.add_action (new_action);

		/* Create the "open" action, and add it to the app */
		var open_action = new SimpleAction ("open", null);
		open_action.activate.connect (open_callback);
		this.add_action (open_action);

		/* You could also add the action to the app menu
		 * if you wanted to.
		 */
		//var menu = new Menu ();
		//menu.append ("New", "app.new");
		//this.app_menu = menu;
	}

	void new_callback (SimpleAction action, Variant? parameter) {
		print ("You clicked \"New\".\n");
	}

	void open_callback (SimpleAction action, Variant? parameter) {
			print ("You clicked \"Open\".\n");
	}
}

/* The main function creates the application and runs it. */
int main (string[] args) {
	return new MyApplication ().run (args);
}
