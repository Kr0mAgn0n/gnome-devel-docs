#!/usr/bin/gjs

const Gio = imports.gi.Gio;
const GLib = imports.gi.GLib;
const Gtk = imports.gi.Gtk;
const Lang = imports.lang;

const GridExample = new Lang.Class ({
	Name: 'Grid Example',

	/* Create the application itself
	   This boilerplate code is needed to build any GTK+ application. */
        _init: function () {
   	     this.application = new Gtk.Application ({
  	          application_id: 'org.example.jsgrid',
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
                                                     	     title: "Grid Example"});

		// Create the grid
		this.Grid = new Gtk.Grid ();

		// Create the widgets inside the grid
		this.progressBar = new Gtk.ProgressBar ();
		this.Button = new Gtk.Button ({ label: "Button" });
		this.Button.connect ("clicked", Lang.bind(this, this._clickHandler));

		// Assemble the grid
		this._window.add (this.Grid);
		this.Grid.attach (this.Button, 1, 1, 1, 1);
		this.Grid.attach_next_to (this.progressBar, this.Button, Gtk.PositionType.BOTTOM, 1, 1);

       	 	// Show the window and all child widgets
       	 	this._window.show_all();
	},

	// Here's the function that says what happens when the button is clicked
	_clickHandler: function () {
		this.progressBar.pulse ();
	}


});

// Run the application
let app = new GridExample ();
app.application.run (ARGV);
