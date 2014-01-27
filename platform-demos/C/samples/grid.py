from gi.repository import Gtk
import sys


class MyWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Grid Example", application=app)

        # three labels
        label_top_left = Gtk.Label(label="This is Top Left")
        label_top_right = Gtk.Label(label="This is Top Right")
        label_bottom = Gtk.Label(label="This is Bottom")

        # a grid
        grid = Gtk.Grid()

        # some space between the columns of the grid
        grid.set_column_spacing(20)

        # in the grid:
        # attach the first label in the top left corner
        grid.attach(label_top_left, 0, 0, 1, 1)
        # attach the second label
        grid.attach(label_top_right, 1, 0, 1, 1)
        # attach the third label below the first label
        grid.attach_next_to(
            label_bottom, label_top_left, Gtk.PositionType.BOTTOM, 2, 1)

        # add the grid to the window
        self.add(grid)


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
