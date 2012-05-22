from gi.repository import GLib
from gi.repository import Gtk
from gi.repository import Gio
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="CheckButton Example", application=app)
        self.set_default_size(300, 100)
        self.set_border_width(10)
        
        # a new checkbutton with a label, connected with the callback
        button = Gtk.CheckButton.new_with_label("Show Title")
        button.connect("toggled", self.toggled_cb)
        # default: is active
        button.set_active(True)
        
        self.add(button)

    # the button operates on the window
    def toggled_cb(self, button):
        if button.get_active():
            self.set_title("CheckButton Example")
        else:
            self.set_title("")
            
class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.gtk.example.grid")
        
    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
