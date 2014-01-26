from gi.repository import Gtk
from gi.repository import Gio
import sys

class MyWindow(Gtk.ApplicationWindow):

    # constructor for a window (the parent window) with a label
    def __init__(self, app):
        Gtk.Window.__init__(self, title="GMenu Example", application=app)
        self.set_default_size(400, 200)
        label = Gtk.Label()
        label.set_text("This application goes boom!")
        self.add(label)

        # create the message_action (a Gio.SimpleAction) - for the window
        message_action = Gio.SimpleAction.new("message", None)
        # connect the signal from the action to the function message_cb()
        message_action.connect("activate", self.message_cb)
        # add the action to the application
        app.add_action(message_action)

    # callback function for the signal "activate" from the message_action
    # in the menu of the parent window
    def message_cb(self, action, parameter):
        # a Gtk.MessageDialog
        messagedialog = Gtk.MessageDialog(parent=self,
                                          flags=Gtk.DialogFlags.MODAL,
                                          type=Gtk.MessageType.WARNING,
                                          buttons=Gtk.ButtonsType.OK_CANCEL,
                                          message_format="This action will cause the universe to stop existing.")
        # connect the response (of the button clicked) to the function
        # dialog_response()
        messagedialog.connect("response", self.dialog_response)
        # show the messagedialog
        messagedialog.show()

    def dialog_response(self, widget, response_id):
        # if the button clicked gives response OK (-5)
        if response_id == Gtk.ResponseType.OK:
            print "*boom*"
        # if the button clicked gives response CANCEL (-6)
        elif response_id == Gtk.ResponseType.CANCEL:
            print "good choice"
        # if the messagedialog is destroyed (by pressing ESC)
        elif response_id == Gtk.ResponseType.DELETE_EVENT:
            print "dialog closed or cancelled"
        # finally, destroy the messagedialog
        widget.destroy()

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def quit_cb(self, action, parameter):
        self.quit()

    def do_startup (self):
        Gtk.Application.do_startup(self)

        # create a menu (a Gio.Menu)
        menu = Gio.Menu()
        # append a menu item with label "Message" and action "app.message"
        menu.append("Message", "app.message")
        # append a menu item with label "Quit" and action "app.quit"
        menu.append("Quit", "app.quit")
        # set menu as the menu for the application
        self.set_app_menu(menu)

        # a new simpleaction - for the application
        quit_action = Gio.SimpleAction.new("quit", None)
        quit_action.connect("activate", self.quit_cb)
        self.add_action (quit_action)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
