//This is the application
public class MyApplication : Gtk.Application {
	public MyApplication () {
		Object (application_id: "org.example.dialog");
	}
	
	void on_response (Gtk.Dialog dialog, int response_id) {
		/*To see the int value of the ResponseType*/
		print ("response is %d\n", response_id);

		dialog.destroy ();
	}

	void on_button_click (Gtk.Button button) {
		var window = button.get_toplevel () as Gtk.Window;
		var dialog = new Gtk.Dialog.with_buttons ("A Gtk+ Dialog", window,
		                                          Gtk.DialogFlags.MODAL,
		                                          Gtk.Stock.OK, 
		                                          Gtk.ResponseType.OK, null);
		var content_area = dialog.get_content_area (); 
		var label = new Gtk.Label ("This demonstrates a dialog with a label");

		content_area.add (label);
		dialog.response.connect (on_response);
		dialog.show_all ();
	}

	public override void activate () {
		var window = new Gtk.Window ();
		window.set_default_size (200, 50);

		var button = new Gtk.Button.from_stock (Gtk.Stock.OK);
		button.clicked.connect (on_button_click);
		window.add (button);

		this.add_window (window);
		window.show_all ();
	}
}

//The main function creates the application and runs it.
int main (string[] args) {
	var app = new MyApplication ();
	return app.run (args);
}
