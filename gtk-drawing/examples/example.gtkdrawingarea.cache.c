#include <math.h>
#include <gtk/gtk.h>

struct Context
{
	gboolean update_cache;
	GdkPixmap *cache;
};

static gboolean
expose_callback (GtkWidget *da, GdkEventExpose *event, gpointer user_data)
{
	struct Context *context = (struct Context *) user_data;

	if (context->update_cache)
	{
		int w, h;

		g_print ("Expose\n");

		if (context->cache) g_object_unref (context->cache);

		/* create a pixmap the same size as the window */
		gdk_drawable_get_size (event->window, &w, &h);
		context->cache = gdk_pixmap_new (event->window, w, h, -1);
	
		cairo_t *cr = gdk_cairo_create (context->cache);

		/* clear it to white */
		cairo_set_source_rgb (cr, 1., 1., 1.);
		cairo_paint (cr);

		/* draw a circle */
		cairo_set_source_rgb (cr, 0., 0., 0.);
		cairo_arc (cr, 50., 50., 25, -M_PI, M_PI);
		cairo_stroke (cr);

		cairo_destroy (cr);

		context->update_cache = FALSE;
	}
	else
	{
		g_print ("Expose from cache\n");
	}

	/* copy the cache to the window */
	GdkGC *gc = gdk_gc_new (event->window);
	gdk_draw_drawable (event->window, gc, context->cache,
			event->area.x, event->area.y,
			event->area.x, event->area.y,
			event->area.width, event->area.height);
	g_object_unref (gc);

	return TRUE;
}

static void
size_allocate (GtkWidget *da, GtkAllocation *allocation, gpointer user_data)
{
	struct Context *context = (struct Context *) user_data;

	g_print ("Resize, invalidate cache\n");

	/* mark the cache as requiring an update */
	context->update_cache = TRUE;
}

int
main (int argc, char **argv)
{
	struct Context context = { 0, };

	gtk_init (&argc, &argv);

	GtkWidget *window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
	GtkWidget *da = gtk_drawing_area_new ();

	gtk_container_add (GTK_CONTAINER (window), da);

	g_signal_connect_swapped (window, "delete-event",
			G_CALLBACK (gtk_main_quit), NULL);
	g_signal_connect (da, "expose-event",
			G_CALLBACK (expose_callback), &context);
	g_signal_connect (da, "size-allocate",
			G_CALLBACK (size_allocate), &context);

	gtk_widget_show_all (window);

	gtk_main ();
}
