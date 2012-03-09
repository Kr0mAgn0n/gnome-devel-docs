/* -*- Mode: C++; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */

#include <gtkmm.h>
#include <iostream>

Gtk::Image* image = 0;

static void
on_open_image ()
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
	filter->set_name("Images");
	dialog.add_filter (filter);

	const int response = dialog.run();
	dialog.hide();

	switch (response)
	{
		case Gtk::RESPONSE_ACCEPT:
			image->set(dialog.get_filename());
			break;
		default:
			break;
	}
}

int
main (int argc, char *argv[])
{
	Gtk::Main kit(argc, argv);

	Gtk::Window main_win;
	main_win.set_title ("image-viewer-cpp");

	Gtk::Box* box = Gtk::manage(new Gtk::Box());
	box->set_orientation (Gtk::ORIENTATION_VERTICAL);
	box->set_spacing(6);
	main_win.add(*box);

	image = Gtk::manage(new Gtk::Image());
	box->pack_start (*image, true, true);
	
	Gtk::Button* button = Gtk::manage(new Gtk::Button("Open Image…"));
	button->signal_clicked().connect (
		sigc::ptr_fun(&on_open_image));
	box->pack_start (*button, false, false);

	main_win.show_all_children();
	kit.run(main_win);

	return 0;
}
