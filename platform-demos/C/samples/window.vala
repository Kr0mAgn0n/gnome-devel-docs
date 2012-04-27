//This is the application
public class Application : Gtk.Application {
	public Application () {
		Object (application_id: "org.example.window");
	}
	
	public override void activate () {
		var window = new Gtk.Window ();
		window.title = "Welcome to GNOME";

		/*
		 The following 3 lines are included here to introduce
		 you to ways you can adjust the toplevel window to suit
		 your needs.  Uncomment them to see what they do.
		*/
		//window.border_width = 10;
		//window.set_default_size (350, 70);
		//window.window_position = Gtk.WindowPosition.CENTER;

		window.show ();
		this.add_window (window);
	}
}

//The main function creates the application and runs it.
int main (string[] args) {
	var app = new Application ();
	return app.run (args);
}
