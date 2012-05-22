from gi.repository import GLib
from gi.repository import Gtk
from gi.repository import Gio
import sys
 
 
# This is the window
class MyWindow(Gtk.ApplicationWindow):
 
    #constructor
    def __init__(self, app):
        Gtk.Window.__init__(self, title="GMenu Example", application=app)
        label = Gtk.Label()
        label.set_text("This application goes boom!")
        self.add(label)
        self.set_default_size(400, 200)
 
        # We create the message_action and connect the
        # signal and add the action to the application.
        message_action = Gio.SimpleAction.new("message", None)
        message_action.connect("activate", self.message_cb)
        app.add_action (message_action)

    def dialog_response(self, widget, response_id):
        if response_id == Gtk.ResponseType.OK:
		    print "*boom*"
        elif response_id == Gtk.ResponseType.CANCEL:
            print "good choice"
        elif response_id == Gtk.ResponseType.DELETE_EVENT:
            print "dialog closed or cancelled"
        widget.destroy()
 
    def message_cb(self, action, parameter):
        messagedialog = Gtk.MessageDialog (self, 
                                           Gtk.DialogFlags.MODAL, 
                                           Gtk.MessageType.WARNING,
                                           Gtk.ButtonsType.OK_CANCEL, 
                                           "This action will cause the universe to stop existing.")
        messagedialog.connect("response", self.dialog_response)
        messagedialog.show()
 
 
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
        menu.append ("Message", "app.message")
        menu.append("Quit", "app.quit")
        self.set_app_menu (menu)
 
        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.quit_cb)
        self.add_action (quit_action)
 
app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
