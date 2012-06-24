#!/usr/bin/gjs

const Gio = imports.gi.Gio;
const Gtk = imports.gi.Gtk;
const Lang = imports.lang;

const SpinButtonExample = new Lang.Class({
    Name: 'SpinButton Example',

    // Create the application itself
    _init: function() {
        this.application = new Gtk.Application({
            application_id: 'org.example.jsspinbutton'
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
            border_width: 20,
            title: "Kitten Feeder"});

        // Create the first spinbutton using a function
        this._kittens = Gtk.SpinButton.new_with_range (1, 9001, 1);
        this._kittens.connect ("value-changed", Lang.bind (this, this._newValue));

        // Create an adjustment to use for the second spinbutton
        this._adjustment = new Gtk.Adjustment ({
            value: 1,
            lower: 0,
            upper: 9001,
            step_increment: 1,
            page_increment: 10 });

        // Create the second spinbutton
        this._tuna = new Gtk.SpinButton ({ adjustment: this._adjustment });
        this._tuna.connect ("value-changed", Lang.bind (this, this._newValue));

        // this._tuna.set_digits (1);
        // this._tuna.set_wrap (true);

        // Create the text labels to go with the spinbuttons
        this._startLabel = new Gtk.Label ({ label: "There are " });
        this._kittenLabel = new Gtk.Label ({ label: " kitten(s), and "});
        this._tunaLabel = new Gtk.Label ({ label: " can(s) of tuna."});
        this.perKitten = Math.floor((this._tuna.get_value() / this._kittens.get_value()));
        this._lastLabel = new Gtk.Label ({
            label: "That's " + this.perKitten + " can(s) of tuna per kitten." });

        // Create a grid to put the spinbuttons and their labels in
        this._spinGrid = new Gtk.Grid ({
            halign: Gtk.Align.CENTER,
            valign: Gtk.Align.CENTER,
            margin_bottom: 20 });

        // Attach everything to the grid
        this._spinGrid.attach (this._startLabel, 0, 0, 1, 1);
        this._spinGrid.attach (this._kittens, 1, 0, 1, 1);
        this._spinGrid.attach (this._kittenLabel, 2, 0, 1, 1);
        this._spinGrid.attach (this._tuna, 3, 0, 1, 1);
        this._spinGrid.attach (this._tunaLabel, 4, 0, 1, 1);

        // Create a main grid to hold it and the last label
        this._mainGrid = new Gtk.Grid ({
            halign: Gtk.Align.CENTER,
            valign: Gtk.Align.CENTER });

        // Attach the smaller grid and the last label to the main grid
        this._mainGrid.attach (this._spinGrid, 0, 0, 1, 1);
        this._mainGrid.attach (this._lastLabel, 0, 1, 1, 1);

        // Add the main grid to the window
        this._window.add (this._mainGrid);

        // Show the window and all child widgets
        this._window.show_all();
    },



    _newValue: function () {

        // Update the label which shows how many cans there are per kitten
        this.perKitten = Math.floor((this._tuna.get_value() / this._kittens.get_value()))
        this._lastLabel.set_label ("That's " + this.perKitten + " can(s) of tuna per kitten.");

    }

});

// Run the application
let app = new SpinButtonExample ();
app.application.run (ARGV);
