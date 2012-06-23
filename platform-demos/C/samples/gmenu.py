from gi.repository import GLib
from gi.repository import Gtk
from gi.repository import Gio
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="GMenu Example", application=app)

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.gtk.example.grid")

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def new_cb(self, action, parameter):
        print "This does nothing. It is only a demonstration."

    def about_cb(self, action, parameter):
        print "No AboutDialog for you. This is only a demonstration"

    def quit_cb(self, action, parameter):
        self.quit()

    def do_startup (self):
        Gtk.Application.do_startup (self)

        menu = Gio.Menu()
        menu.append("New", "app.new")
        menu.append ("About", "app.about")
        menu.append("Quit", "app.quit")
        self.set_app_menu (menu)

        new_action = Gio.SimpleAction.new ("new", None)
        new_action.connect ("activate", self.new_cb)
        self.add_action (new_action)

        about_action = Gio.SimpleAction.new ("about", None)
        about_action.connect ("activate", self.about_cb)
        self.add_action (about_action)

        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.quit_cb)
        self.add_action (quit_action)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
