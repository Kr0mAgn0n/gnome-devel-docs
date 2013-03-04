from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, application=app)
        self.set_title("Welcome to GNOME")

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.gnome.ApplicationWindowExample")

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

# create the application
app = MyApplication()
# run the application, which returns the value exit_status
exit_status = app.run(sys.argv)
# terminate the program using exit_status
sys.exit(exit_status)
