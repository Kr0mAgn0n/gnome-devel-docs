class MyWindow: Gtk.ApplicationWindow {

	/* MyWindow instance variables. */
	GLib.File? file;
	Gtk.TextBuffer buffer;
	Gtk.TextView textview;
	Gtk.ScrolledWindow scrolled_window;

	/* Create ActionEntries. */
	const ActionEntry[] actions = {
		{ "new", new_cb },
		{ "open", open_cb },
		{ "save", save_cb },
		{ "save-as", save_as_cb }
	};

	/* Constructor creates MyWindow, and add the scrolled_window. */
	internal MyWindow (MyApplication app) {
		Object (application: app, title: "FileChooserDialog Example");
		this.set_default_size (400, 400);

		/* Add the ActionEntries to MyWindow. */
		this.add_action_entries (actions, this);

		buffer = new Gtk.TextBuffer (null); //stores text to be displayed
		textview = new Gtk.TextView.with_buffer (buffer); //displays TextBuffer
		textview.set_wrap_mode (Gtk.WrapMode.WORD); //sets line wrapping

		scrolled_window = new Gtk.ScrolledWindow (null, null);
		scrolled_window.set_policy (Gtk.PolicyType.AUTOMATIC,
		                            Gtk.PolicyType.AUTOMATIC);

		scrolled_window.add (textview);
		scrolled_window.set_border_width (5);

        this.add (scrolled_window);
		this.show_all ();
	}

	void new_cb (SimpleAction action, Variant? parameter) {
		file = null;
		buffer.set_text ("");
		print ("New file created\n");
	}

	/* Create FileChooserDialog in OPEN mode. */
	void open_cb (SimpleAction action, Variant? parameter) {

		var open_dialog = new Gtk.FileChooserDialog ("Pick a file",
		                                             this as Gtk.Window,
		                                             Gtk.FileChooserAction.OPEN,
		                                             Gtk.Stock.CANCEL,
		                                             Gtk.ResponseType.CANCEL,
		                                             Gtk.Stock.OPEN,
		                                             Gtk.ResponseType.ACCEPT);

		open_dialog.local_only = false; //allow for uri
		open_dialog.set_modal (true);
		open_dialog.response.connect (open_response_cb);
		open_dialog.show ();
	}

	/* Either open the file and load the file contents or cancel. */
	void open_response_cb (Gtk.Dialog dialog, int response_id) {
		var open_dialog = dialog as Gtk.FileChooserDialog;

		switch (response_id) {
			case Gtk.ResponseType.ACCEPT: //open the file
				file = open_dialog.get_file();

				uint8[] file_contents;

				try {
					file.load_contents (null, out file_contents, null);
				}
				catch (GLib.Error err) { //handle the exception
					error ("%s\n", err.message);
				}
				/* Set the buffer text to be the contents of the file. */
				buffer.set_text ((string) file_contents,
				                 file_contents.length);

				print ("opened: %s\n", (open_dialog.get_filename ()));
				break;

			case Gtk.ResponseType.CANCEL:
				print ("cancelled: FileChooserAction.OPEN\n");
				break;
		}
		dialog.destroy ();
	}


	/* Create FileChooserDialog in SAVE mode. */
	void save_as_cb (SimpleAction action, Variant? parameter) {
		var save_dialog = new Gtk.FileChooserDialog ("Pick a file",
		                                             this as Gtk.Window,
		                                             Gtk.FileChooserAction.SAVE,
		                                             Gtk.Stock.CANCEL,
		                                             Gtk.ResponseType.CANCEL,
		                                             Gtk.Stock.SAVE,
		                                             Gtk.ResponseType.ACCEPT);

		save_dialog.set_do_overwrite_confirmation (true);
		save_dialog.set_modal (true);
		if (file != null) {
			try {
				(save_dialog as Gtk.FileChooser).set_file (file);
			}
			catch (GLib.Error error) {
				print ("%s\n", error.message);
			}
		}
		save_dialog.response.connect (save_as_response_cb);
		save_dialog.show ();
	}

	void save_as_response_cb (Gtk.Dialog dialog, int response_id) {
		var save_dialog = dialog as Gtk.FileChooserDialog;

		switch (response_id) {
			case Gtk.ResponseType.ACCEPT:
				file = save_dialog.get_file();
				this.save_to_file ();
				break;
			default:
				break;
		}
			dialog.destroy ();
	}

	/* Save the existing contents to the file.
	 * If file does not exist, call save_as_cb.
	 */
	void save_cb (SimpleAction action, Variant? parameter) {
		if (file != null) {
			this.save_to_file ();
		}
		else {
			save_as_cb (action, parameter);
		}
	}

	void save_to_file (){
		Gtk.TextIter start;
		Gtk.TextIter end;

		buffer.get_bounds (out start, out end);
		string current_contents = buffer.get_text (start, end, false);
		try {
				file.replace_contents (current_contents.data, null, false,
				                       GLib.FileCreateFlags.NONE, null, null);

				print ("saved: %s\n", file.get_path ());
		}
		catch (GLib.Error err) {
			error ("%s\n", err.message);
		}
	}
}

/* This is the application */
class MyApplication: Gtk.Application {
	protected override void activate () {
		new MyWindow (this).show_all;
	}

	const ActionEntry[] actions = {
		{ "quit", quit_cb }
	};

	void quit_cb (SimpleAction action, Variant? parameter) {
		this.quit ();
	}

	protected override void startup () {
		base.startup ();

		/* Setup actions */
		this.add_action_entries (actions, this);

		/* Setup menus */
		var builder = new Gtk.Builder ();
		try {
			builder.add_from_file ("filechooserdialog.ui");
		} catch (GLib.Error err) {
			error ("Unable to load file: %s\n", err.message);
		}
		this.app_menu = builder.get_object ("appmenu") as MenuModel;
	}
}

/* main creates and runs the application. */
public int main (string[] args) {
	return new MyApplication ().run (args);
}
