public class MyWindow : Gtk.ApplicationWindow {

        void on_response (Gtk.Dialog dialog, int response_id) {
                /*To see the int value of the ResponseType*/
                print ("response is %d\n", response_id);

                dialog.destroy ();
        }

	void on_button_click (Gtk.Button button) {
                var dialog = new Gtk.Dialog.with_buttons ("A Gtk+ Dialog", this,
                                                          Gtk.DialogFlags.MODAL,
                                                          Gtk.Stock.OK,
                                                          Gtk.ResponseType.OK, null);

                var content_area = dialog.get_content_area ();
                var label = new Gtk.Label ("This demonstrates a dialog with a label");

                content_area.add (label);
                dialog.response.connect (on_response);
                dialog.show_all ();
	}

	internal MyWindow (MyApplication app) {
		Object (application: app, title: "GNOME Button");

		var button = new Gtk.Button.with_label ("Click Me");
		button.clicked.connect (on_button_click);
                button.show ();

                this.window_position = Gtk.WindowPosition.CENTER;
                this.set_default_size (250,50);
		this.add (button);
	}
}

public class MyApplication : Gtk.Application {
	protected override void activate () {
		new MyWindow (this).show ();
	}

	internal MyApplication () {
		Object (application_id: "org.example.MyApplication");
	}
}

public int main (string[] args) {
	return new MyApplication ().run (args);
}
