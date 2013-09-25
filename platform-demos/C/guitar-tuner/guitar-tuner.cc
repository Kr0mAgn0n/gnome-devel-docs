/* -*- Mode: C++; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */

#include <gtkmm.h>
#include <gstreamermm.h>
#include <iostream>

/* For testing purposes, use the local (not installed) ui file */
/* #define UI_FILE PACKAGE_DATA_DIR"/guitar_tuner_cpp/ui/guitar_tuner_cpp.ui" */
#define UI_FILE "src/guitar_tuner.ui"

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
	
	// Load the Glade file and instantiate its widgets:
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
	Gtk::Button* button = 0;
	
	builder->get_widget("button_E", button);
	button->signal_clicked().connect (sigc::bind<double, Sound*>(sigc::ptr_fun(&on_button_clicked),
	                                              329.63, &sound));
	builder->get_widget("button_A", button);
	button->signal_clicked().connect (sigc::bind<double, Sound*>(sigc::ptr_fun(&on_button_clicked),
	                                              440, &sound));
	builder->get_widget("button_D", button);
	button->signal_clicked().connect (sigc::bind<double, Sound*>(sigc::ptr_fun(&on_button_clicked),
	                                              587.33, &sound));
	builder->get_widget("button_G", button);
	button->signal_clicked().connect (sigc::bind<double, Sound*>(sigc::ptr_fun(&on_button_clicked),
	                                              783.99, &sound));
	builder->get_widget("button_B", button);
	button->signal_clicked().connect (sigc::bind<double, Sound*>(sigc::ptr_fun(&on_button_clicked),
	                                              987.77, &sound));
	builder->get_widget("button_e", button);
	button->signal_clicked().connect (sigc::bind<double, Sound*>(sigc::ptr_fun(&on_button_clicked),
	                                              1318.5, &sound));
	
	kit.run(*main_win);

	return 0;
}
