from gi.repository import Gtk
from gi.repository import Gio
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Menubutton Example", application=app)
        self.set_default_size(600, 400)

        grid = Gtk.Grid()
        
        # a menubutton
        menubutton = Gtk.MenuButton()
        menubutton.set_size_request(80, 35)
        
        grid.attach(menubutton, 0, 0, 1, 1)
        
        # a menu with two actions
        menumodel = Gio.Menu()
        menumodel.append("New", "app.new")
        menumodel.append("About", "win.about")

        # a submenu with one action for the menu
        submenu = Gio.Menu()
        submenu.append("Quit", "app.quit")
        menumodel.append_submenu("Other", submenu)

        # the menu is set as the menu of the menubutton
        menubutton.set_menu_model(menumodel)

        # the action related to the window (about)
        about_action = Gio.SimpleAction.new("about", None)
        about_action.connect("activate", self.about_callback)
        self.add_action(about_action)
        
        self.add(grid)

    # callback for "about"
    def about_callback(self, action, parameter):
        print "You clicked \"About\""

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

        #  the actions related to the application
        new_action = Gio.SimpleAction.new("new", None)
        new_action.connect("activate", self.new_callback)
        self.add_action(new_action)
        
        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.quit_callback)
        self.add_action(quit_action)
    
    # callback functions for the actions related to the application
    def new_callback(self, action, parameter):
        print "You clicked \"New\""

    def quit_callback(self, action, parameter):
        print "You clicked \"Quit\""
        self.quit()

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
