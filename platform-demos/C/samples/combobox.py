from gi.repository import Gtk
import sys

distros = [["Select distribution"], ["Fedora"], ["Mint"], ["Suse"]]

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Welcome to GNOME", application=app)
        self.set_default_size(200, -1)
        self.set_border_width(10)

        # the data in the model, of type string
        listmodel = Gtk.ListStore(str)
        # there is no insert_with_values in Python, we use append to
        for i in range(len(distros)):
            listmodel.append(distros[i])

        # a combobox to see the data stored in the model
        combobox = Gtk.ComboBox(model=listmodel)

        # a cellrenderer
        cell = Gtk.CellRendererText()
        # packs the cell into the beginning of the combobox, allocating
        # (False) no more space than needed
        combobox.pack_start(cell, False)
        # there is no set_attributes() in Python
        # associates a property ("text") of the cellrenderer (cell) to a column (column 0)
        # in the model used by the combobox
        combobox.add_attribute(cell, "text", 0)
        # the first row is the active one
        combobox.set_active(0)

        # when a row is selected, emit a signal
        combobox.connect("changed", self.on_changed)

        self.add(combobox)

    def on_changed(self, combo):
        # if the row selected is not the first one, write its value on the terminal
        if combo.get_active() != 0:
            print "You chose " + str(distros[combo.get_active()][0]) +"."
        return True


class MyApplication(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self, application_id="org.example.combobox")

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
