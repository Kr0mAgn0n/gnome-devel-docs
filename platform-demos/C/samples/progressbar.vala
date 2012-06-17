public class MyApplication : Gtk.Application {

	Gtk.ProgressBar progress_bar;

	protected override void activate () {
		var window = new Gtk.ApplicationWindow (this);
		window.set_title ("ProgressBar Example");
		window.set_position (Gtk.WindowPosition.CENTER);
		window.set_default_size (220, 20);

		progress_bar = new Gtk.ProgressBar ();
		window.add (progress_bar);
		window.show_all ();

		double fraction = 0.0;
		progress_bar.set_fraction (fraction);
		GLib.Timeout.add (500, fill);
		this.quit ();
	}

	bool fill () {
                double fraction = progress_bar.get_fraction ();
		fraction += 0.1; //increase by 10%

		progress_bar.set_fraction (fraction);

                /* This function is only called by GLib.Timeout.add while it returns true; */
		if (fraction < 1.0)
			return true;	
		else progress_bar.set_fraction (0.0);
		return true;
	}
}

public int main (string[] args) {
	var progress_bar_application = new MyApplication ();
	int status =  progress_bar_application.run (args);
	return status;
}
