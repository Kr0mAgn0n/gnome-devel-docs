from gi.repository import Gtk
import sys


class MyWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Separator Example", application=app)

        # three labels
        label1 = Gtk.Label()
        label1.set_text("Below, a horizontal separator.")

        label2 = Gtk.Label()
        label2.set_text("On the right, a vertical separator.")

        label3 = Gtk.Label()
        label3.set_text("On the left, a vertical separator.")

        # a horizontal separator
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        # a vertical separator
        vseparator = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)

        # a grid to attach labels and separators
        grid = Gtk.Grid()
        grid.attach(label1, 0, 0, 3, 1)
        grid.attach(hseparator, 0, 1, 3, 1)
        grid.attach(label2, 0, 2, 1, 1)
        grid.attach(vseparator, 1, 2, 1, 1)
        grid.attach(label3, 2, 2, 1, 1)
        grid.set_column_homogeneous(True)
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
