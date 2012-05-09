class MyWindow : Gtk.ApplicationWindow {
	
	internal MyWindow (MyApplication app) {
		Object (application: app, title: "CheckButton Example");

		this.set_default_size (300, 100);
		this.border_width = 10;
	
		var checkbutton = new Gtk.CheckButton.with_label ("Show Title");
		checkbutton.toggled.connect (toggled_cb);
		this.add (checkbutton);
		checkbutton.set_active (true);
		checkbutton.show ();
	}

	void toggled_cb (Gtk.ToggleButton checkbutton) {
		if (checkbutton.get_active())
			this.set_title ("CheckButton Example");
		else
			this.set_title ("");
	}
}

class MyApplication : Gtk.Application {
	protected override void activate () {
		new MyWindow (this).show ();
	}

	internal MyApplication () {
		Object (application_id: "org.example.checkbutton");
	}
}

int main (string[] args) {
	return new MyApplication ().run (args);
}
