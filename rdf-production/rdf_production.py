import pandas as pd
from rdflib import Graph, Literal, URIRef, Namespace
from rdflib.namespace import XSD, OWL
import urllib.parse

dir = "https://github.com/know-org-project/Nana-and-Jojo-s-Bizzare-LODventure/tree/main/csvs"
csv = ["Amphora","Suit","Painting","FashionCollection","Album","MusicRecording","Movie","Poem","Shoes","Manga","MangaSeries","rel","Concept"]
df_list = []
for i in csv:
  dir_name = dir + i + ".csv"
  df=pd.read_csv(dir_name)
  df_list.append(df)

g = Graph()
root = "https://github.com/know-org-project/Nana-and-Jojo-s-Bizzare-LODventure/"
prov = Namespace("http://www.w3.org/ns/prov#")
dct = Namespace("http://purl.org/dc/terms/")
schema = Namespace("https://schema.org/")
gvp = Namespace("http://vocab.getty.edu/ontology#")
crm = Namespace("http://www.cidoc-crm.org/cidoc-crm/")
dbo = Namespace("https://dbpedia.org/ontology/")
gn = Namespace("http://www.geonames.org/ontology/documentation.html#")
rdag1 = Namespace("http://rdvocab.info/Elements/")
frbrer = Namespace("https://www.iflastandards.info/fr/frbr/frbrer#")
skos = Namespace("http://www.w3.org/2004/02/skos/core#")
wd = Namespace("https://www.wikidata.org/wiki/")
eft = Namespace("http://thesaurus.europeanafashion.eu/thesaurus/")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
foaf = Namespace("http://xmlns.com/foaf/spec/#term_")
fabio = Namespace("http://purl.org/spar/fabio/")
frapo = Namespace("http://purl.org/cerif/frapo/")
viaf = Namespace("https://viaf.org/viaf/")
tgn = Namespace("http://vocab.getty.edu/page/tgn/")
g.bind("prov",prov)
g.bind("dc",dct)
g.bind("schema",schema)
g.bind("gvp",gvp)
g.bind("crm",crm)
g.bind("dbo",dbo)
g.bind("gn",gn)
g.bind("rdag1",rdag1)
g.bind("frbrer",frbrer)
g.bind("skos",skos)
g.bind("wd",wd)
g.bind("eft",eft)
g.bind("rdf",rdf)
g.bind("foaf",foaf)
g.bind("fabio",fabio)
g.bind("frapo",frapo)
g.bind("viaf",viaf)
g.bind("tgn",tgn)


pred_dict = {
    "crm:P67_refers_to":crm.P67_refers_to, "crm:P32_used_general_technique":crm.P32_used_general_technique, "dc:creator":dct.creator, "schema:locationCreated":schema.locationCreated,
    "schema:birthPlace":schema.birthPlace, "gn:locatedIn":gn.locatedIn, "dbo:institution":dbo.institution, "dc:medium":dct.medium,"dbo:Place":dbo.Place,
    "dc:publisher":dct.publisher, "dc:isPartOf":dct.isPartOf,"foaf:Person":foaf.Person,"schema:Country":schema.Country,"dbo:ArtisticGenre":dbo.ArtisticGenre,
    "gvp:aat2894_exemplified_by":gvp.aat2894_exemplified_by, "prov:wasAttributedTo":prov.wasAttributedTo, "schema:director":schema.director, "schema:genre":schema.genre,
    "foaf:Organization":foaf.Organization, "schema:producer":schema.producer, "dbo:Painting":dbo.Painting, "schema:MusicAlbum":schema.MusicAlbum, "fabio:Poem":fabio.Poem,
    "schema:Movie":schema.Movie, "crm:E24_Physical_Human_Made_Thing":crm.E24_Physical_Human_Made_Thing, "schema:MusicRecording":schema.MusicRecording,
    "schema:Continent":schema.Continent, "wd:Q829960":wd.Q829960, "rdag1:placeOfPublication":rdag1.placeOfPublication, "wd:Q8274":wd.Q8274, "wd:Q21198342":wd.Q21198342,
    "frapo:collaboratesWith":frapo.collaboratesWith, "gvp:aat2422_takes_place_in":gvp.aat2422_takes_place_in,"dc:coverage":dct.coverage, "frbrer:P3003":frbrer.P3003,
    "dbo:releaseDate":dbo.releaseDate, "dc:title":dct.title, "dc:description":dct.description, "rdf:type":rdf.type, "owl:sameAs":OWL.sameAs, "schema:about":schema.about,
    "skos:broader":skos.broader, "fabio:Periodical":fabio.Periodical, "skos:Concept":skos.Concept, "skos:narrower":skos.narrower, "skos:related":skos.related,
    "eft:10952":(eft+"10952"),"eft:10249":(eft+"10249"),"eft:10002":(eft+"10002"), "schema:MusicGroup":schema.MusicGroup,"dbo:LiteraryGenre":dbo.LiteraryGenre,
    "dbo:MusicGenre":dbo.MusicGenre, "schema:Event":schema.Event, "europeana:2048222":"https://www.europeana.eu/en/item/2048222/europeana_fashion_1981",
    "va:O72586":"https://collections.vam.ac.uk/item/O72586/bondage-suit-vivienne-westwood/", "wd:Q662166":wd.Q662166, "wd:Q663481":wd.Q663481,
    "wc:659263635":"https://search.worldcat.org/title/659263635", "europeana:2048212":"https://www.europeana.eu/en/item/2048212/europeana_fashion_gucci_aw11_0115",
    "wd:Q696918":wd.Q696918, "wol:jtAnfd1D4bE":"https://whiteoak.library.link/portal/jtAnfd1D4bE","met:248902":"https://www.metmuseum.org/art/collection/search/248902",
    "imdb:tt0060176":"https://www.imdb.com/title/tt0060176/", "viaf:116608684":(viaf+"116608684"), "viaf:51908743":(viaf+"51908743"), "viaf:95159449":(viaf+"95159449"),
    "viaf:85586601":(viaf+"85586601"), "wd:Q82545":wd.Q82545, "wd:Q1374087":wd.Q1374087, "viaf:69008939":(viaf+"69008939"), "viaf:133624743":(viaf+"133624743"),
    "viaf:117455224":(viaf+"117455224"), "viaf:110291829":(viaf+"110291829"),"tgn:7008591":(tgn+"7008591"),"tgn:1000080":(tgn+"1000080"),"tgn:1000063":(tgn+"1000063"),
    "tgn:1000003":(tgn+"1000003"),"tgn:1000120":(tgn+"1000120"),"tgn:7012149":(tgn+"7012149"),"wd:Q11772":wd.Q11772, "wd:Q178516":wd.Q178516
}

for i in df_list:
  for idx, row in i.iterrows():
    if row[0] == "wd:Q8274" or row[0] =="wd:Q21198342":
      s = pred_dict[row[0]]
    else:
      s = URIRef(root+row[0])
    p = row[1]
    o = row[2]
    if p == "rdf:type" or p == "owl:sameAs" or p == "skos:broader" or (p == "skos:related" and ":" in o):
      o = pred_dict[o]
    if "/" in o:
      o = URIRef(root+o)
    else:
      o = Literal(o)
    g.add((s,pred_dict[p],o))


turtle_str = g.serialize(format="turtle", base=root, encoding="utf-8")
with open("output.ttl", "wb") as f:
    f.write(turtle_str)