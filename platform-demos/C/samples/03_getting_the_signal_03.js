#!/usr/bin/gjs

const Gtk = imports.gi.Gtk;
const Lang = imports.lang;

// We start out with 0 cookies
var cookies = 0;

const GettingTheSignal = new Lang.Class({
    Name: 'Getting the Signal',

    // Create the application itself
    _init: function() {
        this.application = new Gtk.Application();

        // Connect 'activate' and 'startup' signals to the callback functions
        this.application.connect('activate', Lang.bind(this, this._onActivate));
        this.application.connect('startup', Lang.bind(this, this._onStartup));
    },

    // Callback function for 'activate' signal presents window when active
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
        this._window = new Gtk.ApplicationWindow({
            application: this.application,
            window_position: Gtk.WindowPosition.CENTER,
            default_height: 200,
            default_width: 400,
            border_width: 20,
            title: "Choose the one that says 'cookie'!"});

        // Create the radio buttons
        this._cookieButton = new Gtk.RadioButton ({ label: "Cookie" });
        this._notCookieOne = new Gtk.RadioButton ({ label: "Not cookie",
            group: this._cookieButton });
        this._notCookieTwo = new Gtk.RadioButton ({ label: "Not cookie",
            group: this._cookieButton });

        // Arrange the radio buttons in their own grid
        this._radioGrid = new Gtk.Grid ();
        this._radioGrid.attach (this._notCookieOne, 0, 0, 1, 1);
        this._radioGrid.attach (this._cookieButton, 0, 1, 1, 1);
        this._radioGrid.attach (this._notCookieTwo, 0, 2, 1, 1);

        // Set the button that will be at the top to be active by default
        this._notCookieOne.set_active (true);

        // Create the cookie button
        this._cookieButton = new Gtk.Button ({
            label: "Get a cookie" });

        // Connect the cookie button to the function that handles clicking it
        this._cookieButton.connect ('clicked', Lang.bind (this, this._getACookie));

        // Create the label
        this._cookieLabel = new Gtk.Label ({
            label: "Number of cookies: " + cookies });

        // Create a grid to arrange everything inside
        this._grid = new Gtk.Grid ({
            halign: Gtk.Align.CENTER,
            valign: Gtk.Align.CENTER,
            row_spacing: 20 });

        // Put everything inside the grid
        this._grid.attach (this._radioGrid, 0, 0, 1, 1);
        this._grid.attach (this._cookieButton, 0, 1, 1, 1);
        this._grid.attach (this._cookieLabel, 0, 2, 1, 1);

        // Add the grid to the window
        this._window.add (this._grid);

        // Show the window and all child widgets
        this._window.show_all();

    },



    _getACookie: function() {

        // Did you select "cookie" instead of "not cookie"?
        if (this._cookieButton.get_active()) {

            // Increase the number of cookies by 1 and update the label
            cookies++;
            this._cookieLabel.set_label ("Number of cookies: " + cookies);

        }

    }

});

// Run the application
let app = new GettingTheSignal ();
app.application.run (ARGV);
