from gi.repository import Gtk
import sys


class MyWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Paned Example", application=app)
        self.set_default_size(450, 350)

        # a new widget with two adjustable panes,
        # one on the left and one on the right
        paned = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)

        # two images
        image1 = Gtk.Image()
        image1.set_from_file("gnome-image.png")
        image2 = Gtk.Image()
        image2.set_from_file("tux.png")

        # add the first image to the left pane
        paned.add1(image1)
        # add the second image to the right pane
        paned.add2(image2)

        # add the panes to the window
        self.add(paned)


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
