from gi.repository import GLib
from gi.repository import Gtk
from gi.repository import Gio
import sys
 
# This is the window
class MyWindow(Gtk.ApplicationWindow):
 
    #constructor
    def __init__(self, app):
        Gtk.Window.__init__(self, title="AboutDialog Example", application=app)
        self.set_default_size(200, 200)
 
        # We create the message_action and connect the
        # signal and add the action to the application.
        about_action = Gio.SimpleAction.new("about", None)
        about_action.connect("activate", self.about_cb)
        app.add_action(about_action)
        self.show_all()

    def about_cb(self, action, parameter):
        aboutdialog = Gtk.AboutDialog()
        
        #lists of authors and documenters (will be used later)
        authors = ["GNOME Documentation Team", None]
        documenters = ["GNOME Documentation Team", None]
        
        aboutdialog.set_program_name("AboutDialog Example")
        aboutdialog.set_copyright("Copyright \xc2\xa9 2012 GNOME Documentation Team")
        aboutdialog.set_authors(authors)
        aboutdialog.set_documenters(documenters)
        aboutdialog.set_website("http://developer.gnome.org")
        aboutdialog.set_website_label("GNOME Developer Website")
        
        # to close the aboutdialog when "close" is clicked
        aboutdialog.connect("response", self.on_close)
        
        aboutdialog.show()
        
    def on_close(self, action, parameter):
        action.destroy()

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.gtk.example.grid")
 
    def do_activate(self):
        win = MyWindow(self)
        win.show_all()
 
    def quit_cb(self, action, parameter):
        self.quit()
 
    def do_startup (self):
        Gtk.Application.do_startup (self)
 
        menu = Gio.Menu()
        menu.append ("About", "app.about")
        menu.append("Quit", "app.quit")
        self.set_app_menu (menu)
 
        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.quit_cb)
        self.add_action(quit_action)
 
app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
