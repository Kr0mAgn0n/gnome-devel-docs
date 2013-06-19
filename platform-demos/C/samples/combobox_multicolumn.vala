class MyWindow : Gtk.ApplicationWindow {

	string[] file = {"Select", "New", "Open", "Save"};
	string[] stock_item = {"","gtk-new", "gtk-open", "gtk-save"};

	enum Column {
		FILE,
		STOCK_ITEM	
	}

	/* Constructor */
	internal MyWindow (MyApplication app) {
		Object (application: app, title: "Welcome to GNOME");

		this.set_default_size (200, -1);
		this.border_width = 10;

		Gtk.ListStore liststore = new Gtk.ListStore (2, typeof (string), typeof (string));

		for (int i = 0; i < file.length; i++){
			Gtk.TreeIter iter;
			liststore.append (out iter);
			liststore.set (iter, Column.FILE, file[i]);
			liststore.set (iter, Column.STOCK_ITEM, stock_item[i]);
		}

		Gtk.ComboBox combobox = new Gtk.ComboBox.with_model (liststore);

		/* CellRenderers render the data. */
		Gtk.CellRendererText cell = new Gtk.CellRendererText ();
		Gtk.CellRendererPixbuf cell_pb = new Gtk.CellRendererPixbuf ();
		
                /* we pack the cell into the beginning of the combobox, allocating
		 * no more space than needed;
		 * first the image, then the text;
		 * note that it does not matter in which order they are in the model,
		 * the visualization is decided by the order of the cellrenderers
		 */
		combobox.pack_start (cell_pb, false);
		combobox.pack_start (cell, false);

		/* associate a property of the cellrenderer to a column in the model
		 * used by the combobox
		 */
		combobox.set_attributes (cell_pb, "stock_id", Column.STOCK_ITEM);
		combobox.set_attributes (cell, "text", Column.FILE);

		/* Set the first item in the list to be selected (active). */
		combobox.set_active (0);

		/* Connect the 'changed' signal of the combobox
		 * to the signal handler (aka. callback function.
		 */
		combobox.changed.connect (this.item_changed);

		/* Add the combobox to this window */
		this.add (combobox);
		combobox.show ();
	}

	void item_changed (Gtk.ComboBox combo) {
		if (combo.get_active () !=0) {
			print ("You chose " + file [combo.get_active ()] +"\n");
		}
	}
}

class MyApplication : Gtk.Application {
        protected override void activate () {
                new MyWindow (this).show ();
        }
}

int main (string[] args) {
	return new MyApplication ().run (args);
}
