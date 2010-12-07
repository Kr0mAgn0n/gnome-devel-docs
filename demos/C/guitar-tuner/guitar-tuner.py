#!/usr/bin/env python
# -*- Mode: Python; py-indent-offset: 4 -*-
# vim: tabstop=4 shiftwidth=4 expandtab
#
# guitar-tuner.py 
# Copyright (C) John (J5) Palmieri 2010 <johnp@redhat.com>
# 
# guitar-tuner is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# guitar-tuner is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
#/

from gi.repository import Gtk, Gst, GObject 
import sys

class GuitarTunerApp(object):
    UI_FILE = 'src/guitar_tuner.ui'
    NOTE_E = 369.23
    NOTE_A = 440
    NOTE_D = 587.33
    NOTE_G = 783.99
    NOTE_B = 987.77
    NOTE_e = 1318.5

    LENGTH = 500
    WIDGET_WINDOW = "window"

    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file(self.UI_FILE)

        window = builder.get_object(self.WIDGET_WINDOW)
        window.connect('destroy', Gtk.main_quit)
        builder.connect_signals(self)

        window.show_all()

    def pipeline_stop(self, pipeline):
        pipeline.set_state(Gst.State.PAUSED)
        return False

    def play_sound(self, frequency):
        pipeline = Gst.Pipeline(name='note')
        source = Gst.ElementFactory.make('audiotestsrc', 'src')
        sink = Gst.ElementFactory.make('autoaudiosink', 'output')

        source.set_property('freq', frequency)
        pipeline.add(source)
        pipeline.add(sink)
        pipeline.set_state(Gst.State.PLAYING)

        GObject.timeout_add(self.LENGTH, self.pipeline_stop, pipeline)

    def on_button_clicked(self, button):
        label = button.get_child()
        text = label.get_label()

        if text == "E":
            self.play_sound (self.NOTE_E);
     	elif text == "A":
            self.play_sound (self.NOTE_A);
        elif text == "G":
            self.play_sound (self.NOTE_G);
        elif text == "D":
            self.play_sound (self.NOTE_D);
        elif text == "B":
            self.play_sound (self.NOTE_B);
        elif text == "e":
            self.play_sound (self.NOTE_e);

if __name__ == '__main__':
    # initialize GStreamer for now, though this may be provided
    # by an override in the future
    Gst.init_check(sys.argv)
    app = GuitarTunerApp()
    Gtk.main()

