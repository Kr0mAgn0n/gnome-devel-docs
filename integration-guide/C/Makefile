SOURCES=			\
	gnome-isv-guide.xml

IMAGES=					\

SOURCE_MAIN=gnome-isv-guide.xml

CSS=docbook.css

STYLESHEET=/usr/share/xml/docbook/stylesheet/nwalsh/xhtml/onechunk.xsl
#STYLESHEET=/usr/share/xml/docbook/stylesheet/nwalsh/html/onechunk.xsl
#STYLESHEET=/usr/share/sgml/docbook/xsl-stylesheets-1.65.1-2/xhtml/onechunk.xsl
#STYLESHEET=/usr/share/yelp/xslt/db2html.xsl

OUTPUTDIR=html

all: html.stamp

html.stamp: $(SOURCES) $(IMAGES)
	mkdir -p $(OUTPUTDIR)
	#cp $(IMAGES) $(OUTPUTDIR)
	xsltproc -o $(OUTPUTDIR)/ --stringparam html.stylesheet $(CSS) $(STYLESHEET) \
		$(SOURCE_MAIN)
	cp $(CSS) $(OUTPUTDIR)/
	touch html.stamp

clean:
	rm -f html.stamp
	rm -rf $(OUTPUTDIR)
	rm -f *~
