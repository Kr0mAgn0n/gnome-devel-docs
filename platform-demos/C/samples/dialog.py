from gi.repository import GLib
from gi.repository import Gtk
from gi.repository import Gio
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="GNOME Button", application=app)
        self.set_default_size(250, 50)
        
        button = Gtk.Button("Click me")
        button.connect("clicked", self.on_button_click)
        self.add(button)
        button.show()
        
    def on_button_click(self, *args):
        dialog = Gtk.Dialog("A Gtk+ Dialog", self, Gtk.DialogFlags.MODAL)
        dialog.add_button(button_text="OK", response_id=Gtk.ResponseType.OK)
        # otherwise, we can add buttons as
        # dialog.add_button(button_text="Another button", response_id=42)
        # where the response_id is any integer
        content_area = dialog.get_content_area()
        label = Gtk.Label("This demonstrates a dialog with a label")
        content_area.add(label)
        label.show()
        dialog.connect("response", self.on_response)
        dialog.show_all()
        
    def on_response(self, widget, response_id):
        print "response_id is", response_id
        widget.destroy()
                
class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.gtk.example.grid")

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup (self):
        Gtk.Application.do_startup (self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
