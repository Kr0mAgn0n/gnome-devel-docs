from gi.repository import GLib
from gi.repository import Gtk
from gi.repository import Gio
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="RadioButton Example", application=app)
        self.set_default_size(250, 100)
        self.set_border_width(20)

        # a new checkbutton with a label, connected with the callback
        button1 = Gtk.RadioButton(label="Button 1")
        button1.connect("toggled", self.toggled_cb)

        # another way to create a button - in the same group as button1
        button2 = Gtk.RadioButton.new_from_widget(button1)
        button2.set_label("Button 2")
        button2.connect("toggled", self.toggled_cb)
        button2.set_active(False)

        # yet another way
        button3 = Gtk.RadioButton.new_with_label_from_widget(button1, "Button 3")
        button3.connect("toggled", self.toggled_cb)
        button3.set_active(False)

        # DO NOT use new_with_label, it gives a segmentation fault!

        # a grid to place the buttons
        grid = Gtk.Grid.new()
        grid.attach(button1, 0, 0, 1, 1);
        grid.attach(button2, 0, 1, 1, 1);
        grid.attach(button3, 0, 2, 1, 1);

        self.add(grid)

    def toggled_cb(self, button):
        state = "unknown"
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print button.get_label() + " was turned " + state + "\n"

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
