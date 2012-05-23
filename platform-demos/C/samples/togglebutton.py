from gi.repository import GLib
from gi.repository import Gtk
from gi.repository import Gio
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="ToggleButton Example", application=app)
        self.set_default_size(300, 300)
        self.set_border_width(30)

        # a spinner animation, with extra horizontal and vertical space
        spinner = Gtk.Spinner()
        spinner.set_hexpand(True)
        spinner.set_vexpand(True)
        # we keep a reference to the spinner inside the class (we need it later)
        self.spinner = spinner

        # a togglebutton
        button = Gtk.ToggleButton.new_with_label("Start/Stop")
        button.connect("toggled", self.toggled_cb)

        # a grid to allocate the widgets
        grid = Gtk.Grid()
        grid.set_row_homogeneous(False);
        grid.set_row_spacing(15);
        grid.attach(spinner, 0, 0, 1, 1);
        grid.attach(button, 0, 1, 1, 1);

        self.add(grid)

    # the button operates on the window
    def toggled_cb(self, button):
        if button.get_active():
            self.spinner.start()
        else:
            self.spinner.stop()

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
