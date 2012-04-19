#!/usr/bin/gjs

// Initialize GTK
var Gtk = imports.gi.Gtk;
Gtk.init(null, 0);

// Create and set up the window
var buttonWindow = new Gtk.Window({type: Gtk.WindowType.TOPLEVEL});
buttonWindow.title = "GNOME Button";
buttonWindow.set_default_size (250,50);
buttonWindow.connect("destroy", function(){Gtk.main_quit()});

// Create the button and add it to the window
var theButton = new Gtk.Button ({label: "Click me"});
buttonWindow.add (theButton);

/* Say what to do when the button is clicked
   You can connect it to more useful things if you like.
   Note that it uses the same syntax as line 11, above.
   Instead of saying what to do when we get a "destroy"
   signal from the window, we're saying what to do when
   we get a "clicked" signal from the button. */
var clicks = 0;
theButton.connect ("clicked", function () {
	clicks++;
	this.theButton.set_label("Number of clicks: " + clicks + "!");
});

// Show the window and the widget inside it, and start the application
buttonWindow.show_all();
Gtk.main();
