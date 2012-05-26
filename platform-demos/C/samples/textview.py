from gi.repository import GLib
from gi.repository import Gtk
from gi.repository import Gio
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="TextView Example", application=app)
        self.set_default_size(300, 450)

        # a scrollbar for the child widget (that is, the textview)
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.set_border_width(5)
        # we scroll only if needed
        scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

        # a text buffer (stores text)
        buffer1 = Gtk.TextBuffer()

        # a textview (displays the buffer)
        textview = Gtk.TextView(buffer=buffer1)
        # wrap the text, if needed, breaking lines in between words
        textview.set_wrap_mode(Gtk.WrapMode.WORD)

        # textview is scrolled
        scrolled_window.add_with_viewport(textview)

        self.add(scrolled_window)

class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.gtk.example.grid")

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
