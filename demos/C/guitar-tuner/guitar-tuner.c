/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */
/*
 * main.c
 * Copyright (C) Johannes Schmid 2010 <jhs@gnome.org>
 * 
 * guitar-tuner is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * guitar-tuner is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License along
 * with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <config.h>
#include <gtk/gtk.h>
#include <gst/gst.h>
#include <glib/gi18n.h>

/* For testing propose use the local (not installed) ui file */
/* #define UI_FILE PACKAGE_DATA_DIR"/guitar_tuner/ui/guitar_tuner.ui" */
#define UI_FILE "src/guitar_tuner.ui"

/* Frequencies of the tones */
#define NOTE_E 369.23
#define NOTE_A 440
#define NOTE_D 587.33
#define NOTE_G 783.99
#define NOTE_B 987.77
#define NOTE_e 1318.5

#define LENGTH 500

#define WIDGET_WINDOW "window"

static gboolean
pipeline_stop (GstElement* pipeline)
{
	gst_element_set_state (pipeline, GST_STATE_PAUSED);
	g_object_unref (pipeline);

	/* disconnect handler */
	return FALSE;
}

static void 
play_sound (gdouble frequency)
{
	GstElement *source, *sink;
	GstElement *pipeline;

	pipeline = gst_pipeline_new ("note");
	source   = gst_element_factory_make ("audiotestsrc",
	                                     "source");
	sink     = gst_element_factory_make ("autoaudiosink",
	                                     "output");

	/* set frequency */
	g_object_set (source, "freq", frequency, NULL);
	
	gst_bin_add_many (GST_BIN (pipeline), source, sink, NULL);
	gst_element_link (source, sink);

	gst_element_set_state (pipeline, GST_STATE_PLAYING);

	/* stop it after 200ms */
	g_timeout_add (LENGTH, (GSourceFunc) pipeline_stop, pipeline);
}

/* Callback for the buttons */
void on_button_clicked (GtkButton* button,
                        gpointer user_data)
{
	GtkWidget* label = gtk_bin_get_child (GTK_BIN (button));
	const gchar* text = gtk_label_get_label (GTK_LABEL (label));

	if (g_str_equal (text, _("E")))
	    play_sound (NOTE_E);
	else if (g_str_equal (text, _("A")))
	    play_sound (NOTE_A);
	else if (g_str_equal (text, _("G")))
	    play_sound (NOTE_G);
	else if (g_str_equal (text, _("D")))
	    play_sound (NOTE_D);
	else if (g_str_equal (text, _("B")))
	    play_sound (NOTE_B);
	else if (g_str_equal (text, _("e")))
	    play_sound (NOTE_e);
}

int
main (int argc, char *argv[])
{
 	GtkWidget *window;
	GtkBuilder *builder;

	
	/* Initialize gtk+ and gstreamer */
	gtk_init (&argc, &argv);
	gst_init (&argc, &argv);

	builder = gtk_builder_new ();
	gtk_builder_add_from_file (builder, UI_FILE, NULL);

	window = GTK_WIDGET (gtk_builder_get_object (builder, WIDGET_WINDOW));
	gtk_builder_connect_signals (builder, NULL);
	
	gtk_widget_show (window);

	gtk_main ();
	return 0;
}
