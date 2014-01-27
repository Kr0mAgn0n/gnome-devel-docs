from gi.repository import Gtk
from gi.repository import Gio
import sys


class MyWindow(Gtk.ApplicationWindow):

     # constructor for a window (the parent window)
    def __init__(self, app):
        Gtk.Window.__init__(self, title="AboutDialog Example", application=app)
        self.set_default_size(200, 200)

        # create the about_action (a Gio.SimpleAction)
        about_action = Gio.SimpleAction.new("about", None)
        # connect the signal from the action to the function about_cb()
        about_action.connect("activate", self.about_cb)
        # add the action to the application
        app.add_action(about_action)

    # callback function for the about_action's "activate" signal
    def about_cb(self, action, parameter):
        # a  Gtk.AboutDialog
        aboutdialog = Gtk.AboutDialog()

        # lists of authors and documenters (will be used later)
        authors = ["GNOME Documentation Team"]
        documenters = ["GNOME Documentation Team"]

        # we fill in the aboutdialog
        aboutdialog.set_program_name("AboutDialog Example")
        aboutdialog.set_copyright(
            "Copyright \xc2\xa9 2012 GNOME Documentation Team")
        aboutdialog.set_authors(authors)
        aboutdialog.set_documenters(documenters)
        aboutdialog.set_website("http://developer.gnome.org")
        aboutdialog.set_website_label("GNOME Developer Website")

        # we do not want to show the title, which by default would be "About AboutDialog Example"
        # we have to reset the title of the messagedialog window after setting
        # the program name
        aboutdialog.set_title("")

        # to close the aboutdialog when "close" is clicked we connect the
        # "response" signal to on_close
        aboutdialog.connect("response", self.on_close)
        # show the aboutdialog
        aboutdialog.show()

    # destroy the aboutdialog
    def on_close(self, action, parameter):
        action.destroy()


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def quit_cb(self, action, parameter):
        self.quit()

    def do_startup(self):
        Gtk.Application.do_startup(self)

        # create a menu (a Gio.Menu)
        menu = Gio.Menu()
        # append a menu item with label "About" and action "app.about"
        menu.append("About", "app.about")
        # append a menu item with label "Quit" and action "app.quit"
        menu.append("Quit", "app.quit")
        # set menu as the menu for the application
        self.set_app_menu(menu)

        # a new simpleaction - for the application
        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.quit_cb)
        self.add_action(quit_action)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
