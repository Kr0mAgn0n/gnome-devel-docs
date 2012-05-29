#!/usr/bin/gjs

const Gio = imports.gi.Gio;
const GLib = imports.gi.GLib;
const Gtk = imports.gi.Gtk;
const Lang = imports.lang;

const LinkButtonExample = new Lang.Class ({
    Name: 'LinkButton Example',

    // Create the application itself
        _init: function () {
        this.application = new Gtk.Application ({
              application_id: 'org.example.jslinkbutton',
              flags: Gio.ApplicationFlags.FLAGS_NONE
         });

    // Connect 'activate' and 'startup' signals to the callback functions
    this.application.connect('activate', Lang.bind(this, this._onActivate));
    this.application.connect('startup', Lang.bind(this, this._onStartup));
    },

    // Callback function for 'activate' signal presents window when active
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
                                                 title: "GNOME LinkButton",
                                                 default_height: 50,
                                                 default_width: 250 });

        // Create the LinkButton and have it link to live.gnome.org
        this.LinkButton = new Gtk.LinkButton ({label: "Link to GNOME live!",
                               uri: "http://live.gnome.org"});
        this._window.add (this.LinkButton);

    // Show the window and all child widgets
    this._window.show_all();
    },

});

// Run the application
let app = new LinkButtonExample ();
app.application.run (ARGV);
