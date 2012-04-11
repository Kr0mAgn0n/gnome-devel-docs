using Gtk;

void on_response (int response_id) {

	/*To see the int value of the ResponseType*/
	print ("response is %d\n", response_id);
	
	main_quit ();
}
int main (string[] args) {

	init (ref args);

	var dialog = new Dialog.with_buttons ("A Gtk+ Dialog", null, 0, Stock.OK, ResponseType.OK, null);
	var content_area = dialog.get_content_area ();
	var label = new Label ("This demonstrates a dialog with a label");
	
	content_area.add (label);
	dialog.response.connect (on_response);
	dialog.show_all ();

	Gtk.main ();
	return 0;
}
