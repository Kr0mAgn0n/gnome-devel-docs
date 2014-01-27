from gi.repository import Gtk
import sys


class MyWindow(Gtk.ApplicationWindow):
    # create a window

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Welcome to GNOME", application=app)
        self.set_default_size(300, 300)

        # create an image
        image = Gtk.Image()
        # set the content of the image as the file filename.png
        image.set_from_file("gnome-image.png")
        # add the image to the window
        self.add(image)


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
