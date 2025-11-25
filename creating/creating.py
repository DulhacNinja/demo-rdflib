from rdflib import Graph, URIRef, Literal
from rdflib.namespace import FOAF, RDF

bob = URIRef("http://example.org/people/Bob")

name = Literal("Bob")

g = Graph()
# g.bind("people", "http://example.org/people/Bob")

g.add((bob, RDF.type, FOAF.Person))
g.add((bob, FOAF.name, name))

g.serialize(destination="created_graph.ttl", format="turtle")