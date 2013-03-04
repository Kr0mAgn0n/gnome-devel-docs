from gi.repository import Gtk
import sys

from gi.repository import Gtk
from gi.repository import GdkPixbuf
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, application=app)
        self.set_title("Welcome to GNOME")
        self.set_default_size(300, 300)

        # create a pixbuf from file filename="gnome-image.png", with width=32
        # and height=64 amd boolean preserve_aspect_ratio=False.
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("gnome-image.png", 64, 128, False)

        # create an image
        image = Gtk.Image()
        # set the content of the image as the pixbuf
        image.set_from_pixbuf(pixbuf)
        # add the image to the window
        self.add(image)
        
class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.gnome.ImageExample")

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
