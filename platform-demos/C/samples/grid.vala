public class MyWindow : Gtk.ApplicationWindow {

	internal MyWindow (MyApplication app) {
		Object (application: app, title: "Grid Example");
		var grid = new Gtk.Grid();
		var progress_bar = new Gtk.ProgressBar ();
		progress_bar.show ();

		var button = new Gtk.Button.with_label ("Button");
		button.clicked.connect (() => {
				progress_bar.pulse ();
		});
		button.show ();

		this.add(grid);
		grid.attach(button, 1, 1, 1, 1);
		grid.attach_next_to (progress_bar, button, Gtk.PositionType.BOTTOM, 1, 1);
		grid.show ();
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
