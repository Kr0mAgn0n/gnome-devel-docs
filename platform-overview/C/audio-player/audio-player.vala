/*
 * Compile using:
 * valac --pkg gtk+-2.0 --pkg gstreamer-0.10 audio-player.vala
 *
 */

using Gtk;
using Gst;

public class AudioPlayer : Gtk.Window
{
  private Gst.Element playbin;
  private string[] files;
  private Gtk.Label label;
  private int song = 0;
  private bool playing;
  private Gtk.Button play_pause_button;

  public AudioPlayer ()
  {
    this.set_size_request (600, 200);
    this.destroy.connect (Gtk.main_quit);
    var vbox = new Gtk.VBox (false, 0);
    this.label = new Gtk.Label ("Audio Player");
    vbox.pack_start (this.label, true, true, 0);

    this.play_pause_button = new Gtk.Button.from_stock (Gtk.STOCK_MEDIA_PLAY);
    this.play_pause_button.clicked.connect (on_play_pause);
    var next_button = new Gtk.Button.from_stock (Gtk.STOCK_MEDIA_NEXT);
    next_button.clicked.connect (on_next);

    var button_box = new Gtk.HButtonBox ();
    button_box.add (this.play_pause_button);
    button_box.add (next_button);
    vbox.pack_start (button_box, false, true, 0);

    this.add (vbox);

    this.playbin = Gst.ElementFactory.make ("playbin", "play");
  }

  private void on_play_pause ()
  {
    if (this.playing)
    {
      this.playbin.set_state (Gst.State.PAUSED);
      this.play_pause_button.set_label (Gtk.STOCK_MEDIA_PAUSE);
    }
    else
    {
      this.playbin.set_state (Gst.State.PLAYING);
      this.play_pause_button.set_label (Gtk.STOCK_MEDIA_PLAY);
    }

    this.playing = !this.playing;
  }

  private void on_next ()
  {
    this.playbin.set_state (Gst.State.NULL);
    this.playbin.set ("uri", "file://" + this.files[song]);
    this.label.set_text (this.files[song]);
    this.song++;
    if (this.files.length <= this.song)
    {
      this.song = 0;
    }
    this.playbin.set_state (Gst.State.PLAYING);
    this.play_pause_button.set_label (Gtk.STOCK_MEDIA_PLAY);
    this.playing = true;
  }

  public static int main (string[] args)
  {
    Gst.init (ref args);
    Gtk.init (ref args);

    if (args.length < 2)
    {
      print ("usage: audio-player [files...]\n");
      return 1;
    }

    var audio_player = new AudioPlayer ();
    audio_player.files = args[1:args.length];
    audio_player.show_all ();
    audio_player.on_next ();
    Gtk.main ();

    return 0;
  }
}
