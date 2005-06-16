SOURCES=			\
	gnome-isv-guide.xml

IMAGES=					\

SOURCE_MAIN=gnome-isv-guide.xml

STYLESHEET=/usr/share/xml/docbook/stylesheet/nwalsh/current/html/onechunk.xsl

OUTPUTDIR=html

all: html.stamp

html.stamp: $(SOURCES) $(IMAGES)
	mkdir -p $(OUTPUTDIR)
	#cp $(IMAGES) $(OUTPUTDIR)
	xsltproc -o $(OUTPUTDIR)/ $(STYLESHEET) $(SOURCE_MAIN)
	touch html.stamp

clean:
	rm -f html.stamp
	rm -rf $(OUTPUTDIR)
	rm -f *~
