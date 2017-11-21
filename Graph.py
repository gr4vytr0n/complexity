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
  #   0 < degree and degree < number of vertices
  #   if number of vertices is odd, degree must be even
  def add_regular_edges(self, degree):
    vList = [v for v in self]
    if degree <= 0:
      raise ValueError('degree must be greater than zero')
    if degree > len(vList):
      raise ValueError('degree must be less than number of vertices')
    if (len(vList) %2 ) != 0 and (degree % 2) != 0:
      raise ValueError('if the number of vertices is odd the degree must be even')

    def add_edges(vertices, distances):
      # lookup table to determine if edge has been made already
      edgeTable = {}
      for d in distances:
        flag = False
        atVert = 0
        nextVert = atVert + d
        while not flag:
          # add edge to graph and to lookup table
          self.add_edge(Edge(vertices[atVert], vertices[nextVert]))
          edgeTable[(atVert, nextVert)] = None
          atVert += d
          nextVert += d
          # check if atVert or nextVert need to loop back through begining of vertices list
          if atVert > (len(vertices) - 1):
            atVert = atVert - len(vertices)
          if nextVert > (len(vertices) - 1):
            nextVert = nextVert - len(vertices)
          # check lookup table for edge; if edge exists exit loop and loop through next distance
          if (atVert, nextVert) in edgeTable:
            flag = True

    # if number of vertices is odd
    if (len(vList) % 2) != 0:
      # distances will be all odd numbers from 1 to k (not including k)
      distances = [i for i in range(1, degree, 2)]
      add_edges(vList, distances)
    # if number of vertices is event
    elif (len(vList) % 2) == 0:
      # if degree is even
      if (degree % 2) == 0:
        # possible distances
        possibles = [i for i in range(1, int(len(vList) / 2))]
        # number of even numbers in range 1 to k (including k)
        numberOfEvens = len([i for i in range(1, (degree + 1)) if (i % 2) == 0])
        # distances are first numberOfEvens out of possibles
        distances = possibles[:numberOfEvens]
        add_edges(vList, distances)
      # if degree is odd
      elif (degree % 2) != 0:
        # possible distances
        possibles = [i for i in range(int(len(vList) / 2), 1, -1)]
        # number of odd numbers in range 1 to k (including k)
        numberOfOdds = len([i for i in range(1, (degree + 1)) if (i % 2) != 0])
        # distances are first numberOfOdds out of possibles
        distances = possibles[:numberOfOdds]
        add_edges(vList, distances)

  # Determine if a graph is a `connected graph`
  # Using breadth-first search
  def is_connected(self):

    # code from wikipedia to be adapted for use here
    def bfs(problem):
      # FIFO set
      open_set = Queue()
      # set of empty nodes
      closed_set = set()
      # meta info. (used for path formation)
      meta = dict() # key -> (parent state, action to reach child)
      # initialize
      start = problem.get_start_state()
      meta[start] = (None, None)
      open_set.enqueue(start)

      while not open_set.is_empty():
        parent_state = open_set.dequeue()
        if problem.is_goal(parent_state)
          return construct_path(parent_state, meta)
        for (child_state, action) in problem.get_successors(parent_state):
          if child_state in closed_set:
            continue
          if child_state not in open_set:
            meta[child_state] = (parent_state, action)
            open_set.enqueue(child_state)

        closed_set.add(parent_state)
    def construct_path(state, meta):
      action_list = list()
      while True:
        row = meta[state]
        if len(row) == 2:
          state = row[0]
          action = row[1]
          action_list.append(action)
        else:
          break
      return action_list.reverse()