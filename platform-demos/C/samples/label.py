from gi.repository import GLib
from gi.repository import Gtk
from gi.repository import Gio
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Welcome to GNOME", application=app)
        
class MyLabel(Gtk.Label):
    def __init__(self):
        Gtk.Label.__init__(self)
        self.set_text("Hello GNOME!")
        
class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.gtk.example.grid")
        
    def do_activate(self):
        win = MyWindow(self)
        win.set_default_size(200, 100)
        win.set_position(Gtk.WindowPosition.CENTER)
        win.add(MyLabel())
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
