from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Paned Example", application=app)
        self.set_default_size(450, 350)

        paned = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)

        image1 = Gtk.Image()
        image1.set_from_file("gnome-image.png")
        image2 = Gtk.Image()
        image2.set_from_file("tux.png")

        paned.add1(image1)
        paned.add2(image2)

        self.add(paned)

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
