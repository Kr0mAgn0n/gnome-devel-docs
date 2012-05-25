from gi.repository import GLib
from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="ProgressBar Example", application=app)
        self.set_default_size(220, 20)

        # a progressbar
        progress_bar = Gtk.ProgressBar()
        self.add(progress_bar)

        self.bar = progress_bar

        # the method pulse is called each 100 milliseconds
        # and self.source_id is set to be the ID of the event source
        # (the bar moves)
        self.source_id = GLib.timeout_add(100, self.pulse)


    # any signal from the keyboard controls if the progressbar stops/starts
    def do_key_press_event(self, event):
        # if the bar has been stopped (and source_id == 0 - see below),
        # turn it back on
        if (self.source_id == 0):
            self.source_id = GLib.timeout_add(100, self.pulse)
        # if the bar is moving, remove the source with the ID of source_id
        # from the main context (stop the bar) and set the source_id to 0
        else:
            GLib.source_remove(self.source_id)
            self.source_id = 0
        return True

    # the progressbar is in "activity mode"
    def pulse(self):
        self.bar.pulse()
        return True

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
