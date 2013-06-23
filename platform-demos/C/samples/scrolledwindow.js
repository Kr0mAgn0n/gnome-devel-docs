#!/usr/bin/gjs

const GObject = imports.gi.GObject;
const Gtk = imports.gi.Gtk;
const Lang = imports.lang;

const ScrolledWindowExample = new Lang.Class ({
    Name: 'ScrolledWindow Example',

    // Create the application itself
    _init: function () {
        this.application = new Gtk.Application({ application_id: 'org.example.jscrolledwindow' });

        // Connect 'activate' and 'startup' signals to the callback functions
        this.application.connect('activate', Lang.bind(this, this._onActivate));
        this.application.connect('startup', Lang.bind(this, this._onStartup));
    },

    // Callback function for 'activate' signal presents windows when active
    _onActivate: function() {
        this.window.present();
    },

    // Callback function for 'startup' signal builds the UI
    _onStartup: function() {
        this._buildUI ();
    },

    // Build the application's UI
    _buildUI: function() {
        // Create the application window
        this.window = new Gtk.ApplicationWindow  ({ application: this.application,
                                                    window_position: Gtk.WindowPosition.CENTER,
                                                    title: "Scrolled Window Example",
                                                    default_width: 200,
                                                    default_height: 200,
                                                    border_width: 10 });
        // the scrolledwindow
        this.scrolledWindow = new Gtk.ScrolledWindow();
        this.scrolledWindow.set_border_width(10);
        // there is always the scrollbar (otherwise: AUTOMATIC - only if needed - or NEVER)
        this.scrolledWindow.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS);
        // an image - slightly larger than the window
        this.image = new Gtk.Image();
        this.image.set_from_file("gnome-image.png");

        // add the image to the scrolledwindow
        this.scrolledWindow.add_with_viewport(this.image);

        // add the scrolledwindow to the window
        this.window.add(this.scrolledWindow);
        this.window.show_all();
    }
});

// Run the application
let app = new ScrolledWindowExample();
app.application.run (ARGV);
