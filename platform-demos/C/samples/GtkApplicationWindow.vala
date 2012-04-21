public class MyWindow : Gtk.ApplicationWindow {
	internal MyWindow (MyApplication app) {
		Object (application: app, title: "Welcome to GNOME");
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
