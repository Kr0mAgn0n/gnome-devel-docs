/* A window in the Application. */
public class MyWindow : Gtk.ApplicationWindow {

	/* Constructor */
	internal MyWindow (MyApplication app) {
		Object (application: app, title: "Welcome to GNOME");
	}
}

/* This is the application. */
public class MyApplication : Gtk.Application {

	/* Constructor. */
	internal MyApplication () {
		Object (application_id: "org.example.MyApplication");
	}

	/* Override the 'activate' signal of GLib.Application. */
	protected override void activate () {

		/* Create the window of this application and show it. */
		new MyWindow (this).show ();
	}
}

/* main creates and runs the application. */
public int main (string[] args) {
	return new MyApplication ().run (args);
}
