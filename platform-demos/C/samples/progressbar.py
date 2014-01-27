from gi.repository import GLib
from gi.repository import Gtk
import sys


class MyWindow(Gtk.ApplicationWindow):
    # a window

    def __init__(self, app):
        Gtk.Window.__init__(self, title="ProgressBar Example", application=app)
        self.set_default_size(220, 20)

        # a progressbar
        self.progress_bar = Gtk.ProgressBar()
        # add the progressbar to the window
        self.add(self.progress_bar)

        # the method self.pulse is called each 100 milliseconds
        # and self.source_id is set to be the ID of the event source
        # (i.e. the bar changes position every 100 milliseconds)
        self.source_id = GLib.timeout_add(100, self.pulse)

    # event handler
    # any signal from the keyboard controls if the progressbar stops/starts
    def do_key_press_event(self, event):
        # if the progressbar has been stopped (therefore source_id == 0 - see
        # "else" below), turn it back on
        if (self.source_id == 0):
            self.source_id = GLib.timeout_add(100, self.pulse)
        # if the bar is moving, remove the source with the ID of source_id
        # from the main context (stop the bar) and set the source_id to 0
        else:
            GLib.source_remove(self.source_id)
            self.source_id = 0
        # stop the signal emission
        return True

    # source function
    # the progressbar is in "activity mode" when this method is called
    def pulse(self):
        self.progress_bar.pulse()
        # call the function again
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
