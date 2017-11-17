from Graph import Graph
from Vertex import Vertex
from Edge import Edge

t = Vertex('t')
v = Vertex('v')
w = Vertex('w')
# e = Edge(v, w)
# f = Edge(v, t)

g = Graph([v, w, t])#, [e, f])

#print(g)
#print(g.vertices())
g.add_all_edges()
print(g.edges())
# print(g.out_vertices(v))
# print(g.out_edges(v))
#print(g['Vertex("t")'])