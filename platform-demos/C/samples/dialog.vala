void on_response (int response_id) {

    /*To see the int value of the ResponseType*/
    print ("response is %d\n", response_id);
    
    Gtk.main_quit ();
}

int main (string[] args) {

    Gtk.init (ref args);

    var dialog = new Gtk.Dialog.with_buttons ("A Gtk+ Dialog", null, 0, Gtk.Stock.OK, Gtk.ResponseType.OK, null);
    var content_area = dialog.get_content_area () as Gtk.Container; //TODO: explain this
    var label = new Gtk.Label ("This demonstrates a dialog with a label");
    
    content_area.add (label);
    dialog.response.connect (on_response);
    dialog.show_all ();

    Gtk.main ();
    return 0;
}
