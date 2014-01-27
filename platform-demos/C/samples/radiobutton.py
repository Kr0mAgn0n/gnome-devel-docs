from gi.repository import Gtk
import sys


class MyWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="RadioButton Example", application=app)
        self.set_default_size(250, 100)
        self.set_border_width(20)

        # a new radiobutton with a label
        button1 = Gtk.RadioButton(label="Button 1")
        # connect the signal "toggled" emitted by the radiobutton
        # with the callback function toggled_cb
        button1.connect("toggled", self.toggled_cb)

        # another radiobutton, in the same group as button1
        button2 = Gtk.RadioButton.new_from_widget(button1)
        # with label "Button 2"
        button2.set_label("Button 2")
        # connect the signal "toggled" emitted by the radiobutton
        # with the callback function toggled_cb
        button2.connect("toggled", self.toggled_cb)
        # set button2 not active by default
        button2.set_active(False)

        # another radiobutton, in the same group as button1,
        # with label "Button 3"
        button3 = Gtk.RadioButton.new_with_label_from_widget(
            button1, "Button 3")
        # connect the signal "toggled" emitted by the radiobutton
        # with the callback function toggled_cb
        button3.connect("toggled", self.toggled_cb)
        # set button3 not active by default
        button3.set_active(False)

        # a grid to place the buttons
        grid = Gtk.Grid.new()
        grid.attach(button1, 0, 0, 1, 1)
        grid.attach(button2, 0, 1, 1, 1)
        grid.attach(button3, 0, 2, 1, 1)
        # add the grid to the window
        self.add(grid)

    # callback function
    def toggled_cb(self, button):
        # a string to describe the state of the button
        state = "unknown"
        # whenever the button is turned on, state is on
        if button.get_active():
            state = "on"
        # else state is off
        else:
            state = "off"
        # whenever the function is called (a button is turned on or off)
        # print on the terminal which button was turned on/off
        print button.get_label() + " was turned " + state


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
