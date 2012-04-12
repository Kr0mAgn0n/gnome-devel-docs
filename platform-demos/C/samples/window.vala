int main (string[] args) {

	Gtk.init (ref args);

	var window = new Gtk.Window ();
	window.title = "Welcome to GNOME";

	/*
	 The following 3 lines are included here to introduce
	 you to ways you can adjust the toplevel window to suit
	 your needs. Uncomment them to see what they do.
	 */
	//window.border_width = 10;
	//window.set_default_size (350, 70);
	//window.window_position = Gtk.WindowPosition.CENTER;

	/*The destroy signal is emitted when the x
	  in the top right of the window is clicked.*/
	window.destroy.connect (Gtk.main_quit);

	/*The show () method only shows the widget it is called on.
      If the widget has children (for example a label or a button,
      the method show_all () should be used to show the widget and
       the child widgets.*/
	window.show ();

	Gtk.main ();
	return 0;
}
