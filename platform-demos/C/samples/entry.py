from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="What is your name?", application=app)
        self.set_default_size(300, 100)
        self.set_border_width(10)

        # a single line entry
        name_box = Gtk.Entry()
        # emits a signal when the Enter key is pressed, connected to the
        # callback function cb_activate
        name_box.connect("activate", self.cb_activate)

        # add the Gtk.Entry to the window
        self.add(name_box)

    # the content of the entry is used to write in the terminal
    def cb_activate(self, entry):
        # retrieve the content of the widget
        name = entry.get_text()
        # print it in a nice form in the terminal
        print "Hello " + name + "!"

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
