/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */
/*
 * main.cc
 * Copyright (C) Johannes Schmid 2011 <jhs@idefix>
 * 
 * guitar-tuner-cpp is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * guitar-tuner-cpp is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License along
 * with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <gtkmm.h>
#include <iostream>
#include <gstreamermm.h>


#ifdef ENABLE_NLS
#  include <libintl.h>
#endif



/* For testing propose use the local (not installed) ui file */
/* #define UI_FILE PACKAGE_DATA_DIR"/guitar_tuner_cpp/ui/guitar_tuner_cpp.ui" */
#define UI_FILE "src/guitar_tuner_cpp.ui"

class Sound
{
	public:
		Sound();

		void start_playing(double frequency);
		bool stop_playing();
		
	private:
		Glib::RefPtr<Gst::Pipeline> m_pipeline;
		Glib::RefPtr<Gst::Element> m_source;
		Glib::RefPtr<Gst::Element> m_sink;
};

Sound::Sound()
{
	m_pipeline = Gst::Pipeline::create("note");
	m_source = Gst::ElementFactory::create_element("audiotestsrc",
	                                               "source");
	m_sink = Gst::ElementFactory::create_element("autoaudiosink",
	                                             "output");
	m_pipeline->add(m_source);
	m_pipeline->add(m_sink);
	m_source->link(m_sink);
}

void Sound::start_playing (double frequency)
{
	m_source->set_property("freq", frequency);
	m_pipeline->set_state(Gst::STATE_PLAYING);

	/* stop it after 200ms */
	Glib::signal_timeout().connect(sigc::mem_fun(*this, &Sound::stop_playing),
	                               200);
}

bool Sound::stop_playing()
{
	m_pipeline->set_state(Gst::STATE_NULL);
	return false;
}

static void
on_button_clicked(double frequency, Sound* sound)
{
	sound->start_playing (frequency);
}
                   
int
main(int argc, char *argv[])
{
	Gtk::Main kit(argc, argv);
	Gst::init (argc, argv);
	
	//Load the Glade file and instiate its widgets:
	Glib::RefPtr<Gtk::Builder> builder;
	try
	{
		builder = Gtk::Builder::create_from_file(UI_FILE);
	}
	catch (const Glib::FileError & ex)
	{
		std::cerr << ex.what() << std::endl;
		return 1;
	}
	Gtk::Window* main_win = 0;
	builder->get_widget("main_window", main_win);

	Sound sound;
	Gtk::Button* button;
	
	builder->get_widget("button_E", button);
	button->signal_clicked().connect (sigc::bind<double, Sound*>(sigc::ptr_fun(&on_button_clicked),
	                                              369.23, &sound));
	builder->get_widget("button_A", button);
	button->signal_clicked().connect (sigc::bind<double>(sigc::ptr_fun(&on_button_clicked),
	                                              440, &sound));
	builder->get_widget("button_D", button);
	button->signal_clicked().connect (sigc::bind<double>(sigc::ptr_fun(&on_button_clicked),
	                                              587.33, &sound));
	builder->get_widget("button_G", button);
	button->signal_clicked().connect (sigc::bind<double>(sigc::ptr_fun(&on_button_clicked),
	                                              783.99, &sound));
	builder->get_widget("button_B", button);
	button->signal_clicked().connect (sigc::bind<double>(sigc::ptr_fun(&on_button_clicked),
	                                              987.77, &sound));
	builder->get_widget("button_e", button);
	button->signal_clicked().connect (sigc::bind<double>(sigc::ptr_fun(&on_button_clicked),
	                                              1318.5, &sound));
	
	if (main_win)
	{
		kit.run(*main_win);
	}
	return 0;
}
