from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import FOAF, RDF

g = Graph()
g.bind("foaf", FOAF) # FOAF = friend of a friend

bob = URIRef("http://example.org/people/Bob")
linda = BNode( value = "linda.jpeg")  # a GUID is generated

name = Literal("Bob")
age = Literal(24)

g.add((bob, RDF.type, FOAF.Person))
g.add((bob, FOAF.name, name))
g.add((bob, FOAF.age, age))
g.add((bob, FOAF.knows, linda))
g.add((linda, RDF.type, FOAF.Person))
g.add((linda, FOAF.name, Literal("Linda")))

g.serialize(destination="big_created_graph.nt", format="nt", encoding="utf-8")
g.serialize(destination="big_created_graph.ttl", format="turtle", encoding="utf-8")