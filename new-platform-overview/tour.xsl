<!--
This will collect all of the code snippets from the tour and output them to tour-summary.js which is included in tour-summary.page.
Run with this line:
xsltproc -o tour-summary.js tour.xsl tour-intro.page
-->
<xsl:stylesheet
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:mal="http://projectmallard.org/1.0/"
  version="1.0">

<xsl:output method="text"/>

<xsl:template match="/mal:page">
  <xsl:variable name="next" select="mal:info/mal:link[@type='next']"/>
  <xsl:if test="$next">
    <xsl:for-each select="mal:code | .//mal:section/mal:code | .//mal:listing/mal:code">
      <xsl:value-of select="."/>
    </xsl:for-each>
    <xsl:apply-templates select="document(concat($next/@xref, '.page'))/mal:page"/>
  </xsl:if>
</xsl:template>

</xsl:stylesheet>

