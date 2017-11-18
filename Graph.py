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

  # Rules for building regular graphs
    # -Preconditions: 0 < k and k < n
    # -If n is odd, k must be even
    # -If n is odd, we add edges between vertices x positions away,
    #  where x is all odd numbers between 1 to k.
    # -If n is even, and k is even, we add edges between vertices x
    #  positions away, where x is a range of numbers starting from 1 to n/2,
    #  and the range of these numbers is limited by the number of even numbers
    #  from 1 to k, including k
    # -If n is even, and k is odd, we add edges between vertices x positions away,
    #  where x is a range of numbers starting from n/2 to 1, and the range of these
    #  numbers is limited by the number of odd numbers from 1 to k, including k
  def add_regular_edges(self, degree):
    vList = [v for v in self]
    if degree <= 0:
      raise ValueError('degree must be greater than zero')
    if degree > len(vList):
      raise ValueError('degree must be less than number of vertices')
    if len(vList)%2 != 0 and degree%2!=0:
      raise ValueError('if the number of vertices is odd the degree must be even')

    def add_edges(vertices, distances):
      adjacentVertices = []
      for d in distances:
        for i in range(0, len(vertices), d):
          adjacentVertices.append(vertices[i])
      print(adjacentVertices)

    if len(vList)%2 != 0:
      x = [i for i in range(1, degree+1) if i%2!=0]
      add_edges(vList, x)
    elif len(vList)%2 == 0:
      if degree%2 == 0:
        x = set([i for i in range(1, int(len(vList)/2))])
        x = x & set([i for i in range(1, degree+1) if i%2==0])
        add_edges(vList, x)
      elif degree%2 != 0:
        x = set([i for i in range(int(len(vList)/2), 0, -1)])
        x = x & set([i for i in range(1, degree+1) if i%2!=0])
        add_edges(vList, x)
    
    
    