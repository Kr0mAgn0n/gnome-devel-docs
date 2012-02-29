const Gtk = imports.gi.Gtk;
const Lang = imports.lang;

function ImageViewer () {
  this._init ();
}

ImageViewer.prototype = {
  _init: function () {
    this.window = new Gtk.Window ({title: "Image Viewer Demo"});
    this.window.connect ("hide", Gtk.main_quit);

    var main_box = new Gtk.Box ({orientation: Gtk.Orientation.VERTICAL, spacing: 0});
    this.window.add (main_box);

    this.image = new Gtk.Image ();
    main_box.pack_start (this.image, true, true, 0);

    var open_button = new Gtk.Button ({label: "Open a picture..."});
    open_button.connect ("clicked", Lang.bind (this, this._openClicked));
    main_box.pack_start (open_button, false, false, 0);

    this.window.show_all ();
  },

  _openClicked: function () {
    var chooser = new Gtk.FileChooserDialog ({title: "Select an image",
                                              action: Gtk.FileChooserAction.OPEN,
                                              transient_for: this.window,
                                              modal: true});
    chooser.add_button (Gtk.STOCK_CANCEL, 0);
    chooser.add_button (Gtk.STOCK_OPEN, 1);
    chooser.set_default_response (1);
    
    var filter = new Gtk.FileFilter ();
    filter.add_pixbuf_formats ();
    chooser.filter = filter;

    if (chooser.run () == 1)
      this.image.file = chooser.get_filename ();

    chooser.destroy ();
  }
}

Gtk.init (null, null);

var iv = new ImageViewer ();

Gtk.main ();
