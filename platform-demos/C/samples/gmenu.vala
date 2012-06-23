/* A window in the application. */
public class Window : Gtk.ApplicationWindow {

	/* Constructor */
	public Window (Application app) {
		Object (application: app, title: "Gmenu Example");

		var about_action = new SimpleAction ("about", null);

		/* Connect the 'activate' signal to the
		 * signal handler (aka. callback).
		 */
		about_action.activate.connect (this.about_cb);

		/* Add the action to this window. */
		this.add_action (about_action);

		this.show ();
	}

	/* Signal handler for 'activate' signal of the SimpleAction. */
	void about_cb (SimpleAction simple, Variant? parameter) {
		print ("This does nothing.  It is only a demonstration.\n");
	}
}

/* This is the Application. */
public class Application : Gtk.Application {

	/* Constructor */
	public Application () {
		Object (application_id: "org.example.application");
	}

	/* Override the 'activate' signal of GLib.Application. */
	protected override void activate () {

		/* Create a new window for this application. */
		new Window (this);
	}

	/* Override the 'startup' signal of GLib.Application. */
	protected override void startup () {
		base.startup ();

		var menu = new Menu ();
		menu.append ("About", "win.about");
		menu.append ("Quit", "app.quit");
		this.app_menu = menu;

		var quit_action = new SimpleAction ("quit", null);
		//quit_action.activate.connect (this.quit);
		this.add_action (quit_action);
	}
}

/* main function creates Application and runs it. */
int main (string[] args) {
	return new Application ().run (args);
}
