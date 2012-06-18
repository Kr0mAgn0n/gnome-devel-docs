from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    # construct a window (the parent window)
    def __init__(self, app):
        Gtk.Window.__init__(self, title="GNOME Button", application=app)
        self.set_default_size(250, 50)

        # a button on the parent window
        button = Gtk.Button("Click me")
        # connect the signal "clicked" of the button with the function on_button_click()
        button.connect("clicked", self.on_button_click)
        # add the button to the window
        self.add(button)

    # callback function for the signal "clicked" of the button in the parent window
    def on_button_click(self, widget):
        # create a Gtk.Dialog
        dialog = Gtk.Dialog()
        dialog.set_title("A Gtk+ Dialog")
        # The window defined in the constructor (self) is the parent of the dialog.
        # Furthermore, the dialog is on top of the parent window
        dialog.set_transient_for(self)
        # set modal true: no interaction with other windows of the application
        dialog.set_modal(True)
        # add a button to the dialog window
        dialog.add_button(button_text="OK", response_id=Gtk.ResponseType.OK)
        # connect the "response" signal (the button has been clicked) to the function on_response()
        dialog.connect("response", self.on_response)

        # get the content area of the dialog, add a label to it
        content_area = dialog.get_content_area()
        label = Gtk.Label("This demonstrates a dialog with a label")
        content_area.add(label)
        # show the dialog
        dialog.show_all()

    def on_response(self, widget, response_id):
        print "response_id is", response_id
        # destroy the widget (the dialog) when the function on_response() is called
        # (that is, when the button of the dialog has been clicked)
        widget.destroy()

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup (self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
