from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, application=app)
        self.set_title("Welcome to GNOME") 
        self.set_default_size(300, 300)

class MyImage(Gtk.Image):
    def __init__(self):
        Gtk.Image.__init__(self)
        self.set_from_file("gnome-image.png")

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.gnome.ImageExample2")

    def do_activate(self):
        win = MyWindow(self)
        win.add(MyImage())
        win.show_all()
        
app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
