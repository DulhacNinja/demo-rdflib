# demo-rdflib

RDFlib demonstration examples for working with RDF data.

## Folder Descriptions

### basic/
Parses an N-Triples file, displays all triples, and exports to Turtle format.

### creating/
Programmatically creates RDF triples (a Person node with name) and serializes to Turtle.

### navigation/
Queries a graph to check if a resource exists, then extracts and filters triples for a specific subject (Bob).

### multi_graph/
Parses a TriG file (multi-graph format) and filters quads by RDF type across named graphs.

### queries/
Executes a SPARQL SELECT query to find relationships (who knows whom) from RDF data.