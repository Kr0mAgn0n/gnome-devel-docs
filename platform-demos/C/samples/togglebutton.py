from gi.repository import Gtk
import sys


class MyWindow(Gtk.ApplicationWindow):
    # a window

    def __init__(self, app):
        Gtk.Window.__init__(
            self, title="ToggleButton Example", application=app)
        self.set_default_size(300, 300)
        self.set_border_width(30)

        # a spinner animation
        self.spinner = Gtk.Spinner()
        # with extra horizontal space
        self.spinner.set_hexpand(True)
        # with extra vertical space
        self.spinner.set_vexpand(True)

        # a togglebutton
        button = Gtk.ToggleButton.new_with_label("Start/Stop")
        # connect the signal "toggled" emitted by the togglebutton
        # when its state is changed to the callback function toggled_cb
        button.connect("toggled", self.toggled_cb)

        # a grid to allocate the widgets
        grid = Gtk.Grid()
        grid.set_row_homogeneous(False)
        grid.set_row_spacing(15)
        grid.attach(self.spinner, 0, 0, 1, 1)
        grid.attach(button, 0, 1, 1, 1)

        # add the grid to the window
        self.add(grid)

    # callback function for the signal "toggled"
    def toggled_cb(self, button):
        # if the togglebutton is active, start the spinner
        if button.get_active():
            self.spinner.start()
        # else, stop it
        else:
            self.spinner.stop()


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
