#!/usr/bin/gjs

const Gio = imports.gi.Gio;
const GLib = imports.gi.GLib;
const Gtk = imports.gi.Gtk;
const Lang = imports.lang;

const Application = new Lang.Class ({
    Name: 'Application',

    //create the application
    _init: function () {
        this.application = new Gtk.Application ({
            application_id: 'org.example.myapp',
            flags: Gio.ApplicationFlags.FLAGS_NONE
        });

       //connect to 'activate' and 'startup' signals to the callback functions
       this.application.connect('activate', Lang.bind(this, this._onActivate));
       this.application.connect('startup', Lang.bind(this, this._onStartup));
    },

    //create the UI (in this case it's just the ApplicationWindow
    _buildUI: function () {
        this._window = new Gtk.ApplicationWindow  ({ application: this.application,
                                                   window_position: Gtk.WindowPosition.CENTER,
                                                   title: "Welcome to GNOME" });

        //uncommenting the line below will change the window size
        //this._window.set_default_size(600, 400);

        //show the window and all child widgets (none in this case)
        this._window.show_all();
    },

    //callback function for 'activate' signal
    _onActivate: function () {
        this._window.present ();
    },

    //callback function for 'startup' signal
    _onStartup: function () {
        this._buildUI ();
    }
});

//run the application
let app = new Application ();
app.application.run (ARGV);
