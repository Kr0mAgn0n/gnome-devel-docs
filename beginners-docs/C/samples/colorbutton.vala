/* This is the application. */
public class MyApplication : Gtk.Application {
	Gtk.Label label;

	/* Override the 'activate' signal of GLib.Application. */
	protected override void activate () {
		/* Create the window of this application and show it. */
		var window = new Gtk.ApplicationWindow (this);
		window.title = "ColorButton";
		window.set_default_size (150, 50);
		window.set_border_width (10);

		/* Create a new ColorButton with default blue. */
		var blue = Gdk.RGBA ();
		blue.parse ("blue");
		var colorbutton = new Gtk.ColorButton.with_rgba (blue);

		label = new Gtk.Label ("Click to choose a color");

		var grid = new Gtk.Grid ();
		grid.attach (colorbutton, 0, 0, 1, 1);
		grid.attach_next_to (label, colorbutton, Gtk.PositionType.BOTTOM, 1, 1);

		colorbutton.color_set.connect (this.on_color_set);

		window.add (grid);
		window.show_all ();
	}

	void on_color_set (Gtk.ColorButton button) {
		var color =  button.get_rgba ();
		label.set_text ("RGBA: " + color.to_string());
	}
}

/* main creates and runs the application. */
public int main (string[] args) {
	return new MyApplication ().run (args);
}
