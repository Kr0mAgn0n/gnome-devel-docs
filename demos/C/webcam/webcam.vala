/*
 * Compile using:
 * valac --pkg gtk+-2.0 --pkg gdk-x11-2.0 --pkg gstreamer-0.10 --pkg gstreamer-interfaces-0.10 webcam.vala
 *
 */
using Gtk;
using Gst;

public class Webcam : Gtk.Window
{
  private Gtk.DrawingArea drawing_area;
  private X.ID xid;
  private Gst.Element camerabin;
  private int counter = 1;
  private bool playing;

  public Webcam ()
  {
    this.set_title ("Press play to start");
    this.destroy.connect (Gtk.main_quit);

    var vbox = new Gtk.VBox (false, 0);
    this.drawing_area = new Gtk.DrawingArea ();
    this.drawing_area.set_size_request (640, 480);
    this.drawing_area.realize.connect (on_realize);
    vbox.pack_start (this.drawing_area, true, true, 0);

    var play_button = new Button.from_stock (Gtk.STOCK_MEDIA_PLAY);
    play_button.clicked.connect (on_play);
    var pause_button = new Button.from_stock (Gtk.STOCK_MEDIA_PAUSE);
    pause_button.clicked.connect (on_pause);
    var photo_button = new Button.with_label ("Take a picture");
    photo_button.clicked.connect (on_take_picture);
    var stop_button = new Button.from_stock (Gtk.STOCK_MEDIA_STOP);
    stop_button.clicked.connect (on_stop);

    var button_box = new Gtk.HButtonBox ();
    button_box.add (play_button);
    button_box.add (pause_button);
    button_box.add (photo_button);
    button_box.add (stop_button);
    vbox.pack_start (button_box, false, true, 5);

    this.add (vbox);

    this.camerabin = Gst.ElementFactory.make ("camerabin", "camera");
    var bus = this.camerabin.get_bus ();
    bus.set_sync_handler (on_bus_callback);
  }

  private Gst.BusSyncReply on_bus_callback (Gst.Bus bus, Gst.Message message)
  {
    if (message.get_structure () != null && message.get_structure().has_name("prepare-xwindow-id")) {
      var xoverlay = message.src as Gst.XOverlay;
      xoverlay.set_xwindow_id (this.xid);
      return Gst.BusSyncReply.DROP;
    }

    return Gst.BusSyncReply.PASS;
  }

  private void on_realize ()
  {
    this.xid = Gdk.x11_drawable_get_xid (this.drawing_area.window);
    on_play ();
  }

  private void on_play ()
  {
    this.camerabin.set_state (Gst.State.PLAYING);
    this.playing = true;
  }

  private void on_pause ()
  {
    this.camerabin.set_state (Gst.State.PAUSED);
    this.playing = false;
  }

  private void on_stop ()
  {
    this.camerabin.set_state (Gst.State.NULL);
    this.playing = false;
  }

  private void on_take_picture ()
  {
    if (this.playing)
    {
      var filename = "photo" + "%d".printf (this.counter) + ".jpg";
      this.set_title ("%d".printf (this.counter) + " photos taken");
      this.counter++;
      this.camerabin.set ("filename", filename);
      GLib.Signal.emit_by_name (this.camerabin, "capture-start");
    }
  }

  public static int main (string[] args)
  {
    Gst.init (ref args);
    Gtk.init (ref args);

    var webcam = new Webcam ();
    webcam.show_all ();

    Gtk.main ();

    return 0;
  }
}
