#!/usr/bin/gjs

const Gio = imports.gi.Gio;
const GLib = imports.gi.GLib;
const Gtk = imports.gi.Gtk;
const Lang = imports.lang;

const ButtonExample = new Lang.Class ({
	Name: 'Button Example',

	/* Create the application itself
	   This boilerplate code is needed to build any GTK+ application. */
        _init: function () {
   	     this.application = new Gtk.Application ({
  	          application_id: 'org.example.jsbutton',
  	          flags: Gio.ApplicationFlags.FLAGS_NONE
   	     });

	// Connect 'activate' and 'startup' signals to the callback functions
	this.application.connect('activate', Lang.bind(this, this._onActivate));
	this.application.connect('startup', Lang.bind(this, this._onStartup));
	},

	// Callback function for 'activate' signal presents windows when active
	_onActivate: function () {
		this._window.present ();
	},

	// Callback function for 'startup' signal initializes menus and builds the UI
	_onStartup: function () {
		this._buildUI ();
	},




	// Build the application's UI
	_buildUI: function () {

		// Create the application window
        	this._window = new Gtk.ApplicationWindow  ({ application: this.application,
                                                     	     window_position: Gtk.WindowPosition.CENTER,
                                                     	     title: "GNOME Button",
                                                     	     default_height: 50,
                                                     	     default_width: 250 });

		// Create the button
		this.Button = new Gtk.Button ({label: "Click Me"});
		this._window.add (this.Button);

		// Bind it to a function that says what to do when the button is clicked
		this.Button.connect ("clicked", Lang.bind(this, this._clickHandler));

       	 	// Show the window and all child widgets
       	 	this._window.show_all();
	},

	// Here's the function that says what happens when the button is clicked
	_clickHandler: function () {
		this.Button.set_label ("Clicked!");
	}


});

// Run the application
let app = new ButtonExample ();
app.application.run (ARGV);
