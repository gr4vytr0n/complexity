from Edge import Edge

# undirected graph implementation
class Graph(dict):
  def __init__(self, vs=[], es=[]):
    """create a new graph. (vs) is a list of vertices; (es) is a list of edges. """
    for v in vs:
      self.add_vertex(v)

    for e in es:
      self.add_edge(e)

  def add_vertex(self, v):
    """add (v) to the graph"""
    self[v] = {}

  def add_edge(self, e):
    """add (e) to the graph by adding an entry in both directions.
       if there is already an edge connecting these vertices, the new edge replaces it"""
    a, b = e
    self[a][b] = e
    self[b][a] = e

  def get_edge(self, node1, node2):
    try:
      edge = self[node1][node2]
    except KeyError:
      edge = None
    return edge

  def remove_edge(self, edge):
    v1, v2 = edge
    del self[v1][v2]
    del self[v2][v1]

  def vertices(self):
    return [v for v in self]

  def edges(self):
    return list(set(self[v][es] for v in self for es in self[v]))

  def out_vertices(self, vertex):
    return [ov for ov in self[vertex]]

  def out_edges(self, vertex):
    return [self[vertex][x] for x in self[vertex]]

  def add_all_edges(self):
    for v1 in self:
      for v2 in self:
        if v1 != v2:
          self.add_edge(Edge(v1, v2))
