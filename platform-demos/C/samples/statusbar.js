#!/usr/bin/gjs

const Gio = imports.gi.Gio;
const Gtk = imports.gi.Gtk;
const Lang = imports.lang;

const StatusbarExample = new Lang.Class({
    Name: 'Statusbar Example',

    // Create the application itself
    _init: function() {
        this.application = new Gtk.Application({
            application_id: 'org.example.jsstatusbar',
            flags: Gio.ApplicationFlags.FLAGS_NONE
        });

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
            default_height: 120,
            default_width: 300,
            title: "Button Clicker"});

        // Create a paned interface
        this._panes = new Gtk.Paned ({
            orientation: Gtk.Orientation.VERTICAL });

        // Create the main button
        this._clickMe = new Gtk.Button ({
            label: "Click Me!" });
        this._clickMe.connect ("clicked", Lang.bind (this, this._clicked));

        // Create the back button
        this._backButton = new Gtk.Button ({
            label: "gtk-go-back",
            use_stock: true });
        this._backButton.connect ("clicked", Lang.bind (this, this._back));

        // Create the clear button
        this._clearButton = new Gtk.Button ({
            label: "gtk-clear",
            use_stock: true });
        this._clearButton.connect ("clicked", Lang.bind (this, this._clear));

        // Put the buttons in a grid
        this._grid = new Gtk.Grid ({
            halign: Gtk.Align.CENTER,
            valign: Gtk.Align.CENTER });
        this._grid.attach (this._backButton, 0, 0, 1, 1);
        this._grid.attach_next_to (this._clickMe, this._backButton, Gtk.PositionType.RIGHT, 1, 1);
        this._grid.attach_next_to (this._clearButton, this._clickMe, Gtk.PositionType.RIGHT, 1, 1);

        // Put the grid in a large frame that fills most of the window
        this._topFrame = new Gtk.Frame ({
            border_width: 20,
            height_request: 90,
            width_request: 300});
        this._topFrame.add (this._grid);

        // Create the statusbar
        this._statusbar = new Gtk.Statusbar();

        // Keep track of the number of times the statusbar has been clicked
        this.Clicks = 0;
        this.ContextID = this._statusbar.get_context_id ("Number of Clicks");

        // Give the statusbar an initial message
        this._statusbar.push (this.ContextID, "Number of clicks: " + this.Clicks);

        // Put the statusbar in its own frame at the bottom
        this._barFrame = new Gtk.Frame ({
            height_request: 30 });
        this._barFrame.add (this._statusbar);

        // Assemble the frames into the paned interface
        this._panes.pack1 (this._topFrame, true, false);
        this._panes.pack2 (this._barFrame, false, false);

        // Put the panes into the window
        this._window.add (this._panes);

        // Show the window and all child widgets
        this._window.show_all();
    },



    _clicked: function() {

        // Increment the number of clicks by 1
        this.Clicks++;

        // Update the statusbar with the new number of clicks
        this._statusbar.push (this.ContextID, "Number of clicks: " + this.Clicks);

    },



    _back: function () {

        // If there have been any clicks, decrement by 1 and remove last statusbar update
        if (this.Clicks > 0 ) {
            this.Clicks--;
            this._statusbar.pop (this.ContextID);
        };

    },



    _clear: function () {

        // Reset the number of clicks
        this.Clicks = 0;

        // Wipe out all the messages pushed to the statusbar
        this._statusbar.remove_all (this.ContextID);

        // Reset the statusbar's message
        this._statusbar.push (this.ContextID, "Number of clicks: " + this.Clicks);

    }

});

// Run the application
let app = new StatusbarExample ();
app.application.run (ARGV);
