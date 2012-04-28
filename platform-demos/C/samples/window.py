from gi.repository import Gtk
import sys

class MyApp(Gtk.Application):
    def do_activate(self):
        window = Gtk.Window(application = self)
        window.set_title("Welcome to GNOME")
        window.show_all()

MyApp(application_id = "org.example.whatever").run(sys.argv)
