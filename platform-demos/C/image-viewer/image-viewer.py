#!/usr/bin/python

from gi.repository import Gtk, GdkPixbuf, Gdk
import os, sys

class GUI:
	image = 0

	def __init__(self):

		window = Gtk.Window()
		window.set_title ("Image Viewer")
		window.connect_after('destroy', self.destroy)

		box = Gtk.Box()
		box.set_spacing(5)
		box.set_orientation (Gtk.Orientation.VERTICAL)
		window.add (box)

		self.image = Gtk.Image()
		box.pack_start (self.image, True, True, 0)

		button = Gtk.Button ("Open a picture...")
		box.pack_start (button, False, False, 0)
		button.connect_after('clicked', self.on_open_clicked)

		window.show_all()

	def destroy(window, self):
		Gtk.main_quit()

	def on_open_clicked (self, button):
		dialog = Gtk.FileChooserDialog ("Open Image", button.get_toplevel(), Gtk.FileChooserAction.OPEN);
		dialog.add_button (Gtk.STOCK_CANCEL, 0)
		dialog.add_button (Gtk.STOCK_OPEN, 1)
		dialog.set_default_response(1)

		filefilter = Gtk.FileFilter ()
		filefilter.add_pixbuf_formats ()
		dialog.set_filter(filefilter)

		if dialog.run() == 1:
			self.image.set_from_file(dialog.get_filename())
		dialog.destroy()

def main():
	app = GUI()
	Gtk.main()

if __name__ == "__main__":
    sys.exit(main())
