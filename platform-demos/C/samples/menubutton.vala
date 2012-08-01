public class MyWindow : Gtk.ApplicationWindow {

	internal MyWindow (MyApplication app) {
		Object (application: app, title: "MenuButton Example");
		this.set_default_size (600, 400);
		var grid = new Gtk.Grid ();

		var menubutton = new Gtk.MenuButton();
		menubutton.set_size_request(80, 35);

		var menumodel = new Menu ();
		menumodel.append ("New", "app.new");
		menubutton.set_menu_model (menumodel);

		this.add(grid);
		grid.attach(menubutton, 0, 0, 1, 1);
	}
}

public class MyApplication : Gtk.Application {
	protected override void activate () {
		new MyWindow (this).show_all ();
	}

	internal MyApplication () {
		Object (application_id: "org.example.MyApplication");

	}

    /* Override the 'startup' signal of GLib.Application. */
	protected override void startup () {
		base.startup ();
		var new_action = new SimpleAction ("new", null);
		new_action.activate.connect (this.new_cb);
		this.add_action (new_action);
}

	void new_cb (SimpleAction simple, Variant? parameter) {
		print ("You clicked \"New\"\n");
	}
}

public int main (string[] args) {
	return new MyApplication ().run (args);
}
