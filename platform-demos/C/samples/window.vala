using Gtk;

int main (string[] args) {

	init (ref args);

	var window = new Window ();
	window.title = "Welcome to GNOME";

	//window.border_width = 10;
	//window.window_position = WindowPosition.CENTER;
	//window.set_default_size (350, 70);

	/*The destroy signal is emitted when the x
	  in the top right of the window is clicked.*/
	window.destroy.connect (main_quit);

	window.show ();

	Gtk.main ();
	return 0;
}
