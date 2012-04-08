//to compile: valac newway.vala --pkg gtk+-3.0
//to run: ./newway

class MyApplication : Gtk.Application {
	protected override void activate () {
		var window = new Gtk.ApplicationWindow (this);
		window.add (new Gtk.Label ("Hello world!\n"));
		window.show_all ();
	}

	void do_new () {
		activate ();
	}

	void do_move (SimpleAction action, Variant? parameter) {
		print ("moved: %s\n", (string) parameter);
	}

	const ActionEntry[] actions = {
		{ "new", do_new },
		{ "move", do_move, "s" }
	};

	protected override void startup () {
		base.startup ();
		add_action_entries (actions, this);

		var builder = new Gtk.Builder ();
		builder.add_from_file ("newway-menus.ui");
		app_menu = builder.get_object ("app-menu") as MenuModel;
	}

	public MyApplication () {
		Object (application_id: "org.gnome.HelloWorld");
	}
}

int main (string[] args) {
	var app = new MyApplication ();
	return app.run ();
}
