from gi.repository import Gtk

class ButtonWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="GNOME Button")
        
        self.set_default_size(250, 50)
        self.set_position(Gtk.WindowPosition.CENTER)
        
        self.button = Gtk.Button(label="Click me")
        self.button.connect("clicked", self.button_clicked)
        self.add(self.button)
    
    def button_clicked(self, widget):
        print "\"Click me\" button was clicked"
        
win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
