from gi.repository import GLib
from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="GNOME LinkButton", application=app)
        button = Gtk.LinkButton("http://live.gnome.org")
        button.set_label("Link to GNOME live!")
        self.add(button)

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.gtk.example.grid")

    def do_activate(self):
        win = MyWindow(self)
        win.set_default_size(250, 50)
        win.set_position(Gtk.WindowPosition.CENTER)
        win.show_all()

    def do_startup (self):
        Gtk.Application.do_startup (self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
