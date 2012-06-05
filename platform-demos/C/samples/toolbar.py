from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Gio
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Toolbar Example", application=app)
        self.set_default_size(400, 200)

        # a grid to attach the toolbar created in the method create_toolbar (see below)
        grid = Gtk.Grid()
        toolbar = self.create_toolbar()
        toolbar.set_hexpand(True)
        toolbar.show()
        grid.attach(toolbar, 0, 0, 1, 1)
        self.add(grid)

        # create the actions that control the window and connect their signal to a
        # callback method (see below)
        undo_action = Gio.SimpleAction.new("undo", None)
        undo_action.connect("activate", self.undo_callback)
        self.add_action(undo_action)

        fullscreen_action = Gio.SimpleAction.new("fullscreen", None)
        fullscreen_action.connect("activate", self.fullscreen_callback)
        self.add_action(fullscreen_action)


    def create_toolbar(self):
        toolbar = Gtk.Toolbar()

        # set this as the primary toolbar of the application
        toolbar.get_style_context().add_class(Gtk.STYLE_CLASS_PRIMARY_TOOLBAR);

        # create a button with a stock image
        new_button = Gtk.ToolButton.new_from_stock(Gtk.STOCK_NEW)
        # label is shown
        new_button.set_is_important(True)
        # insert the button at position in the toolbar
        toolbar.insert(new_button, 0)
        # show the button
        new_button.show()
        # set the name of the action associated with the button.
        # The action controls the application (app)
        new_button.set_action_name("app.new")

        open_button = Gtk.ToolButton.new_from_stock(Gtk.STOCK_OPEN)
        open_button.set_is_important(True)
        toolbar.insert(open_button, 1)
        open_button.show()
        open_button.set_action_name("app.open")

        undo_button = Gtk.ToolButton.new_from_stock(Gtk.STOCK_UNDO)
        undo_button.set_is_important(True)
        toolbar.insert(undo_button, 2)
        undo_button.show()
        undo_button.set_action_name("win.undo")

        self.fullscreen_button = Gtk.ToolButton.new_from_stock(Gtk.STOCK_FULLSCREEN)
        self.fullscreen_button.set_is_important(True)
        toolbar.insert(self.fullscreen_button, 3)
        self.fullscreen_button.set_action_name("win.fullscreen")

        return toolbar

    def undo_callback(self, action, parameter):
        print "You clicked \"Undo\"."

    def fullscreen_callback(self, action, parameter):
        # check if the state is the same as Gdk.WindowState.FULLSCREEN, which is a bit flag
        is_fullscreen = self.get_window().get_state() & Gdk.WindowState.FULLSCREEN != 0
        if not is_fullscreen:
            self.fullscreen_button.set_stock_id(Gtk.STOCK_LEAVE_FULLSCREEN)
            self.fullscreen()
        else:
            self.fullscreen_button.set_stock_id(Gtk.STOCK_FULLSCREEN)
            self.unfullscreen()

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.example.toolbar")

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

        # actions that control the application...
        new_action = Gio.SimpleAction.new("new", None)
        new_action.connect("activate", self.new_callback)
        app.add_action(new_action)

        open_action = Gio.SimpleAction.new("open", None)
        open_action.connect("activate", self.open_callback)
        app.add_action(open_action)

    # ... and their callback methods
    def new_callback(self, action, parameter):
        print "You clicked \"New\"."

    def open_callback(self, action, parameter):
        print "You clicked \"Open\"."

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
