from gi.repository import GLib
from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="What is your name?", application=app)
        self.set_default_size(300, 100)
        self.set_border_width(10)

        name_box = Gtk.Entry()
        name_box.connect("activate", self.cb_activate)

        self.add(name_box)

    # the button operates on the window
    def cb_activate(self, entry):
		name = entry.get_text()
		print "\nHello " + name + "!\n"

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.example.MyApplication")

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
