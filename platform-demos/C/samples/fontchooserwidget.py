from gi.repository import Gtk
import sys


class MyWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="FontChooserWidget", application=app)

        # a font chooser
        self.font_chooser = Gtk.FontChooserWidget()
        # a default font
        self.font_chooser.set_font("Sans")
        # a text to preview the font
        self.font_chooser.set_preview_text(
            "This is an example of preview text!")

        # connect signal from the font chooser to the callback function
        self.font_chooser.connect("notify::font", self.font_cb)

        # add the font chooser to the window
        self.add(self.font_chooser)

    # callback function:
    def font_cb(self, event, user_data):
        # print in the terminal
        print "You chose the font " + self.font_chooser.get_font()


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
