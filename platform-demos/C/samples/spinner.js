#!/usr/bin/gjs

const Gio = imports.gi.Gio;
const GLib = imports.gi.GLib;
const Gtk = imports.gi.Gtk;
const Gdk = imports.gi.Gdk;
const Lang = imports.lang;

const SpinnerExample = new Lang.Class ({
    Name: 'Spinner Example',

    // Create the application itself
    _init: function () {
        this.application = new Gtk.Application ({
            application_id: 'org.example.jsspinner',
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

    // Callback function for 'startup' signal builds the UI
    _onStartup: function () {
        this._buildUI ();
    },



    // Build the application's UI
    _buildUI: function () {

        // Create the application window
        this._window = new Gtk.ApplicationWindow  ({
            application: this.application,
            window_position: Gtk.WindowPosition.CENTER,
            title: "Spinner Example",
            default_height: 200,
            default_width: 200,
            border_width: 30 });

        // Create a spinner which starts spinning automatically
        this._spinner = new Gtk.Spinner ({active: true});
        this._window.add (this._spinner);

        // Connect a keypress event to the function that makes it start or stop spinning
        this._window.connect("key-press-event", Lang.bind(this, this._onKeyPress));

        // Show the window and all child widgets
        this._window.show_all();
    },



    _onKeyPress: function(widget, event) {

        // Get the value of the key that was pressed
        let keyval = event.get_keyval()[1];

        // If it was the spacebar, toggle the spinner to start or stop
        if (keyval == Gdk.KEY_space) {
            if (this._spinner.active == true)
                this._spinner.stop();
            else
                this._spinner.start();
        }
    }


});

// Run the application
let app = new SpinnerExample ();
app.application.run (ARGV);
