#!/usr/bin/python

from gi.repository import Gtk, Gst, GObject 
import os, sys

#Comment the first line and uncomment the second before installing
#or making the tarball (alternatively, use project variables)
UI_FILE = "guitar_tuner_py.ui"
#UI_FILE = "/usr/local/share/guitar_tuner_py/ui/guitar_tuner_py.ui"

class GUI:
	LENGTH = 500
	# Frequencies of the strings
	NOTE_E = 369.23
	NOTE_A = 440
	NOTE_D = 587.33
	NOTE_G = 783.99
	NOTE_B = 987.77
	NOTE_e = 1318.5
	
	def __init__(self):
		self.builder = Gtk.Builder()
		self.builder.add_from_file(UI_FILE)
		self.builder.connect_signals(self)

		window = self.builder.get_object('window')
		window.show_all()


	def on_button_clicked (self, button):
		label = button.get_child()
		text = label.get_label()
		
		if text == "E":
			self.play_sound (self.NOTE_E)
		elif text == "A":
			self.play_sound (self.NOTE_A)
		elif text == "G":
			self.play_sound (self.NOTE_G)
		elif text == "D":
			self.play_sound (self.NOTE_D)
		elif text == "B":
			self.play_sound (self.NOTE_B)
		elif text == "e":
			self.play_sound (self.NOTE_e)
			
	def destroy(window, self):
		Gtk.main_quit()

	def play_sound(self, frequency):
		pipeline = Gst.Pipeline(name='note')
		source = Gst.ElementFactory.make('audiotestsrc', 'src')
		sink = Gst.ElementFactory.make('autoaudiosink', 'output')
		
		source.set_property('freq', frequency)
		pipeline.add(source)
		pipeline.add(sink)

		source.link (sink)

		pipeline.set_state(Gst.State.PLAYING)

		GObject.timeout_add(self.LENGTH, self.pipeline_stop, pipeline)

	def pipeline_stop(self, pipeline):
		pipeline.set_state(Gst.State.PAUSED)
		return False

	

		
def main():
	Gst.init_check(sys.argv)
	app = GUI()
	Gtk.main()
		
if __name__ == "__main__":
    sys.exit(main())

