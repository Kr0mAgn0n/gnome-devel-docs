from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="SpinButton Example", application=app)
        self.set_default_size(200, 150)

        # an adjustment (initial value, min value, max value,
        # step increment - press cursor keys or +/- buttons to see!,
        # page increment - not used here,
        # page size - not used here)
        ad = Gtk.Adjustment(0, 0, 100, 1, 10, 0)

        # a spin button for integers (digits=0)
        spin = Gtk.SpinButton(adjustment=ad, climb_rate=1, digits=0)

        spin.connect("value-changed", self.spin_selected)

        # the statusbar (the context_id is not shown in the UI but it is needed)
        statusbar = Gtk.Statusbar()
        context_id = statusbar.get_context_id("example")
        # a new message onto the statusbar's stack
        statusbar.push(context_id, "Give me a number...")

        # a grid to attach the widgets
        grid = Gtk.Grid()
        grid.set_row_homogeneous(True)
        grid.attach(spin, 1, 1, 1, 1)
        grid.attach(statusbar, 1, 2, 2, 1)

        self.add(grid)

        self.bar = statusbar
        self.id = context_id
        self.spin = spin

    # the signal of the spinbutton is signaled to the statusbar
    # onto which we push a new status
    def spin_selected(self, event):
        self.bar.push(self.id,
                      "The number you selected is " + str(self.spin.get_value_as_int()) + ".")
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
