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
    """add (e) to the graph by adding an entry in both directions. if there is already an edge connecting these vertices, the new edge replaces it"""
    v, w = e
    self[v][w] = e
    self[w][v] = e

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
    print(self)
