from Graph import Graph
from Vertex import Vertex
from Edge import Edge

# 7, 2
t = Vertex('t')
v = Vertex('v')
w = Vertex('w')
t2 = Vertex('t2')
v2 = Vertex('v2')
w2 = Vertex('w2')
w3 = Vertex('w3')
g = Graph([v, w, t, v2, w2, t2, w3])
g.add_regular_edges(2)
print(g.edges())

# 6, 2
a = Vertex('a')
b = Vertex('b')
c = Vertex('c')
a2 = Vertex('a2')
b2 = Vertex('b2')
c2 = Vertex('c2')
h = Graph([a, b, c, a2, b2, c2])
h.add_regular_edges(2)
print(h.edges())

# 6, 3
q = Vertex('q')
r = Vertex('r')
s = Vertex('s')
q2 = Vertex('q2')
r2 = Vertex('r2')
s2 = Vertex('s2')
i = Graph([q, r, s, q2, r2, s2])
i.add_regular_edges(3)
print(i.edges())
