#include <gtk/gtk.h>
#include <gtk/gtkgl.h>

#include <GL/gl.h>

static gboolean
configure_callback (GtkWidget *da, GdkEventConfigure *event, gpointer user_data)
{
	g_print ("Configure\n");
	GdkGLContext *glcontext = gtk_widget_get_gl_context (da);
	GdkGLDrawable *gldrawable = gtk_widget_get_gl_drawable (da);

	if (!gdk_gl_drawable_gl_begin (gldrawable, glcontext))
	{
		g_assert_not_reached ();
	}

	/* set the OpenGL Viewport */

	gdk_gl_drawable_gl_end (gldrawable);

	return TRUE;
}

static gboolean
expose_callback (GtkWidget *da, GdkEventExpose *event, gpointer user_data)
{
	g_print ("Expose\n");
	GdkGLContext *glcontext = gtk_widget_get_gl_context (da);
	GdkGLDrawable *gldrawable = gtk_widget_get_gl_drawable (da);

	if (!gdk_gl_drawable_gl_begin (gldrawable, glcontext))
	{
		g_assert_not_reached ();
	}

	/* clear */
	glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

	/* drawing code goes here */

	/* flush */
	if (gdk_gl_drawable_is_double_buffered (gldrawable))
		gdk_gl_drawable_swap_buffers (gldrawable);
	else
		glFlush ();

	gdk_gl_drawable_gl_end (gldrawable);

	return TRUE;
}

int
main (int argc, char **argv)
{
	gtk_init (&argc, &argv);

	GtkWidget *window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
	GtkWidget *da = gtk_drawing_area_new ();

	gtk_container_add (GTK_CONTAINER (window), da);

	g_signal_connect_swapped (window, "delete-event",
			G_CALLBACK (gtk_main_quit), NULL);

	GdkGLConfig *glconfig = gdk_gl_config_new_by_mode (
			GDK_GL_MODE_RGB |
			GDK_GL_MODE_DEPTH |
			GDK_GL_MODE_DOUBLE);

	if (!glconfig) g_assert_not_reached ();

	if (!gtk_widget_set_gl_capability (da, glconfig, NULL, TRUE,
				GDK_GL_RGBA_TYPE))
	{
		g_assert_not_reached ();
	}

	g_signal_connect (da, "configure-event",
			G_CALLBACK (configure_callback), NULL);
	g_signal_connect (da, "expose-event",
			G_CALLBACK (expose_callback), NULL);

	/* the window must be shown before we can do anything with GL */
	gtk_widget_show_all (window);

	g_print ("Setup\n");
	GdkGLContext *glcontext = gtk_widget_get_gl_context (da);
	GdkGLDrawable *gldrawable = gtk_widget_get_gl_drawable (da);

	if (!gdk_gl_drawable_gl_begin (gldrawable, glcontext))
	{
		g_assert_not_reached ();
	}

	/* setup fixed items for OpenGL */

	gdk_gl_drawable_gl_end (gldrawable);

	gtk_main ();
}
