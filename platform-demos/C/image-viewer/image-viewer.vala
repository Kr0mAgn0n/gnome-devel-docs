using GLib;
using Gtk;

public class Main : Object
{
	private Window window;
	private Image image;
		
	public Main () {
	
		window = new Window ();
		window.set_title ("Image Viewer in Vala");
		
		// Set up the UI
		var box = new Box (Orientation.VERTICAL, 5);
		var button = new Button.with_label ("Open image");
		image = new Image ();
		
		box.pack_start (image, true, true, 0);
		box.pack_start (button, false, false, 0);
		window.add (box);
		
		// Show open dialog when opening a file
		button.clicked.connect (on_open_image);
		
		window.show_all ();
		window.destroy.connect (main_quit);
	}
	
	[CCode (instance_pos = -1)]
	public void on_open_image (Button self) {
		var filter = new FileFilter ();
		var dialog = new FileChooserDialog ("Open image",
		                                    window,
		                                    FileChooserAction.OPEN,
		                                    Stock.OK,     ResponseType.ACCEPT,
		                                    Stock.CANCEL, ResponseType.CANCEL);
		filter.add_pixbuf_formats ();
		dialog.add_filter (filter);
		
		switch (dialog.run ()) 
		{
			case ResponseType.ACCEPT:
				var filename = dialog.get_filename ();
				image.set_from_file (filename);
				break;
			default:
				break;
		}
		dialog.destroy ();
	}

	static int main (string[] args) {
		Gtk.init (ref args);
		var app = new Main ();
		
		Gtk.main ();
		
		return 0;
	}
}

