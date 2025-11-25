from rdflib import Graph, URIRef
from rdflib.namespace import RDF, FOAF

g = Graph()
g_bob = Graph()
g.parse("navigation_data.nt", format="nt")

print(f"Triples in the graph: {len(g)}\n")

bob = URIRef("http://example.org/people/bob")
if (bob, RDF.type, FOAF.Person) in g:
    print("This graph knows that Bob is a person!\n")

# Display all triples involving Bob
print("All triples involving Bob:")
for subj, pred, obj in g.triples((bob, None, None)):
    print(f"  {subj} -> {pred} -> {obj}")
    g_bob.add((subj, pred, obj))

g_bob.serialize(destination="bob_data.ttl", format="turtle")