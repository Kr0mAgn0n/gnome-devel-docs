public class MyWindow : Gtk.ApplicationWindow {
        internal MyWindow (MyApplication app) {
                Object (application: app, title: "FontChooserWidget");

		var font_chooser = new Gtk.FontChooserWidget ();
		font_chooser.set_font ("Sans");
		font_chooser.set_preview_text ("This is an example of preview text!");
		this.add (font_chooser);

		font_chooser.notify["font"].connect (() => {
			print ("font: %s\n", font_chooser.get_font ().to_string ());
			print ("desc: %s\n", font_chooser.get_font_desc ().to_string ());
			print ("face: %s\n", font_chooser.get_font_face ().get_face_name ());
			print ("size: %d\n", font_chooser.get_font_size ());
			print ("family: %s\n", font_chooser.get_font_family ().get_name ());
			print ("monospace: %s\n\n", font_chooser.get_font_family ().is_monospace ().to_string ());
		});

                this.show_all ();
        }
}

public class MyApplication : Gtk.Application {
        protected override void activate () {
                new MyWindow (this).show ();
        }
}

public int main (string[] args) {
        return new MyApplication ().run (args);
}

