public class MyWindow : Gtk.ApplicationWindow {

	Gtk.ProgressBar progress_bar;
	uint source_id;

	internal MyWindow (MyApplication app) {
		Object (application: app, title: "ProgressBar Example");
		this.set_default_size (220, 20);
		
		progress_bar = new Gtk.ProgressBar ();
		this.add (progress_bar);
		progress_bar.show ();

		source_id = GLib.Timeout.add (100, pulse);
	}

	protected override bool key_press_event (Gdk.EventKey event) {
		if (source_id == 0)
			source_id = GLib.Timeout.add (100, pulse);
		else {
			GLib.Source.remove (source_id);
			source_id = 0;
		}
		return true;
	}

	bool pulse () {
		progress_bar.pulse ();
		return true;
	}
}

public class MyApplication : Gtk.Application {

	protected override void activate () {
		MyWindow window = new MyWindow (this);
		window.show ();
	}

	internal MyApplication () {
		Object (application_id: "org.example.ProgressBar");
	}
}

public int main (string[] args) {
	var progress_bar_application = new MyApplication ();
	int status =  progress_bar_application.run (args);
	return status;
}
