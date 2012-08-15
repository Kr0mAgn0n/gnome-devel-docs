from gi.repository import Gtk
import sys

class MyWindow(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="Calculator", application=app)
        self.set_default_size(450, 100)
        self.set_border_width(10)

        box = Gtk.ButtonBox.new(Gtk.Orientation.HORIZONTAL)
        
        button_plus = Gtk.Button(label="+")
        button_plus.connect("clicked", self.plus_callback)
        box.add(button_plus)

        button_minus = Gtk.Button(label="-")
        button_minus.connect("clicked", self.minus_callback)
        box.add(button_minus)

        button_multi = Gtk.Button(label="*")
        button_multi.connect("clicked", self.multi_callback)
        box.add(button_multi)
        
        button_divided = Gtk.Button(label="/")
        button_divided.connect("clicked", self.divided_callback)
        box.add(button_divided)
        
        button_equal = Gtk.Button(label="=")
        button_equal.connect("clicked", self.equal_callback)
        box.add(button_equal)
                
        button_cancel = Gtk.Button(label="C")
        button_cancel.connect("clicked", self.cancel_callback)
        box.add(button_cancel)
        
        box.set_child_non_homogeneous(button_cancel, True)
              
        self.entry = Gtk.Entry()
        self.entry.set_text('0.0')
        self.entry.connect("activate", self.equal_callback)

        self.second_number = 0.0
        self.result = 0.0

        self.operation = ""

        grid = Gtk.Grid()
        grid.attach(self.entry, 0, 0, 1, 1)
        grid.attach(box, 0, 1, 1, 1)
        
        self.add(grid)
        
    def plus_callback(self, button):
        if self.entry.get_text() == "":
            self.first_number = 0.0
        else:
            self.first_number = float(self.entry.get_text())
        self.operation = "plus"

    def minus_callback(self, button):
        if self.entry.get_text() == "":
            self.first_number = 0.0
        else:
            self.first_number = float(self.entry.get_text())
        self.operation = "minus"

    def multi_callback(self, button):
        if self.entry.get_text() == "":
            self.first_number = 0.0
        else:
            self.first_number = float(self.entry.get_text())
        self.operation = "multiplication"

    def divided_callback(self, button):
        if self.entry.get_text() == "":
            self.first_number = 0.0
        else:
            self.first_number = float(self.entry.get_text())
        self.operation = "division"

    def equal_callback(self, button):
        self.second_number =  float(self.entry.get_text())
        if self.operation == "plus":
            self.result = self.first_number + self.second_number
        elif self.operation == "minus":
            self.result = self.first_number - self.second_number
        elif self.operation == "multiplication":
            self.result = self.first_number * self.second_number
        elif self.operation == "division":
            self.result = self.first_number / self.second_number
        else:
            print "Error!"
        self.first_number = self.result
        self.entry.set_text(str(self.result))

    def cancel_callback(self, button):
        if self.entry.get_text() == "":
            self.first_number = 0.0
        else:
            self.first_number = float(self.entry.get_text())
        self.second_number = 0.0
        self.result = 0.0
        self.entry.set_text('0.0')

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
