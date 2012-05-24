from gi.repository import GLib
from gi.repository import Gtk
from gi.repository import Gdk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Spinner Example", application=app)
        self.set_default_size(200, 200)
        self.set_border_width(30)

        # a spinner
        spinner = Gtk.Spinner()
        spinner.start()

        self.spinner = spinner

        self.add(spinner)

    # a signal from the keyboard (space) controls if the spinner stops/starts
    def do_key_press_event(self, event):
        keyname = Gdk.keyval_name(event.keyval)
        if keyname == "space":
            if self.spinner.get_property("active"):
                self.spinner.stop()
            else:
                self.spinner.start()
        return True

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
