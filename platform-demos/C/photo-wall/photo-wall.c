#include <gdk-pixbuf/gdk-pixbuf.h>
#include <clutter/clutter.h>

#define STAGE_WIDTH  800
#define STAGE_HEIGHT 600

#define THUMBNAIL_SIZE 200
#define ROW_COUNT (STAGE_HEIGHT / THUMBNAIL_SIZE)
#define COL_COUNT (STAGE_WIDTH  / THUMBNAIL_SIZE)
#define THUMBNAIL_COUNT (ROW_COUNT * COL_COUNT)

#define ANIMATION_DURATION_MS 500

#define IMAGE_DIR_PATH "./berlin_images/"

static GPtrArray *img_paths;

static ClutterPoint unfocused_pos;

static void
load_image_path_names()
{
    /* Ensure we can access the directory. */
    GError *error = NULL;
    GDir *dir = g_dir_open(IMAGE_DIR_PATH, 0, &error);
    if(error)
    {
        g_warning("g_dir_open() failed with error: %s\n", error->message);
        g_clear_error(&error);
        return;
    }

    img_paths = g_ptr_array_new_with_free_func (g_free);

    const gchar *filename = g_dir_read_name(dir);
    while(filename)
    {
        if(g_str_has_suffix(filename, ".jpg") || g_str_has_suffix(filename, ".png")) 
        {
            gchar *path = g_build_filename(IMAGE_DIR_PATH, filename, NULL);
            g_ptr_array_add (img_paths, path);
        }
        filename = g_dir_read_name(dir);
    }
}

static gboolean
actor_clicked_cb(ClutterActor *actor,
                 ClutterEvent *event,
                 gpointer      user_data)
{
    /* Flag to keep track of our state. */
    static gboolean is_focused = FALSE;
    ClutterActorIter iter;
    ClutterActor *child;

    /* Reset the focus state on all the images */
    clutter_actor_iter_init (&iter, clutter_actor_get_parent(actor));
    while (clutter_actor_iter_next(&iter, &child))
      clutter_actor_set_reactive(child, is_focused);

    clutter_actor_save_easing_state(actor);
    clutter_actor_set_easing_duration(actor, ANIMATION_DURATION_MS);

    if(is_focused)
    {
        /* Restore the old location and size. */
        clutter_actor_set_position(actor, unfocused_pos.x, unfocused_pos.y);
        clutter_actor_set_size(actor, THUMBNAIL_SIZE, THUMBNAIL_SIZE);
    }
    else
    {
        /* Save the current location before animating. */
        clutter_actor_get_position(actor, &unfocused_pos.x, &unfocused_pos.y);

        /* Only the currently focused image should receive to events. */
        clutter_actor_set_reactive(actor, TRUE);

        /* Put the focused image on top. */
        clutter_actor_set_child_above_sibling(clutter_actor_get_parent(actor), actor, NULL);

        clutter_actor_set_position(actor, (STAGE_WIDTH - STAGE_HEIGHT) / 2.0, 0);
        clutter_actor_set_size(actor, STAGE_HEIGHT, STAGE_HEIGHT);
    }

    clutter_actor_restore_easing_state(actor);

    /* Toggle our flag. */
    is_focused = !is_focused;

    return TRUE;
}

/* This function handles setting up and placing the rectangles. */
static void
initialize_actor(ClutterActor *actor, guint row, guint col)
{
    clutter_actor_set_size(actor, THUMBNAIL_SIZE, THUMBNAIL_SIZE);
    clutter_actor_set_position(actor, col * THUMBNAIL_SIZE, row * THUMBNAIL_SIZE);
    clutter_actor_set_reactive(actor, TRUE);

    g_signal_connect(actor,
                     "button-press-event",
                     G_CALLBACK(actor_clicked_cb),
                     NULL);
}

int
main(int argc, char *argv[])
{
    ClutterColor stage_color = { 16, 16, 16, 255 };
    ClutterActor *stage = NULL;

    if (clutter_init (&argc, &argv) != CLUTTER_INIT_SUCCESS)
        return 1;

    stage = clutter_stage_new();
    clutter_actor_set_size(stage, STAGE_WIDTH, STAGE_HEIGHT);
    clutter_actor_set_background_color(stage, &stage_color);
    clutter_stage_set_title(CLUTTER_STAGE (stage), "Photo Wall");
    g_signal_connect(stage, "destroy", G_CALLBACK(clutter_main_quit), NULL);

    load_image_path_names();

    guint row = 0;
    guint col = 0;
    for(row=0; row < ROW_COUNT; ++row)
    {
        for(col=0; col < COL_COUNT; ++col)
        {
            const char *img_path = g_ptr_array_index(img_paths, (row * COL_COUNT) + col);
            GdkPixbuf *pixbuf = gdk_pixbuf_new_from_file_at_size(img_path, STAGE_HEIGHT, STAGE_HEIGHT, NULL);
            ClutterContent *image = clutter_image_new ();
            ClutterActor *actor = clutter_actor_new ();

            if (pixbuf != NULL)
            {
                clutter_image_set_data(CLUTTER_IMAGE(image),
                                       gdk_pixbuf_get_pixels(pixbuf),
                                       gdk_pixbuf_get_has_alpha(pixbuf)
                                           ? COGL_PIXEL_FORMAT_RGBA_8888
                                           : COGL_PIXEL_FORMAT_RGB_888,
                                       gdk_pixbuf_get_width(pixbuf),
                                       gdk_pixbuf_get_height(pixbuf),
                                       gdk_pixbuf_get_rowstride(pixbuf),
                                       NULL);
            }

            clutter_actor_set_content(actor, image);
            g_object_unref(image);
            g_object_unref(pixbuf);

            initialize_actor(actor, row, col);
            clutter_actor_add_child(stage, actor);
        }
    }

    /* Show the stage. */
    clutter_actor_show(stage);

    /* Start the clutter main loop. */
    clutter_main();

    g_ptr_array_unref(img_paths);

    return 0;
}
