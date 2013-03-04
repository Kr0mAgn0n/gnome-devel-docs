from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    # a window
    def __init__(self, app):
        Gtk.Window.__init__(self, title="CheckButton Example", application=app)
        self.set_default_size(300, 100)
        self.set_border_width(10)

        # a new checkbutton
        button = Gtk.CheckButton()
        #  with a label
        button.set_label("Show Title")
        # connect the signal "toggled" emitted by the checkbutton
        # with the callback function toggled_cb
        button.connect("toggled", self.toggled_cb)
        # by default, the checkbutton is active
        button.set_active(True)

        # add the checkbutton to the window
        self.add(button)

    # callback function
    def toggled_cb(self, button):
        # if the togglebutton is active, set the title of the window
        # as "Checkbutton Example"
        if button.get_active():
            self.set_title("CheckButton Example")
        # else, set it as "" (empty string)
        else:
            self.set_title("")

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
