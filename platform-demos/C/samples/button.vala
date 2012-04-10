using Gtk;

/*callback for the "clicked" signal.*/
void button_clicked_cb () {
	stdout.printf ("You clicked the button!\n");
	//TODO: add a modal window
}

int main (string[] args) {

	init (ref args);

	var window = new Window ();
	window.title = "GNOME Button";
	window.set_default_size (250,50);

	var button = new Button.with_label ("Click Me");
	window.add (button);

	window.window_position = WindowPosition.CENTER;

	/* The "clicked" signal is emitted when the
	   button is clicked.  The signal is connected to
	   the button_clicked_cb method defined above.*/
	button.clicked.connect (button_clicked_cb);

	/*The "destroy" signal is emitted when the x
	  in the top right of the window is clicked.
	  The destroy signal is connected to the
	  main_quit method, which destroys the window
	  and exits the program.*/
	window.destroy.connect (main_quit);

	window.show_all ();

	Gtk.main ();
	return 0;
}
