#!/usr/bin/gjs

var Gtk = imports.gi.Gtk;
Gtk.init(null, 0);

// Create window and give it a name
// You can't call it "window" as that name is a JavaScript keyword.
var sampleWindow = new Gtk.Window({type: Gtk.WindowType.TOPLEVEL});
sampleWindow.title = "Welcome to GNOME";

/* The "destroy" signal is sent out when you click the X button.
   Here, we connect that signal to the GTK+ function to close the window. */
sampleWindow.connect("destroy", function(){Gtk.main_quit()});

/* Here are a few ways we can customize our window.
   Try uncommenting them or changing their values! */
// sampleWindow.set_default_size (400,200);
// sampleWindow.set_has_resize_grip (false);
// sampleWindow.set_opacity (0.5);
// sampleWindow.maximize ();

// If the window has widgets in it, you'll want to use show_all() instead.
sampleWindow.show();

Gtk.main();
