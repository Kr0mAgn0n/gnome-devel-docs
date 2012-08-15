# The actual runnable program is set to the SCRIPTS primitive.
# # Prefix bin_ tells where to copy this
bin_PROGRAMS = hello-world
hello_world_CFLAGS = $(gtk_CFLAGS)
hello_world_LDADD = $(gtk_LIBS)
hello_world_VALAFLAGS = --pkg gtk+-3.0
hello_world_SOURCES = hello-world.vala

desktopdir = $(datadir)/applications
desktop_DATA = \
	hello-world.desktop
