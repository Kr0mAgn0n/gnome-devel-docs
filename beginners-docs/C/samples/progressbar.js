#!/usr/bin/gjs

const Gio = imports.gi.Gio;
const GLib = imports.gi.GLib;
const Gtk = imports.gi.Gtk;
const Lang = imports.lang;

const ProgressBarExample = new Lang.Class({
    Name: 'ProgressBar Example',

    // Create the application itself
        _init: function() {
        this.application = new Gtk.Application({
            application_id: 'org.example.jsprogressbar',
            flags: Gio.ApplicationFlags.FLAGS_NONE
        });

    // Connect 'activate' and 'startup' signals to the callback functions
    this.application.connect('activate', Lang.bind(this, this._onActivate));
    this.application.connect('startup', Lang.bind(this, this._onStartup));
    },

    // Callback function for 'activate' signal presents windows when active
    _onActivate: function() {
        this._window.present();
    },

    // Callback function for 'startup' signal builds the UI
    _onStartup: function() {
        this._buildUI ();
    },



    // Build the application's UI
    _buildUI: function() {

        // Create the application window
            this._window = new Gtk.ApplicationWindow({ application: this.application,
                                                       window_position: Gtk.WindowPosition.CENTER,
                                                       default_height: 20,
                                                       default_width: 220,
                                                       title: "ProgressBar Example"});

        // Create the progress bar
        this.progressBar = new Gtk.ProgressBar ();
        this._window.add(this.progressBar);

        // Start the function that pulses the bar every 100 milliseconds
        this.sourceID = GLib.timeout_add(GLib.PRIORITY_DEFAULT, 100, Lang.bind(this, this._barPulse));

        // Connect a keypress event to the function that toggles the bar to start or stop pulsing
        this._window.connect("key-press-event", Lang.bind(this, this._onKeyPress));

            // Show the window and all child widgets
            this._window.show_all();
    },



    // Pulse the progressbar (unless it has been disabled by a keypress)
    _barPulse: function() {
        this.progressBar.pulse();
        return true;
    },

    // Start or stop the progressbar when a key is pressed
    _onKeyPress: function() {
        if (this.sourceID == 0)
            this.sourceID = GLib.timeout_add(GLib.PRIORITY_DEFAULT, 100, Lang.bind(this, this._barPulse));
        else {
            GLib.source_remove(this.sourceID);
            this.sourceID = 0;
        }
    }

});

// Run the application
let app = new ProgressBarExample ();
app.application.run (ARGV);
