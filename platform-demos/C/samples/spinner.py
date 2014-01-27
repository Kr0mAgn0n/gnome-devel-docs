from gi.repository import Gtk
from gi.repository import Gdk
import sys


class MyWindow(Gtk.ApplicationWindow):
    # a window

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Spinner Example", application=app)
        self.set_default_size(200, 200)
        self.set_border_width(30)

        # a spinner
        self.spinner = Gtk.Spinner()
        # that by default spins
        self.spinner.start()
        # add the spinner to the window
        self.add(self.spinner)

    # event handler
    # a signal from the keyboard (space) controls if the spinner stops/starts
    def do_key_press_event(self, event):
        # keyname is the symbolic name of the key value given by the event
        keyname = Gdk.keyval_name(event.keyval)
        # if it is "space"
        if keyname == "space":
            # and the spinner is active
            if self.spinner.get_property("active"):
                # stop the spinner
                self.spinner.stop()
            # if the spinner is not active
            else:
                # start it again
                self.spinner.start()
        # stop the signal emission
        return True


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
