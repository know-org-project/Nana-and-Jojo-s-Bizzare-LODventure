import xml.etree.ElementTree as ET
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import RDF, DC, FOAF, RDFS, DCTERMS, XSD

TEI = Namespace("http://www.tei-c.org/ns/1.0/")

# parsing the XML file
tree = ET.parse(r'C:\Users\Эльвира\Downloads\TEI.xml')  # adjust the path 
root = tree.getroot()

# creating an RDF graph
g = Graph()

# extracting title and author
title = root.find('.//{http://www.tei-c.org/ns/1.0}title').text
author = root.find('.//{http://www.tei-c.org/ns/1.0}author').text

# Create URIs for resources
poem_uri = URIRef("https://github.com/know-org-project/Nana-and-Jojo-s-Bizzare-LODventure/poem/ozymandias")
author_uri = URIRef("https://github.com/know-org-project/Nana-and-Jojo-s-Bizzare-LODventure/poem/author/Percy_Bysshe_Shelley")

# adding basic triples to the graph
g.add((poem_uri, RDF.type, TEI['Poem']))
g.add((poem_uri, DC.title, Literal(title)))
g.add((poem_uri, DC.creator, author_uri))
g.add((author_uri, RDF.type, FOAF.Person))
g.add((author_uri, FOAF.name, Literal(author)))

# extracting book name, edition, and notes
book_name = root.find('.//{http://www.tei-c.org/ns/1.0}seriesStmt/{http://www.tei-c.org/ns/1.0}title').text
edition = root.find('.//{http://www.tei-c.org/ns/1.0}editionStmt/{http://www.tei-c.org/ns/1.0}p').text
notes = [note.text for note in root.findall('.//{http://www.tei-c.org/ns/1.0}note')]
isbn = root.find('.//{http://www.tei-c.org/ns/1.0}seriesStmt/{http://www.tei-c.org/ns/1.0}idno[@type="ISBN"]').text

# Adding book name, edition, notes, and ISBN to the graph
book_uri = URIRef("https://github.com/know-org-project/Nana-and-Jojo-s-Bizzare-LODventure/book/" + book_name.replace(" ", "_"))
g.add((book_uri, DC.title, Literal(book_name)))
g.add((poem_uri, DCTERMS.isPartOf, book_uri))  
g.add((book_uri, DCTERMS.hasVersion, Literal(edition)))  # edition is displayed
g.add((book_uri, DC.identifier, Literal(isbn)))

for index, note in enumerate(notes):
    note_uri = URIRef(f"https://github.com/know-org-project/Nana-and-Jojo-s-Bizzare-LODventure/note/{index + 1}")
    g.add((note_uri, RDF.type, RDFS.Literal))
    g.add((note_uri, RDFS.comment, Literal(note)))
    g.add((poem_uri, DC.description, note_uri))

# adding editors
editors = root.findall('.//{http://www.tei-c.org/ns/1.0}editor')
for editor in editors:
    editor_name = editor.text
    editor_uri = URIRef(f"https://github.com/know-org-project/Nana-and-Jojo-s-Bizzare-LODventure/editor/{editor_name.replace(' ', '_')}")
    g.add((editor_uri, RDF.type, FOAF.Person))
    g.add((editor_uri, FOAF.name, Literal(editor_name)))
    g.add((poem_uri, DC.contributor, editor_uri))

# handling multiple publishers with respective publication dates
publishers = root.findall('.//{http://www.tei-c.org/ns/1.0}publicationStmt')
for pub in publishers:
    publisher_name = pub.find('.//{http://www.tei-c.org/ns/1.0}publisher').text
    publisher_uri = URIRef(f"https://github.com/know-org-project/Nana-and-Jojo-s-Bizzare-LODventure/publisher/{publisher_name.replace(' ', '_')}")
    pub_place = pub.find('.//{http://www.tei-c.org/ns/1.0}pubPlace').text
    pub_date = pub.find('.//{http://www.tei-c.org/ns/1.0}date').text

    g.add((publisher_uri, RDF.type, FOAF.Organization))
    g.add((publisher_uri, FOAF.name, Literal(publisher_name)))
    g.add((poem_uri, DC.publisher, publisher_uri))
    g.add((publisher_uri, DCTERMS.spatial, Literal(pub_place)))
    g.add((publisher_uri, DCTERMS.issued, Literal(pub_date, datatype=XSD.date)))

# the final graph
print(g.serialize(format='turtle'))

