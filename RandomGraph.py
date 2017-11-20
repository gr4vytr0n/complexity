import random
import itertools

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
    combos = itertools.combinations(self.vertices(), 2)
    print([i for i in combos])

if __name__ == '__main__':
  v = Vertex('v')
  w = Vertex('w')
  x = Vertex('x')
  y = Vertex('y')
  r = RandomGraph([v, w, x, y])
  randomProbability = random.uniform(0, 1)
  r.add_random_edges(randomProbability)
