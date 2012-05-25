from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Scale Example", application=app)
        self.set_default_size(400, 300)

        # two adjustments (initial value, min value, max value,
        # step increment - press cursor keys to see!,
        # page increment - click around the handle to see!,
        # page size - not used here)
        ad1 = Gtk.Adjustment(0, 0, 100, 5, 10, 0)
        ad2 = Gtk.Adjustment(50, 0, 100, 5, 10, 0)

        # an horizontal scale
        h_scale = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=ad1)
        h_scale.set_digits(0)

        h_scale.connect("value-changed", self.scale_moved)

        # a vertical scale
        v_scale = Gtk.VScale(adjustment=ad2)

        v_scale.connect("value-changed", self.scale_moved)

        # the statusbar (the context_id is not shown in the UI but it is needed)
        statusbar = Gtk.Statusbar()
        context_id = statusbar.get_context_id("example")
        # pushed a new message onto the statusbar's stack
        statusbar.push(context_id, "Move around the scales...")

        # a grid to attach the widgets
        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)
        grid.attach(h_scale, 1, 1, 1, 1)
        grid.attach_next_to(v_scale, h_scale, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach(statusbar, 1, 2, 2, 1)

        self.add(grid)

        self.bar = statusbar
        self.id = context_id
        self.scale1 = h_scale
        self.scale2 = v_scale

    # any signal from the scales is signaled to the statusbar
    # onto which we push a new status
    def scale_moved(self, event):
        self.bar.push(self.id,
                      "Horizontal scale is " + str(int(self.scale1.get_value())) +
                      "; vertical scale is " + str(self.scale2.get_value()) + ".")
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
