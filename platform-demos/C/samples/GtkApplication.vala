//Note to self: Python and JS need to import Glib for the menu

/*** You need to be running Gtk+-3.4 or later for this to work ***/

//A window in the application
public class Window : Gtk.ApplicationWindow {
	public Window (Application app) {
		Object (application: app, title: "GtkApplication Example");

		var label = new Gtk.Label ("Hello GtkApplication!");
		add (label);

		var about_action = new SimpleAction ("about", null);
		about_action.activate.connect (about);
		add_action (about_action);

		set_default_size (400, 200);
		show_all ();
	}

	void about () {
		string[] authors = { "GNOME Documentation Team", null };
		string[] documenters = { "GNOME Documentation Team", null };

		Gtk.show_about_dialog (this,
	                       "program-name", ("GtkApplication Example"),
	                       "copyright", ("Copyright \xc2\xa9 2012 GNOME Documentation Team"),
	                       "authors", authors,
	                       "documenters", documenters,
	                       "website", "http://developer.gnome.org",
	                       "website-label", ("GNOME Developer Website"),
	                       null);
	}
}

//This is the Application
public class Application : Gtk.Application {
	protected override void activate () {
		new Window (this);
	}

	protected override void startup () {
		base.startup ();

		var menu = new Menu ();
		menu.append ("About", "win.about");
		menu.append ("Quit", "app.quit");
		app_menu = menu;

		var quit_action = new SimpleAction ("quit", null);
		quit_action.activate.connect (quit);
		add_action (quit_action);
	}

	public Application () {
		Object (application_id: "org.example.application");
	}
}

//main function creates Application and runs it
int main (string[] args) {
	return new Application ().run (args);
}

