#include <math.h>
#include <gtk/gtk.h>

#define SLICE_WIDTH 6
#define RADIUS 30

static gboolean
expose_callback (GtkWidget *da, GdkEventExpose *event, gpointer user_data)
{
	cairo_t *cr = gdk_cairo_create (event->window);
	int *alpha = (int *) user_data;

	cairo_translate (cr, da->allocation.width / 2,
			     da->allocation.height / 2);

	cairo_save (cr); /* pie slice */

	cairo_rotate (cr, M_PI / SLICE_WIDTH * *alpha);
	cairo_set_source_rgb (cr, 0.5, 0.5, 1.0);

	cairo_move_to (cr, 0, 0);
	cairo_arc (cr, 0, 0, RADIUS, 0, M_PI / SLICE_WIDTH);
	cairo_close_path (cr);
	cairo_fill (cr);

	cairo_restore (cr); /* pie slice */
	
	cairo_arc (cr, 0, 0, RADIUS, -M_PI, M_PI);
	cairo_stroke (cr);

	cairo_destroy (cr);

	return TRUE;
}

static gboolean
animate_cb (gpointer user_data)
{
	GtkWidget *da = GTK_WIDGET (((GtkWidget **) user_data)[1]);
	int *alpha = ((int **) user_data)[2];

	*alpha = (*alpha + 1) % (SLICE_WIDTH * 2);

	gdk_window_invalidate_rect (da->window, NULL, FALSE);

	return TRUE;
}

static void
animate_toggled (GtkToggleButton *toggle, gpointer user_data)
{
	guint *source = ((guint **) user_data)[0];

	if (gtk_toggle_button_get_active (toggle))
	{
		/* animate */
		*source = g_timeout_add (1000 / 30, animate_cb, user_data);
	}
	else
	{
		/* cancel animation */
		g_source_remove (*source);
		*source = 0;
	}
}

int
main (int argc, char **argv)
{
	gtk_init (&argc, &argv);

	GtkWidget *window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
	GtkWidget *vbox = gtk_vbox_new (FALSE, 6);
	GtkWidget *toggle = gtk_toggle_button_new_with_label ("Animate");
	GtkWidget *da = gtk_drawing_area_new ();

	gtk_container_add (GTK_CONTAINER (window), vbox);
	gtk_box_pack_start (GTK_BOX (vbox), toggle, FALSE, FALSE, 0);
	gtk_box_pack_start (GTK_BOX (vbox), da, TRUE, TRUE, 0);

	/* prepare the user_data - in a real program, this would probably
	 * be a struct */
	gpointer user_data[3];
	guint timeout_source;
	int alpha = 0;
	user_data[0] = &timeout_source;
	user_data[1] = da;
	user_data[2] = &alpha;

	g_signal_connect (toggle, "toggled",
			G_CALLBACK (animate_toggled), user_data);

	g_signal_connect_swapped (window, "delete-event",
			G_CALLBACK (gtk_main_quit), NULL);
	g_signal_connect (da, "expose-event",
			G_CALLBACK (expose_callback), &alpha);

	gtk_window_set_default_size (GTK_WINDOW (window), 200, 200);
	gtk_widget_show_all (window);

	gtk_main ();
}
