//!/usr/bin/gjs

const Gtk = imports.gi.Gtk;
const Lang = imports.lang;

const FontChooserWidgetExample = new Lang.Class ({
    Name: 'Font Chooser Widget Example',

    // Create the application itthis
    _init: function () {
        this.application = new Gtk.Application({ application_id: 'org.example.fontchooserwidget' });

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
                                                    title: "FontChooserWidget",
                                                    default_width: 200,
                                                    default_height: 200,
                                                    border_width: 10 });

        this.fontChooser = new Gtk.FontChooserWidget();
        // a default font
        this.fontChooser.set_font("Sans");
        // a text to preview the font
        this.fontChooser.set_preview_text("This is an example of preview text!");

        // connect signal from the font chooser to the callback function
        this.fontChooser.connect("notify::font", Lang.bind(this, this._fontCb));

        // add the font chooser to the window
        this.window.add(this.fontChooser);
        this.window.show_all();
   },

     // callback function:
     _fontCb: function() {
        // print in the terminal
        print("You chose the font " + this.fontChooser.get_font());
    }
});

// Run the application
let app = new FontChooserWidgetExample();
app.application.run (ARGV);
