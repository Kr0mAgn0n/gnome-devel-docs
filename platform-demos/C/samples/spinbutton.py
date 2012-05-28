from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="SpinButton Example", application=app)
        self.set_default_size(210, 70)
        self.set_border_width(5)

        # an adjustment (initial value, min value, max value,
        # step increment - press cursor keys or +/- buttons to see!,
        # page increment - not used here,
        # page size - not used here)
        ad = Gtk.Adjustment(0, 0, 100, 1, 10, 0)

        # a spin button for integers (digits=0)
        spin = Gtk.SpinButton(adjustment=ad, climb_rate=1, digits=0)
        # as wide as possible
        spin.set_hexpand(True)

        spin.connect("value-changed", self.spin_selected)

        # a label
        label = Gtk.Label()
        label.set_text("Choose a number")

        # a grid to attach the widgets
        grid = Gtk.Grid()
        grid.attach(spin, 1, 1, 1, 1)
        grid.attach(label, 1, 2, 2, 1)

        self.add(grid)

        self.label = label
        self.spin = spin

    # the signal of the spinbutton is signaled to the label the text of which is changed
    def spin_selected(self, event):
        self.label.set_text("The number you selected is " + str(self.spin.get_value_as_int()) + ".")
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
