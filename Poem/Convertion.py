# This is the Python script for XML/TEI to HTML
# NB. .xml and .xsl files must be in the same directory for the transformation to be performed!

from lxml import etree

tei_data = etree.parse("TEI.xml")
xslt_data = etree.parse("Style.xslt")

transform = etree.XSLT(xslt_data)
result_tree = transform(tei_data)

with open("Ozymandias.html", "wb") as f:
    f.write(etree.tostring(result_tree, pretty_print=True))