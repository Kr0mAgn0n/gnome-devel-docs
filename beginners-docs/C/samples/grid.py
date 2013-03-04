from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Grid Example", application=app)
        self.set_border_width(5)

        label_top_left = Gtk.Label(label="This is Top Left")
        label_top_right = Gtk.Label(label="This is Top Right")
        label_bottom = Gtk.Label(label="This is Bottom")

        grid = Gtk.Grid()
        grid.set_column_spacing(20)

        grid.attach(label_top_left, 0, 0, 1, 1)
        grid.attach(label_top_right, 1, 0, 1, 1)
        grid.attach_next_to(label_bottom, label_top_left, Gtk.PositionType.BOTTOM, 2, 1)

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
