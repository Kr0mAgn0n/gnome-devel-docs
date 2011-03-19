/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */
using GLib;
using Gtk;

public class Main : Object 
{
	private Gtk.DrawingArea drawing_area;
	private Gst.Element camerabin;
	
	public Main () {
		this.drawing_area = new Gtk.DrawingArea ();
		this.drawing_area.set_size_request (640, 480);
		
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
