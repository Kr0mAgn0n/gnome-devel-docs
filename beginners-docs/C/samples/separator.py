from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Separator Example", application=app)

        label1 = Gtk.Label(label="Below, a horizontal separator.")
        label2 = Gtk.Label(label="On the right, a vertical separator.")
        label3 = Gtk.Label(label="On the left, a vertical separator.")

        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        vseparator = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)

        grid = Gtk.Grid()
        grid.attach(label1, 0, 0, 3, 1)
        grid.attach(hseparator, 0, 1, 3, 1)
        grid.attach(label2, 0, 2, 1, 1)
        grid.attach(vseparator, 1, 2, 1, 1)
        grid.attach(label3, 2, 2, 1, 1)
        grid.set_column_homogeneous(True)

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
