//to compile: valac hello-world.vala --pkg gtk+-3.0
//to run: ./hello-world

class HelloWorld : Gtk.Application {

        /* constructor */
	public HelloWorld () {
		Object (application_id: "org.gnome.HelloWorld");
	}

	protected override void activate () {
		var window = new Gtk.ApplicationWindow (this);
		window.add (new Gtk.Label ("Hello world!\n"));
		window.show_all ();
	}
}

int main (string[] args) {
	var app = new HelloWorld ();
	return app.run ();
}
