from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="MenuBar Example", application=app)
        self.set_default_size(200, 200)

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

        # a builder to add the UI designed with Glade to the grid:
        builder = Gtk.Builder()
        # get the file (if it is there)
        try:
            builder.add_from_file("menubar_basis.ui")
        except:
            print "file not found"
            sys.exit()

        # we use the method Gtk.Application.set_menubar(menubar) to add the menubar
        # to the application (Note: NOT the window!)
        self.set_menubar(builder.get_object("menubar"))

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
