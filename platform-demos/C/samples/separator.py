from gi.repository import Gtk
import sys

class SeparatorsWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Separator Example", application=app)

        # three labels
        label1 = Gtk.Label()
        label1.set_text("Below, a horizontal separator.")

        label2 = Gtk.Label()
        label2.set_text("On the right, a vertical separator.")

        label3 = Gtk.Label()
        label3.set_text("On the left, a vertical separator.")

        # a horizontal and a vertical separator
        hseparator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        vseparator = Gtk.Separator(orientation=Gtk.Orientation.VERTICAL)

        # a grid to attach them
        grid = Gtk.Grid()
        grid.attach(label1, 1, 1, 3, 1)
        grid.attach(hseparator, 1, 2, 3, 1)
        grid.attach(label2, 1, 3, 1, 1)
        grid.attach(vseparator, 2, 3, 1, 1)
        grid.attach(label3, 3, 3, 1, 1)
        grid.set_column_homogeneous(True)
        self.add(grid)

class GridApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.gtk.example.separator")

    def do_activate(self):
	win = SeparatorsWindow(self)
	win.show_all()

app = GridApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
