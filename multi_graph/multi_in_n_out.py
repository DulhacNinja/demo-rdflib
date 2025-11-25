from rdflib import Graph
from rdflib import Dataset
from rdflib.namespace import RDF

g = Dataset()
# g.parse("input.nt", format="nt")
g.parse("multi_input.trig", format="trig")

#filter for quads which have rdf:type as predicate
for s, p, o, g in g.quads((None, RDF.type, None, None)):
    print(f"subj: {s} \npred: {p} \nobj: {o} \ngraph: {g} \n")

