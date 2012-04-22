public class MyWindow : Gtk.ApplicationWindow {
	void reverse_label (Gtk.Button button) {
		button.label = button.label.reverse ();
	}

	internal MyWindow (MyApplication app) {
		Object (application: app, title: "GNOME Button");

		var button = new Gtk.Button.with_label ("Click Me");
		button.clicked.connect (reverse_label);
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
