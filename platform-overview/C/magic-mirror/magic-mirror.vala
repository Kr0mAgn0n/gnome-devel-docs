/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */
using GLib;
using Gtk;

public class Main : Object 
{
	private Gst.Element camerabin;
	
	public Main () {		
		this.camerabin = Gst.ElementFactory.make ("camerabin", "camera");
		this.camerabin.set_state (Gst.State.PLAYING);
	}
	
	static int main (string[] args) {
		Gtk.init (ref args);
		Gst.init (ref args);
		var app = new Main ();

		Gtk.main ();
		
		return 0;
	}
}
