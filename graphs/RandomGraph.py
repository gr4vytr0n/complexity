import random as rand
import itertools as it
import numpy as np

from Graph import Graph
from Vertex import Vertex
from Edge import Edge

# Erdős-Rényi random graph model G(n, p)
# n is number of vertices
# p is probability that there is an edge between two nodes
class RandomGraph(Graph):
  def __init__(self, vs = [], es = []):
    Graph.__init__(self, vs, es)

  def add_random_edges(self, probability):
    # possible nodes combinations
    combos = list(it.combinations(self.vertices(), 2))
    # 1 - add edge, 0 - no edge added -- draw samples from binomial distribution
    edge_hits = np.random.binomial(1, probability, len(combos))
    # list of edges to be made
    edges = [combos[i] for i in range(len(edge_hits)) if edge_hits[i] == 1]
    for i in edges:
      self.add_edge(Edge(i[0], i[1]))

if __name__ == '__main__':
  v = Vertex('v')
  w = Vertex('w')
  x = Vertex('x')
  y = Vertex('y')
  r = RandomGraph([v, w, x, y])
  randomProbability = rand.uniform(0, 1)
  r.add_random_edges(randomProbability)
  print(r.edges())
