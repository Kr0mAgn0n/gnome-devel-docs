class MyWindow : Gtk.ApplicationWindow {
	
	string[] distros = {"Select distribution", "Fedora", "Mint", "Suse"};
	
	internal MyWindow (MyApplication app) {
		Object (application: app, title: "Welcome to GNOME");

		this.set_default_size (200, -1);
		this.border_width = 10;

		Gtk.ListStore liststore = new Gtk.ListStore (1, typeof (string));

		for (int i = 0; i < distros.length; i++){
			Gtk.TreeIter iter;
			liststore.append (out iter);
			liststore.set (iter, 0, distros[i]);
		}

		Gtk.ComboBox combobox = new Gtk.ComboBox.with_model (liststore);
		Gtk.CellRendererText cell = new Gtk.CellRendererText ();
		combobox.pack_start (cell, false);

		//set the attributes in the list as the attributes of the cell. 
		combobox.set_attributes (cell, "text", 0);

		combobox.set_active (0);

		combobox.changed.connect (this.item_changed);
		
		this.add (combobox);
		combobox.show ();
	}

	void item_changed (Gtk.ComboBox combo) {
		if (combo.get_active () !=0) {
			print ("You chose " + distros [combo.get_active ()] +"\n");
		}
	}
}

class MyApplication : Gtk.Application {
	protected override void activate () {
		new MyWindow (this).show_all ();
	}

	internal MyApplication () {
		Object (application_id: "org.example.MyApplication");
	}
}

int main (string[] args) {
	return new MyApplication ().run (args);
}
