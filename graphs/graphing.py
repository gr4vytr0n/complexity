from Graph import Graph
from Vertex import Vertex
from Edge import Edge

t = Vertex('t')
v = Vertex('v')
w = Vertex('w')
tv = Edge(t, v)
vw = Edge(v, w)
tw = Edge(t, w)

t2 = Vertex('t2')
v2 = Vertex('v2')
w2 = Vertex('w2')
t2v2 = Edge(t2, v2)
v2w2 = Edge(v2, w2)
t2w2 = Edge(t2, w2)

wv2 = Edge(w, v2)
wt2 = Edge(w, t2)

g = Graph([v, w, t, t2, v2, w2], [tv, vw, wv2, t2w2])

print(g.is_connected())
