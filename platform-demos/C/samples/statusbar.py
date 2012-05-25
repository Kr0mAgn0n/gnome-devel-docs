from gi.repository import Gtk
from gi.repository import Gdk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="StatusBar Example", application=app)
        self.set_default_size(200, 100)

        # a label
        label = Gtk.Label(label="Press any key or ")

        # a button
        button = Gtk.Button(label="click me.")
        # connected to a callback
        button.connect("clicked", self.button_clicked_cb)

        # the statusbar (the context_id is not shown in the UI but it is needed)
        statusbar = Gtk.Statusbar()
        context_id = statusbar.get_context_id("example")
        # pushed a new message onto the statusbar's stack
        statusbar.push(context_id, "Waiting for you to do something...")

        # a grid to attach the widgets
        grid = Gtk.Grid()
        grid.set_column_spacing(5)
        grid.set_column_homogeneous(True)
        grid.set_row_homogeneous(True)
        grid.attach(label, 1, 1, 1, 1)
        grid.attach_next_to(button, label, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach(statusbar, 1, 2, 2, 1)

        self.add(grid)

        self.bar = statusbar
        self.id = context_id

    # if the button is clicked the event is signaled to the statusbar
    # onto which we push a new status
    def button_clicked_cb(self, button):
        self.bar.push(self.id, "You clicked the button.")

    # any signal from the keyboard is signaled to the statusbar
    # onto which we push a new status
    def do_key_press_event(self, event):
        self.bar.push(self.id, Gdk.keyval_name(event.keyval) + " key was pressed.")
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
