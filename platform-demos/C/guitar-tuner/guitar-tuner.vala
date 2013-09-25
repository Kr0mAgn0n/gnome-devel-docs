/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */

using GLib;
using Gtk;

public class Main : Object
{
	/*
	 * Uncomment this line when you are done testing and building a tarball
	 * or installing
	 */
	//const string UI_FILE = Config.PACKAGE_DATA_DIR + "/" + "guitar_tuner.ui";
	const string UI_FILE = "src/guitar_tuner.ui";

	Gst.Element sink;
	Gst.Element source;
	Gst.Pipeline pipeline;

	[CCode (instance_pos=-1)]
	public void on_button_clicked (Gtk.Button sender) {
		var label = sender.get_child () as Gtk.Label;
		switch (label.get_label()) {
			case "E":
				play_sound (329.63);
				break;
			case "A":
				play_sound (440);
				break;
			case "D":
				play_sound (587.33);
				break;
			case "G":
				play_sound (783.99);
				break;
			case "B":
				play_sound (987.77);
				break;
			case "e":
				play_sound (1318);
				break;
			default:
				break;
		}
	}

	public Main () {
		try
		{
			var builder = new Builder ();
			builder.add_from_file (UI_FILE);
			builder.connect_signals (this);

			var window = builder.get_object ("window") as Window;
			window.show_all ();
		}
		catch (Error e) {
			stderr.printf ("Could not load UI: %s\n", e.message);
		}
	}

	[CCode (instance_pos = -1)]
	public void on_destroy (Window window) {
		Gtk.main_quit();
	}

	private void play_sound(double frequency) {
		pipeline = new Gst.Pipeline ("note");
		source   = Gst.ElementFactory.make ("audiotestsrc",
		                                     "source");
		sink     = Gst.ElementFactory.make ("autoaudiosink",
		                                     "output");

		/* set frequency */
		source.set ("freq", frequency);

		pipeline.add (source);
		pipeline.add (sink);
		source.link (sink);

		pipeline.set_state (Gst.State.PLAYING);

		/* stop it after 200ms */
	    var time = new TimeoutSource(200);

		time.set_callback(() => {
			pipeline.set_state (Gst.State.NULL);
		    return false;
		});

		time.attach(null);
	}

	static int main (string[] args) {
		Gst.init (ref args);
		Gtk.init (ref args);
		var app = new Main ();

		Gtk.main ();

		return 0;
	}
}
