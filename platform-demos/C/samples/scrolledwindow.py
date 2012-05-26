from gi.repository import GLib
from gi.repository import Gtk
from gi.repository import Gio
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="ScrolledWindow Example", application=app)
        self.set_default_size(200, 200)

        # the scrolledwindow
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_border_width(10)
        # there is always the scrollbar (otherwise: AUTOMATIC - only if needed - or NEVER)
        scrolled_window.set_policy(Gtk.PolicyType.ALWAYS, Gtk.PolicyType.ALWAYS)

        # an image - slightly larger than the window...
        image = Gtk.Image()
        image.set_from_file("gnome-image.png")

        # we add the scrollbar to the image
        scrolled_window.add_with_viewport(image)

        self.add(scrolled_window)

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.gtk.example.grid")

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
