from gi.repository import Gtk
from gi.repository import cairo
import sys
import math


class MyWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Choose an angle", application=app)
        self.set_default_size(400, 400)
        self.set_border_width(10)

        # a default angle
        self.angle = 360

        grid = Gtk.Grid()

        # a spinbutton that takes the value of an angle
        ad = Gtk.Adjustment(360, 0, 360, 1, 0, 0)
        self.spin = Gtk.SpinButton(adjustment=ad, climb_rate=1, digits=0)
        self.spin.connect("value-changed", self.get_angle)

        # a drawing area for drawing whatever we want
        self.darea = Gtk.DrawingArea()
        # that we describe in the method draw(), connected to the signal "draw"
        self.darea.connect("draw", self.draw)
        # we have to request a minimum size of the drawing area, or it will
        # disappear
        self.darea.set_size_request(300, 300)

        grid.attach(self.spin, 0, 0, 1, 1)
        grid.attach(self.darea, 0, 1, 1, 1)

        self.add(grid)

    # whenever we get a new angle in the spinbutton
    def get_angle(self, event):
        self.angle = self.spin.get_value_as_int()
        # redraw what is in the drawing area
        self.darea.queue_draw()

    def draw(self, darea, cr):
        # a 10-pixels-wide line
        cr.set_line_width(10)
        # red
        cr.set_source_rgba(0.5, 0.0, 0.0, 1.0)

        # get the width and height of the drawing area
        w = self.darea.get_allocated_width()
        h = self.darea.get_allocated_height()

        # move to the center of the drawing area
        # (translate from the top left corner to w/2, h/2)
        cr.translate(w / 2, h / 2)
        # draw a line to (55, 0)
        cr.line_to(55, 0)
        # and get back to (0, 0)
        cr.line_to(0, 0)
        # draw an arc centered in the origin, 50 pixels wide, from the angle 0
        # (in radians) to the angle given by the spinbutton (in degrees)
        cr.arc(0, 0, 50, 0, self.angle * (math.pi / 180))
        # draw a line back to the origin
        cr.line_to(0, 0)
        # drawing the path, and keeping the path for future use
        cr.stroke_preserve()

        # set a colour
        cr.set_source_rgba(0.0, 0.5, 0.5, 1.0)
        # and use it to fill the path (that we had kept)
        cr.fill()


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
