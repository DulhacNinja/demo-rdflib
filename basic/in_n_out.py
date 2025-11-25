from rdflib import Graph

g = Graph()
g.parse("input.nt", format="nt")
# g.parse("http://www.w3.org/People/Berners-Lee/card")


print(f"Triples in the graph: {len(g)}\n")

for subj, pred, obj in g:
    print(f"subj: {subj} \npred: {pred} \nobj: {obj}\n")


g.serialize(destination="output.ttl", format="turtle")
