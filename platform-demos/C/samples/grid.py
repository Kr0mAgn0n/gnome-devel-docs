from gi.repository import Gtk
import sys

class GridWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Grid Example", application=app)

        grid = Gtk.Grid()
        button = Gtk.Button(label="Button")
  
        self.add(grid)
        grid.attach(button, 1, 1, 1, 1)
        self.progress_bar = Gtk.ProgressBar()
        grid.attach_next_to(self.progress_bar, button, 3, 1, 1)

        button.connect("clicked", self.button_clicked_cb)

    def button_clicked_cb(self, widget):
        self.progress_bar.pulse()

class GridApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.gtk.example.grid")

    def do_activate(self):
        win = GridWindow(self)
        win.show_all()

app = GridApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
