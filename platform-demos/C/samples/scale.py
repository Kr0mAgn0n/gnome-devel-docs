from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Scale Example", application=app)
        self.set_default_size(400, 300)
        self.set_border_width(5)

        # two adjustments (initial value, min value, max value,
        # step increment - press cursor keys to see!,
        # page increment - click around the handle to see!,
        # page size - not used here)
        ad1 = Gtk.Adjustment(0, 0, 100, 5, 10, 0)
        ad2 = Gtk.Adjustment(50, 0, 100, 5, 10, 0)

        # an horizontal scale
        h_scale = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, adjustment=ad1)
        h_scale.set_digits(0)
        # that can expand horizontally if there is space in the grid (see below)
        h_scale.set_hexpand(True)
        # that is aligned at the top of the space allowed in the grid (see below)
        h_scale.set_valign(Gtk.Align.START)

        h_scale.connect("value-changed", self.scale_moved)

        # a vertical scale
        v_scale = Gtk.Scale(orientation=Gtk.Orientation.VERTICAL, adjustment=ad2)
        # that can expand vertically if there is space in the grid (see below)
        v_scale.set_vexpand(True)

        v_scale.connect("value-changed", self.scale_moved)

        # a label
        label = Gtk.Label()
        label.set_text("Move the scale handles...")

        # a grid to attach the widgets
        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_column_homogeneous(True)
        grid.attach(h_scale, 1, 1, 1, 1)
        grid.attach_next_to(v_scale, h_scale, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach(label, 1, 2, 2, 1)

        self.add(grid)

        self.label = label
        self.scale1 = h_scale
        self.scale2 = v_scale

    # any signal from the scales is signaled to the label the text of which is changed
    def scale_moved(self, event):
        self.label.set_text("Horizontal scale is " + str(int(self.scale1.get_value())) +
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
