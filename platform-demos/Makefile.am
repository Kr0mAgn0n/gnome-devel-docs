include $(top_srcdir)/gnome-doc-utils.make

DOC_ID = gnome-devel-demos

DOC_LINGUAS = de es gl

demo_sources = \
	guitar-tuner/guitar-tuner.c \
	guitar-tuner/guitar-tuner.cc \
	guitar-tuner/guitar-tuner.py \
	guitar-tuner/guitar-tuner.vala \
	image-viewer/image-viewer.c \
	image-viewer/image-viewer.cc \
	image-viewer/image-viewer.py \
	image-viewer/image-viewer.js \
	magic-mirror/magic-mirror.vala \
	magic-mirror/magic-mirror-advanced.vala \
	message-board/message-board.c \
	photo-wall/photo-wall.c \
	record-collection/record-collection.js \
	gnome-devtools.catalog
	

DOC_FIGURES = \
	media/ubuntu.png			\
	media/fedora.png			\
	media/opensuse.png			\
	media/guitar-tuner.png			\
	media/guitar-tuner-glade.png		\
	media/guitar-tuner-pipeline.png		\
	media/image-viewer.png			\
	media/photo-wall.png			\
	media/record-collection.png		\
	media/magic-mirror.png			\
	$(demo_sources)

DOC_ENTITIES =

DOC_PAGES =			\
	getting-ready.page	\
	guitar-tuner.c.page	\
	guitar-tuner.cpp.page   \
	guitar-tuner.py.page    \
	guitar-tuner.vala.page  \
	image-viewer.c.page	\
	image-viewer.cpp.page   \
	image-viewer.py.page    \
	image-viewer.js.page	\
	magic-mirror.vala.page	\
	message-board.c.page	\
	photo-wall.c.page	\
	record-collection.js.page	\
	index.page

dist-hook: doc-dist-hook
