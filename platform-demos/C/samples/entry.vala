public class MyWindow : Gtk.ApplicationWindow {
	
	void on_activate (Gtk.Entry entry) {
		name = entry.get_text ();
		print ("Hello " + name + "!\n");
	}

	internal MyWindow (MyApplication app) {
		Object (application: app, title: "What is your name?");

		var name_box = new Gtk.Entry ();
		name_box.activate.connect (on_activate);
		name_box.show ();

		this.set_default_size (300, 100);
		this.border_width = 10;
		this.add (name_box);
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
