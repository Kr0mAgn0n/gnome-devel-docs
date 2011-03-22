#include <clutter/clutter.h>

#define STAGE_WIDTH  800
#define STAGE_HEIGHT 600

#define THUMBNAIL_SIZE 200
#define ROW_COUNT (STAGE_HEIGHT / THUMBNAIL_SIZE)
#define COL_COUNT (STAGE_WIDTH  / THUMBNAIL_SIZE)
#define THUMBNAIL_COUNT (ROW_COUNT * COL_COUNT)

#define ANIMATION_DURATION_MS 500

#define FOCUS_DEPTH 100.0
#define UNFOCUS_DEPTH 0.0

#define IMAGE_DIR_PATH "./berlin_images/"

static GSList *actor_list = NULL;
static GSList *img_path_list = NULL;

typedef struct Position
{
    float x;
    float y;
}
Position;

static Position origin = {0, 0};

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

    const gchar *filename = g_dir_read_name(dir);
    while(filename)
    {
        if(g_str_has_suffix(filename, ".jpg") || g_str_has_suffix(filename, ".png")) 
        {
            gchar *path = g_build_filename(IMAGE_DIR_PATH, filename, NULL);
            img_path_list = g_slist_prepend(img_path_list, path);
        }
        filename = g_dir_read_name(dir);
    }
}

static void
foreach_set_focus_state(gpointer data, gpointer user_data)
{
    ClutterActor *actor = CLUTTER_ACTOR(data);
    gboolean is_reactive = *((gboolean*)user_data);

    clutter_actor_set_reactive(actor, is_reactive);
}

static gboolean
actor_clicked_cb(ClutterActor *actor,
                 ClutterEvent *event,
                 gpointer      user_data)
{
    /* Flag to keep track of our state. */
    static gboolean is_focused = FALSE;

    g_slist_foreach(actor_list, foreach_set_focus_state, &is_focused);

    if(is_focused)
    {
        clutter_actor_animate(actor, CLUTTER_LINEAR, ANIMATION_DURATION_MS,
                              "x",      origin.x,
                              "y",      origin.y,
                              "depth",  UNFOCUS_DEPTH,
                              "width",  (float) THUMBNAIL_SIZE,
                              "height", (float) THUMBNAIL_SIZE,
                              NULL);
    }
    else
    {
        /*Save the current location before animating. */
        clutter_actor_get_position(actor, &origin.x, &origin.y);
        clutter_actor_set_reactive(actor, TRUE);
        clutter_actor_animate(actor, CLUTTER_LINEAR, ANIMATION_DURATION_MS,
                              "x",      (STAGE_WIDTH - STAGE_HEIGHT) / 2.0,
                              "y",      0.0,
                              "depth",  FOCUS_DEPTH,
                              "width",  (float) STAGE_HEIGHT,
                              "height", (float) STAGE_HEIGHT,
                              NULL);
    }

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

    clutter_init (&argc, &argv);

    stage = clutter_stage_get_default();
    clutter_actor_set_size(stage, STAGE_WIDTH, STAGE_HEIGHT);
    clutter_stage_set_color(CLUTTER_STAGE (stage), &stage_color);

    load_image_path_names();

    guint row = 0;
    guint col = 0;
    for(row=0; row < ROW_COUNT; ++row)
    {
        for(col=0; col < COL_COUNT; ++col)
        {
            GSList *img_path_node = g_slist_nth(img_path_list, (row * COL_COUNT) + col);
            ClutterActor *actor = clutter_texture_new_from_file((gchar *)(img_path_node->data), NULL);
            initialize_actor(actor, row, col);
            clutter_container_add_actor(CLUTTER_CONTAINER(stage), actor);
            actor_list = g_slist_prepend(actor_list, actor);
        }
    }

    /* Show the stage. */
    clutter_actor_show(stage);

    /* Start the clutter main loop. */
    clutter_main();

    return 0;
}
