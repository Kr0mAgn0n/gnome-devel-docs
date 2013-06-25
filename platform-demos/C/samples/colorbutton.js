#!/usr/bin/gjs

const Gdk = imports.gi.Gdk;
const GObject = imports.gi.GObject;
const Gtk = imports.gi.Gtk;
const Lang = imports.lang;

const ColorbuttonExample = new Lang.Class ({
    Name: 'Colorbutton Example',

    // Create the application itself
    _init: function () {
        this.application = new Gtk.Application ({ application_id: 'org.example.jscolorbutton' });

        // Connect 'activate' and 'startup' signals to the callback functions
        this.application.connect('activate', Lang.bind(this, this._onActivate));
        this.application.connect('startup', Lang.bind(this, this._onStartup));
    },

    // Callback function for 'activate' signal presents windows when active
    _onActivate: function() {
        this.window.present();
    },

    // Callback function for 'startup' signal builds the UI
    _onStartup: function () {
        this._buildUI ();
    },

    // Build the application's UI
    _buildUI: function () {

        // Create the application window
        this.window = new Gtk.ApplicationWindow ({ application: this.application,
                                                   window_position: Gtk.WindowPosition.CENTER,
                                                   title: "ColorButton",
                                                   default_width: 150,
                                                   default_height: 50,
                                                   border_width: 10 });

        this.button = new Gtk.ColorButton();
        this.color = new Gdk.RGBA();
        this.color.red = 0.0;
        this.color.green = 0.0;
        this.color.blue = 1.0;
        this.color.alpha = 0.5;
        this.button.set_rgba(this.color);
        this.button.connect("color-set", Lang.bind(this, this.onColorChosen));
        this.label = new Gtk.Label();
        this.label.set_text("Click to choose a color");

        let grid = new Gtk.Grid();
        grid.attach(this.button, 0, 0, 2, 1);
        grid.attach(this.label, 0, 1, 2, 1);
        this.window.add(grid);
        this.window.show_all();
    },

    onColorChosen: function() {
    let colorName = this.color.to_string();
    this.label.set_text("You chose the color " + colorName);
    }
});

// Run the application
let app = new ColorbuttonExample ();
app.application.run (ARGV);
