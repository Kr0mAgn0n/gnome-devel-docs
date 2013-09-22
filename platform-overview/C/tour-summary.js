
#!/usr/bin/gjs

const Lang = imports.lang;
const Gtk = imports.gi.Gtk;

const HelloWorld = new Lang.Class({
    Name: 'HelloWorld',

    _init: function() {
        this.application = new Gtk.Application();
        this.application.connect('activate', Lang.bind(this, this._onActivate));
        this.application.connect('startup', Lang.bind(this, this._onStartup));
    },

    _onActivate: function(){
        this._window.show_all();
    },

    _onStartup: function() {
        let builder = new Gtk.Builder();
        builder.add_from_file('helloworld.glade');
        this._window = builder.get_object('window1');
        this.application.add_window(this._window);
    }
});

let app = new HelloWorld();
app.application.run(ARGV);
