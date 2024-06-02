<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:tei="http://www.tei-c.org/ns/1.0">
    <xsl:output method="html" indent="yes" encoding="UTF-8"/>
    
    <!-- Template to match the root element -->
    <xsl:template match="/">
        <html>
            <head>
                <title><xsl:value-of select="//tei:titleStmt/tei:title"/></title>
                <style>
                    body { font-family: Arial, sans-serif; margin: 30px; }
                    .metadata { border-bottom: 1px solid #ccc; padding-bottom: 10px; margin-bottom: 20px; }
                    .notes { display: block; margin-top: 15px; }
                    .note { display: block; margin-bottom: 20px; }
                    .footnote { font-size: smaller; margin-top: 30px; border-top: 1px solid #ccc; padding-top: 10px; }
                </style>
            </head>
            <body>
                <!-- Transforming teiHeader -->
                <div class="metadata">
                    <h1><xsl:value-of select="//tei:titleStmt/tei:title"/></h1>
                    <h3>Authored by: <xsl:value-of select="//tei:titleStmt/tei:author"/></h3>
                    <p><strong>Collection/ Book: </strong><xsl:value-of select="//tei:seriesStmt/tei:title"/>,  page <xsl:value-of select="//tei:seriesStmt/tei:biblScope[@unit='page']"/>.</p>
                    <p><strong>Edited by: </strong><xsl:value-of select="//tei:titleStmt/tei:editor[1]"/>, <xsl:value-of select="//tei:titleStmt/tei:editor[2]"/></p>
                    <p><strong>Publication: </strong> <xsl:value-of select="//tei:sourceDesc/tei:biblFull/tei:publicationStmt/tei:publisher"/>, <xsl:value-of select="//tei:sourceDesc/tei:biblFull/tei:publicationStmt/tei:pubPlace"/>. <xsl:value-of select="//tei:sourceDesc/tei:biblFull/tei:editionStmt/tei:p"/>.</p>
                    <p><strong>Open Library ID:</strong> <xsl:value-of select="//tei:publicationStmt/tei:idno[@type='openLibrary']"/> / <strong>ISBN: </strong><xsl:value-of select="//tei:seriesStmt/tei:idno[@type='ISBN']"/></p>
                    <p><strong>Availability:</strong> <a href="{//tei:publicationStmt/tei:availability/tei:licence/@target}">
                        <xsl:value-of select="//tei:publicationStmt/tei:availability/tei:licence/tei:p"/>
                    </a></p>
                    <p><strong>Notes:</strong></p>
                    <div class="notes">
                        <xsl:for-each select="//tei:notesStmt/tei:note">
                            <span class="note"><xsl:value-of select="."/></span>
                        </xsl:for-each>
                    </div>
                </div>

                <!-- Transforming the poem -->
                <div id="poem">
                    <h2>Ozymandias</h2>
                    <xsl:apply-templates select="//tei:lg[@type='poem']"/>
                </div>

                 <!-- Footnote for projectDesc -->
                <div class="footnote">
                    <p><strong>Project Description:</strong> <xsl:value-of select="//tei:encodingDesc/tei:projectDesc/tei:p"/></p>
                </div>
            </body>
        </html>
    </xsl:template>

    <!-- Template to match the lg (poem) element -->
    <xsl:template match="tei:lg[@type='poem']">
        <p>
            <xsl:apply-templates/>
        </p>
    </xsl:template>

    <!-- Template to match the l (line) element -->
    <xsl:template match="tei:l">
        <xsl:value-of select="."/>
        <br/>
    </xsl:template>

    <!-- Template to match the emph (italic) element -->
    <xsl:template match="tei:emph">
        <i>
            <xsl:apply-templates/>
        </i>
    </xsl:template>

</xsl:stylesheet>
