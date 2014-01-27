from gi.repository import Gtk
import sys


class MyWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Calculator", application=app)
        self.set_default_size(350, 200)
        self.set_border_width(10)

        # an entry
        self.entry = Gtk.Entry()
        # with an initial text
        self.entry.set_text('0')
        # text aligned on the right
        self.entry.set_alignment(1)
        # the text in the entry cannot be modified writing in it
        self.entry.set_can_focus(False)

        # a grid
        grid = Gtk.Grid()
        grid.set_row_spacing(5)

        # to attach the entry
        grid.attach(self.entry, 0, 0, 1, 1)

        # the labels for the buttons
        buttons = [7, 8, 9, '/',
                   4, 5, 6, '*',
                   1, 2, 3, '-',
                   'C', 0, '=', '+']

        # each row is a ButtonBox, attached to the grid
        for i in range(4):
            hbox = Gtk.ButtonBox.new(Gtk.Orientation.HORIZONTAL)
            hbox.set_spacing(5)
            grid.attach(hbox, 0, i + 1, 1, 1)
            # each ButtonBox has 4 buttons, connected to the callback function
            for j in range(4):
                button = Gtk.Button(label=buttons[i * 4 + j])
                button.set_can_focus(False)
                button.connect("clicked", self.button_clicked)
                hbox.add(button)

        # some variables for the calculations
        self.first_number = 0
        self.second_number = 0
        self.counter = 0
        self.operation = ""

        # add the grid to the window
        self.add(grid)

    # callback function for all the buttons
    def button_clicked(self, button):
        # for the operations
        if button.get_label() == '+':
            self.counter += 1
            if self.counter > 1:
                self.do_operation()
            self.entry.set_text('0')
            self.operation = "plus"
        elif button.get_label() == '-':
            self.counter += 1
            if self.counter > 1:
                self.do_operation()
            self.entry.set_text('0')
            self.operation = "minus"
        elif button.get_label() == '*':
            self.counter += 1
            if self.counter > 1:
                self.do_operation()
            self.entry.set_text('0')
            self.operation = "multiplication"
        elif button.get_label() == '/':
            self.counter += 1
            if self.counter > 1:
                self.do_operation()
            self.entry.set_text('0')
            self.operation = "division"
        # for =
        elif button.get_label() == '=':
            self.do_operation()
            self.entry.set_text(str(self.first_number))
            self.counter = 1
        # for Cancel
        elif button.get_label() == 'C':
            self.first_number = 0
            self.second_number = 0
            self.counter = 0
            self.entry.set_text('')
            self.operation = ""
        # for a digit button
        else:
            new_digit = int(button.get_label())
            if self.entry.get_text() == 'error':
                number = 0
            else:
                number = int(self.entry.get_text())
            number = number * 10 + new_digit
            if self.counter == 0:
                self.first_number = number
            else:
                self.second_number = number
            self.entry.set_text(str(number))

    def do_operation(self):
        if self.operation == "plus":
            self.first_number += self.second_number
        elif self.operation == "minus":
            self.first_number -= self.second_number
        elif self.operation == "multiplication":
            self.first_number *= self.second_number
        elif self.operation == "division":
            try:
                self.first_number /= self.second_number
            except ZeroDivisionError:
                self.first_number = 0
                self.second_number = 0
                self.counter = 0
                self.entry.set_text('error')
                self.operation = ""
                return
        else:
            self.first_number = 0
            self.second_number = 0
            self.counter = 0
            self.entry.set_text('error')


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
