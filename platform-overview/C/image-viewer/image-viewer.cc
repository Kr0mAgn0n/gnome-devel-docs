/* -*- Mode: C++; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */

#include <gtkmm.h>
#include <iostream>

#include "config.h"


#ifdef ENABLE_NLS
#  include <libintl.h>
#endif


static void
on_open_image (Gtk::Image* image)
{
	Gtk::FileChooserDialog dialog("Open image",
	                              Gtk::FILE_CHOOSER_ACTION_OPEN);
	dialog.add_button (Gtk::Stock::OPEN,
	                   Gtk::RESPONSE_ACCEPT);
	dialog.add_button (Gtk::Stock::CANCEL,
	                   Gtk::RESPONSE_CANCEL);

	Glib::RefPtr<Gtk::FileFilter> filter =
		Gtk::FileFilter::create();
	filter->add_pixbuf_formats();
	dialog.add_filter (filter);

	switch (dialog.run())
	{
		case Gtk::RESPONSE_ACCEPT:
			image->set(dialog.get_filename());
			break;
		default:
			break;
	}
	dialog.hide();
}

int
main (int argc, char *argv[])
{
	Gtk::Main kit(argc, argv);

	Gtk::Window* main_win = new Gtk::Window(Gtk::WINDOW_TOPLEVEL);
	main_win->set_title ("image-viewer-cpp");

	Gtk::Box* box = new Gtk::Box();
	box->set_orientation (Gtk::ORIENTATION_VERTICAL);
	box->set_spacing(5);
	main_win->add(*box);

	Gtk::Image* image = new Gtk::Image();
	box->pack_start (*image, true, true);
	
	Gtk::Button* button = new Gtk::Button("Open Image…");
	button->signal_clicked().connect (sigc::bind<Gtk::Image*>(sigc::ptr_fun(&on_open_image), image));
	box->pack_start (*button, false, false);
	
	main_win->show_all();
	
	if (main_win)
	{
		kit.run(*main_win);
	}
	return 0;
}
