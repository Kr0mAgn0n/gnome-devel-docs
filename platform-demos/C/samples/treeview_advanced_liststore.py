from gi.repository import Gtk
from gi.repository import Pango
import sys

list_of_dvd = [["The Usual Suspects"],
               ["Gilda"],
               ["The Godfather"],
               ["Pulp Fiction"],
               ["Once Upon a Time in the West"],
               ["Rear Window"]]

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="My DVDs", application=app)
        self.set_default_size(250, 100)
        self.set_border_width(10)

        # the data are stored in the model
        # create a liststore with one column
        self.listmodel = Gtk.ListStore(str)
        for i in range(len(list_of_dvd)):
            self.listmodel.append(list_of_dvd[i])

        # a treeview to see the data stored in the model
        view = Gtk.TreeView(model=self.listmodel)

        # cellrenderer for the first column
        cell = Gtk.CellRendererText()
        # the first column is created
        col = Gtk.TreeViewColumn("Title", cell, text=0)
        # and it is appended to the treeview
        view.append_column(col)

        # when a row of the treeview is selected, it emits a signal
        self.selection = view.get_selection()
        self.selection.connect("changed", self.on_changed)

        # the label we use to show the selection
        self.label = Gtk.Label()
        self.label.set_text("")

        # a button to add new titles, connected to a callback function
        self.button_add = Gtk.Button(label="Add")
        self.button_add.connect("clicked", self.add_cb)

        # an entry to enter titles
        self.entry = Gtk.Entry()

        # a button to remove titles, connected to a callback function
        self.button_remove = Gtk.Button(label="Remove")
        self.button_remove.connect("clicked", self.remove_cb)

        # a button to remove all titles, connected to a callback function
        self.button_remove_all = Gtk.Button(label="Remove All")
        self.button_remove_all.connect("clicked", self.remove_all_cb)

        # a grid to attach the widgets
        grid = Gtk.Grid()
        grid.attach(view, 0, 0, 4, 1)
        grid.attach(self.label, 0, 1, 4, 1)
        grid.attach(self.button_add, 0, 2, 1, 1)
        grid.attach_next_to(self.entry, self.button_add, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.button_remove, self.entry, Gtk.PositionType.RIGHT, 1, 1)
        grid.attach_next_to(self.button_remove_all, self.button_remove, Gtk.PositionType.RIGHT, 1, 1)

        # add the grid to the window
        self.add(grid)

    def on_changed(self, selection):
        # get the model and the iterator that points at the data in the model
        (model, iter) = selection.get_selected()
        # set the label to a new value depending on the selection, if there is one
        if iter is not None:
            self.label.set_text("\n %s" %(model[iter][0]))
        else:
            self.label.set_text("")
        return True

    # callback function for the "Add" button
    def add_cb(self, button):
        # append to the model the title that is in the entry
        title = self.entry.get_text()
        self.listmodel.append([title])
        # and print a message in the terminal
        print "%s has been added" %(title)

    def remove_cb(self, button):
        # if there is still an entry in the model
        if len(self.listmodel) != 0:
            # get the selection
            (model, iter) = self.selection.get_selected()
            # if there is a selection, print a message in the terminal
            # and remove it from the model
            if iter is not None:
                print "%s has been removed" %(model[iter][0])
                self.listmodel.remove(iter)
            # otherwise, ask the user to select something to remove
            else:
                print "Select a title to remove"
        # else, if there are no entries in the model, print "Empty list"
        # in the terminal
        else:
            print "Empty list"

    def remove_all_cb(self, button):
        # if there is still an entry in the model
        if len(self.listmodel) != 0:
            # remove all the entries in the model
            for i in range(len(self.listmodel)):
                iter = self.listmodel.get_iter(0)
                self.listmodel.remove(iter)
        # print a message in the terminal alerting that the model is empty
        print "Empty list"


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
