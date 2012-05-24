from gi.repository import GLib
from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Switch Example", application=app)
        self.set_default_size(300, 100)
        self.set_border_width(10)

        # a switch, turned on by default, sends the signal notify::active
        switcher = Gtk.Switch()
        switcher.set_active(True)
        switcher.connect("notify::active", self.activate_cb)

        # a label
        label = Gtk.Label()
        label.set_text("Title")

        # a grid to allocate the widgets
        grid = Gtk.Grid()
        grid.set_column_spacing (10);
        grid.attach (label, 0, 0, 1, 1);
        grid.attach (switcher, 1, 0, 1, 1);

        self.add(grid)

    # the switch operates on the title of the window. Since the signal is
    # notify::active we need the argument 'active'
    def activate_cb(self, button, active):
        if button.get_active():
            self.set_title("Switch Example")
        else:
            self.set_title("")

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.example.spinner")

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
