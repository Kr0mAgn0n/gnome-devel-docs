#!/usr/bin/python

from gi.repository import Gtk, Gst, GObject
import os, sys

#Comment the first line and uncomment the second before installing
#or making the tarball (alternatively, use project variables)
UI_FILE = "src/guitar_tuner.ui"
#UI_FILE = "/usr/local/share/guitar_tuner_py/ui/guitar_tuner.ui"

class GUI:
	LENGTH = 500
	# Frequencies of the strings
	frequencies = {
		'E': 329.63,
		'A': 440,
		'D': 587.33,
		'G': 783.99,
		'B': 987.77,
		'e': 1318.5
	}

	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file(UI_FILE)
		self.builder.connect_signals(self)

		window = self.builder.get_object('window')
		window.show_all()

	def on_button_clicked (self, button):
		label = button.get_child()
		text = label.get_label()
		self.play_sound (self.frequencies[text])

	def destroy(window, self):
		Gtk.main_quit()

	def pipeline_stop(self, pipeline):
		pipeline.set_state(Gst.State.NULL)
		return False

	def play_sound(self, frequency):
		pipeline = Gst.Pipeline(name='note')
		source = Gst.ElementFactory.make('audiotestsrc', 'src')
		sink = Gst.ElementFactory.make('autoaudiosink', 'output')

		source.set_property('freq', frequency)
		pipeline.add(source)
		pipeline.add(sink)
		source.link(sink)

		pipeline.set_state(Gst.State.PLAYING)

		GObject.timeout_add(self.LENGTH, self.pipeline_stop, pipeline)

def main():
	Gst.init_check(sys.argv)
	app = GUI()
	Gtk.main()

if __name__ == "__main__":
    sys.exit(main())

