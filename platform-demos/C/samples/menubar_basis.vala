public class MyWindow : Gtk.ApplicationWindow {
	internal MyWindow (MyApplication app) {
		Object (application: app, title: "MenuBar Example");
		this.set_default_size (200, 200);
	}
}

class MyApplication: Gtk.Application {
	protected override void activate () {
		new MyWindow (this).show ();
	}
	protected override void startup () {
		base.startup ();

		/* Setup menubar. */
		/* Get the UI file. */
		var builder = new Gtk.Builder ();
		try {
			builder.add_from_file ("menubar_basis.ui");
		/* Handle the exception. */
		} catch (Error e) {
			error ("Unable to load file: %s", e.message);
		}

		/* Get the menubar from the builder. */
		this.menubar = builder.get_object ("menubar") as MenuModel;
	}
}

/* main creates and runs the application. */
public int main (string[] args) {
	return new MyApplication ().run (args);
}
