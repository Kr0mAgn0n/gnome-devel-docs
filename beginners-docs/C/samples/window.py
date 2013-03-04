from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        # set the title
        self.set_title("Welcome to GNOME")
        # set a default size: width of 200 and default height
        self.set_default_size(200, -1)
        # set a default position: center of the screen
        self.set_position(Gtk.WindowPosition.CENTER)
        # show the window
        self.show_all()

# create an instance of MyWindow
win = MyWindow()
# close the GTK+ processing loop when the window is closed
win.connect("delete-event", Gtk.main_quit)
# start the GTK+ processing loop
Gtk.main()
