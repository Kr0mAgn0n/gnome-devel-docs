/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */
/*
 * main.c
 * Copyright (C) Johannes Schmid 2011 <jhs@idefix>
 * 
 * guitar-tuner-vala is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * guitar-tuner-vala is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License along
 * with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

using GLib;
using Gtk;

public class Main : Object 
{
	/* 
	 * Uncomment this line when you are done testing and building a tarball
	 * or installing
	 */
	//const string UI_FILE = Config.PACKAGE_DATA_DIR + "/" + "guitar_tuner_vala.ui";
	const string UI_FILE = "src/guitar_tuner_vala.ui";

	Gst.Element sink;
	Gst.Element source;
	Gst.Pipeline pipeline;
	
	[CCode (instance_pos=-1)]
	public void on_button_clicked (Gtk.Button sender) {
		var label = sender.get_child () as Gtk.Label;
		switch (label.get_label()) {
			case "E":
				play_sound (369.23);
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
			pipeline.set_state (Gst.State.PAUSED);
			pipeline.unref();
		    return false;
		});

		time.attach(null);
	}
		
	static int main (string[] args) {
		Gtk.init (ref args);
		Gst.init (ref args);
		var app = new Main ();

		Gtk.main ();
		
		return 0;
	}
}
