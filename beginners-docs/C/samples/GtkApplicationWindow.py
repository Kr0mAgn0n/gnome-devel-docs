from gi.repository import Gtk
import sys

# a Gtk ApplicationWindow
class MyWindow(Gtk.ApplicationWindow):
    # constructor: the window belongs to the application app
    def __init__(self, app):
        Gtk.Window.__init__(self, application=app)
        # set the title of the window
        self.set_title("Welcome to GNOME")

class MyApplication(Gtk.Application):
    # constructor of the Gtk Application
    def __init__(self):
        Gtk.Application.__init__(self)

    # create and activate a MyWindow, with self (the MyApplication) as
    # application app the window belongs to.
    def do_activate(self):
        win = MyWindow(self)
        # show the window and all its content
        # note that this line could also go in the constructor of MyWindow
        win.show_all()

    # start up the application
    def do_startup(self):
        Gtk.Application.do_startup(self)

# create the application
app = MyApplication()
# run the application, which returns the value exit_status
exit_status = app.run(sys.argv)
# terminate the program using exit_status
sys.exit(exit_status)
