from gi.repository import Gtk
from gi.repository import Gdk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="ColorButton", application=app)
        self.set_default_size(150, 50)
        self.set_border_width(10)

        # a colorbutton (which opens a dialogue window in
        # which we choose a color)
        button = Gtk.ColorButton()
        # with a default color (blue, in this instance)
        # if not chosen it will be black
        color = Gdk.RGBA()
        color.red = 0.0
        color.green = 0.0
        color.blue = 1.0
        color.alpha = 0.5
        button.set_rgba(color)

        # choosing a color in the dialogue window emits a signal
        button.connect("color-set", self.on_color_chosen)
        self.button = button

        # a label
        label = Gtk.Label()
        label.set_text("Click to choose a color")

        # a grid to attach button and label
        grid = Gtk.Grid()
        grid.attach(button, 1, 1, 2, 1)
        grid.attach(label, 1, 2, 2, 1)
        self.add(grid)

    # if a new color is chosen, we print it as rgb(r,g,b) in the terminal
    def on_color_chosen(self, user_data):
        print "You chose another color: " + self.button.get_rgba().to_string()

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.example.colorbutton")

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup (self):
        Gtk.Application.do_startup (self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
