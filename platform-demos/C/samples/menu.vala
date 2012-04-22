public class MyWindow : Gtk.ApplicationWindow {
	void reverse_label (Gtk.Button button) {
		button.label = button.label.reverse ();
	}

	internal MyWindow (MyApplication app) {
		Object (application: app, title: "My Application");

		var button = new Gtk.Button.with_label ("Click me!");
		button.clicked.connect (reverse_label);
		this.add (button);
		button.show ();
	}
}

public class MyApplication : Gtk.Application {
	protected override void activate () {
		new_window ();
	}

	void new_window () {
		new MyWindow (this).show ();
	}

	const ActionEntry[] action_entries = {
		{ "new", new_window },
		{ "quit", quit }
	};

	internal MyApplication () {
		Object (application_id: "org.example.MyApplication");
	}

	protected override void startup () {
		base.startup ();

		this.add_action_entries (action_entries, this);

		var menu = new Menu ();
		menu.append ("New", "app.new");
		menu.append ("Quit", "app.quit");
		this.app_menu = menu;
	}
}

public int main (string[] args) {
	return new MyApplication ().run (args);
}
