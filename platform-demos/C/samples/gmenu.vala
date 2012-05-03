//A window in the application
public class Window : Gtk.ApplicationWindow {
	public Window (Application app) {
		Object (application: app, title: "Gmenu Example");

		var about_action = new SimpleAction ("about", null);
		about_action.activate.connect (about);
		this.add_action (about_action);

		this.show_all ();
	}

	void about () {
		print ("This does nothing.  It is only a demonstration\n");
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
		this.app_menu = menu;

		var quit_action = new SimpleAction ("quit", null);
		//quit_action.activate.connect (this.quit);
		this.add_action (quit_action);
	}

	public Application () {
		Object (application_id: "org.example.application");
	}
}

//main function creates Application and runs it
int main (string[] args) {
	return new Application ().run (args);
}

