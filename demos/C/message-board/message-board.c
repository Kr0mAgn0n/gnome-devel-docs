/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */
/*
 * main.c
 * Copyright (C) Shaun McCance 2010 <shaunm@gnome.org>
 * 
 * message-board is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * message-board is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License along
 * with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <config.h>
#include <gtk/gtk.h>
#include <webkit/webkit.h>


#include <glib/gi18n.h>


/* For testing propose use the local (not installed) ui file */
/* #define UI_FILE PACKAGE_DATA_DIR"/message_board/ui/message_board.ui" */
#define UI_FILE "src/message_board.ui"

/* Signal handlers */
/* Note: These may not be declared static because signal autoconnection
 * only works with non-static methods
 */

static const guchar CSS[] =
"body { margin: 0; padding: 0; }\n"
"div { "
" -webkit-border-radius: 2px;"
" background: -webkit-gradient(linear, 0% 100%, 0% 0%,"
" from(#f1f1f1), to(white));"
" border: solid 1px #c6c6c6;"
" -webkit-box-shadow: 0px 0px 2px #c6c6c6;"
" margin: 12px; padding: 6px;"
"}";

/* Called when the window is closed */
void
destroy (GtkWidget *widget, gpointer data)
{
	gtk_main_quit ();
}

static void
entry_activate_cb (GtkEntry *entry, WebKitWebView *view)
{
	WebKitDOMDocument *document;
	WebKitDOMElement *body, *div;

	document = webkit_web_view_get_dom_document (view);
	body = webkit_dom_document_query_selector (document,
	                                           "body",
	                                           NULL);
	div = webkit_dom_document_create_element (document,
	                                          "div",
	                                          NULL);
	webkit_dom_node_set_text_content (WEBKIT_DOM_NODE (div),
	                                  gtk_entry_get_text (entry),
	                                  NULL);
	webkit_dom_node_append_child (WEBKIT_DOM_NODE (body),
	                              WEBKIT_DOM_NODE (div),
	                              NULL);
	gtk_entry_set_text (entry, "");
}

static GtkWidget*
create_window (void)
{
    GtkWidget *window, *box, *scroll, *view, *entry;
	gchar *tmp, *css;

    window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
    gtk_window_set_default_size (GTK_WINDOW (window), 400, 400);
    gtk_window_set_title (GTK_WINDOW (window), "Message Board");
	g_signal_connect (window, "delete-event",
	                  G_CALLBACK (destroy), NULL);

    box = gtk_box_new (GTK_ORIENTATION_VERTICAL, 6);
    gtk_container_set_border_width (GTK_CONTAINER (box), 6);
    gtk_container_add (GTK_CONTAINER (window), box);

    entry = gtk_entry_new ();
    gtk_box_pack_start (GTK_BOX (box), entry, FALSE, FALSE, 0);

    scroll = gtk_scrolled_window_new (NULL, NULL);
	g_object_set (scroll, "shadow-type", GTK_SHADOW_IN, NULL);
    gtk_box_pack_start (GTK_BOX (box), scroll, TRUE, TRUE, 0);

    view = webkit_web_view_new ();
    gtk_container_add (GTK_CONTAINER (scroll), view);
    webkit_web_view_load_string (WEBKIT_WEB_VIEW (view),
	                             "<html><body></body></html>",
	                             "text/html",
	                             "UTF-8",
	                             NULL);

	tmp = g_base64_encode (CSS, strlen((gchar *) CSS));
	css = g_strconcat ("data:text/css;charset=utf-8;base64,",
	                   tmp, NULL);
	g_object_set (webkit_web_view_get_settings (WEBKIT_WEB_VIEW (view)),
	              "user-stylesheet-uri", css, NULL);
	g_free (css);
	g_free (tmp);

	g_signal_connect (entry, "activate",
	                  G_CALLBACK (entry_activate_cb), view);

	gtk_widget_show_all (GTK_WIDGET (box));
	return window;
}

int
main (int argc, char *argv[])
{
 	GtkWidget *window;


#ifdef ENABLE_NLS
	bindtextdomain (GETTEXT_PACKAGE, PACKAGE_LOCALE_DIR);
	bind_textdomain_codeset (GETTEXT_PACKAGE, "UTF-8");
	textdomain (GETTEXT_PACKAGE);
#endif

	
	gtk_set_locale ();
	gtk_init (&argc, &argv);

	window = create_window ();
	gtk_widget_show (window);

	gtk_main ();
	return 0;
}
