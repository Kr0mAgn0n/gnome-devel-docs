public class MyToolbar : Gtk.Toolbar {

	Gtk.ApplicationWindow window;
	Gtk.ToolButton new_button;
	Gtk.ToolButton open_button;
	Gtk.ToolButton undo_button;
	Gtk.ToolButton fullscreen_button;
	Gtk.ToolButton leave_fullscreen_button;
	bool window_is_fullscreen = false;
 
	public MyToolbar (MyWindow window) {

		this.window = window;
	
		this.get_style_context ().add_class (Gtk.STYLE_CLASS_PRIMARY_TOOLBAR);
		
		new_button = new Gtk.ToolButton.from_stock (Gtk.Stock.NEW);
		new_button.is_important = true; //decides whether to show the label
		this.add (new_button);
		new_button.show ();
		new_button.clicked.connect (on_new_clicked);

	  	open_button = new Gtk.ToolButton.from_stock (Gtk.Stock.OPEN);
        	open_button.is_important = true;
        	this.add (open_button);
		open_button.clicked.connect (on_open_clicked);

      		undo_button = new Gtk.ToolButton.from_stock (Gtk.Stock.UNDO);
		undo_button.is_important = true;
		this.add (undo_button);
		undo_button.clicked.connect (on_undo_clicked);

		fullscreen_button = new Gtk.ToolButton.from_stock (Gtk.Stock.FULLSCREEN);
		fullscreen_button.is_important = true;
		this.add (fullscreen_button);
		fullscreen_button.clicked.connect (on_toggle_fullscreen);
	
		leave_fullscreen_button = new Gtk.ToolButton.from_stock (Gtk.Stock.LEAVE_FULLSCREEN);
		leave_fullscreen_button.is_important = true;
		leave_fullscreen_button.clicked.connect (on_toggle_fullscreen);
	}

	void on_new_clicked () {
		print ("You clicked the \"New\" ToolButton.\n");
	}
	
	void on_open_clicked () {
			print ("You clicked the \"Open\" ToolButton.\n");
	}
	
	void on_undo_clicked () {
			print ("You clicked the \"Undo\" ToolButton.\n");
	}

	void on_toggle_fullscreen (Gtk.ToolButton toolbutton) {
		if (window_is_fullscreen) {
			this.window.unfullscreen ();
			window_is_fullscreen = false;
			this.remove (toolbutton);
			this.add (fullscreen_button);
			fullscreen_button.show ();
		}
		else {
			this.window.fullscreen ();
			window_is_fullscreen = true;
			this.remove (toolbutton);
			this.add (leave_fullscreen_button);
			leave_fullscreen_button.show ();
		}
	}
}

class MyWindow : Gtk.ApplicationWindow {
	
	internal MyWindow (MyApplication app) {
		Object (application: app, title: "Toolbar Example");

		this.set_default_size (400, 200);
		var grid = new Gtk.Grid ();
		this.add (grid);

		MyToolbar toolbar = new MyToolbar (this);
		toolbar.set_hexpand (true);
		grid.attach (toolbar, 1, 1, 1, 1);
		toolbar.show ();
	}
}

class MyApplication : Gtk.Application {
	protected override void activate () {
		new MyWindow (this).show_all ();
	}

	internal MyApplication () {
		Object (application_id: "org.example.toolbar");
	}
}

int main (string[] args) {
	return new MyApplication ().run (args);
}
