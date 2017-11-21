import string
import random

from RandomGraph import RandomGraph

# connectedness of a graph can display the `phase-chage`
#

# generate random graphs for n (number of vertices) and p (probabilty)
def generate_graphs(num_graphs, n):
  graphs = []

  # generate n number of lists of random list of unique letters for vertices
  alpha = list(string.ascii_lowercase[::1])
  vLists = []
  i = num_graphs
  while i > 0:
    # variable sized list of random alphabetic characters -- vertex labels
    # lists can have from up to 26 (inclusive) vertices
    sample = random.sample(alpha, n)
    # append to vList if a similar list is not already existing
    if sample in vLists:
      break
    else:
      vLists.append(sorted(sample))
      i -= 1

  for v in vLists:
    graphs.append(RandomGraph(v))
  return graphs

if __name__ == '__main__':
  import matplotlib.pyplot as plt

  iters = 10000
  div = iters
  n = 10
  p = random.uniform(0, 1)
  connectedCount = 0
  while iters > 0:
    master = {}
    g = generate_graphs(1, n) 
    for i in range(len(g)):
      g[i].add_random_edges(p)
      master[i] = {}
      master[i]['connected'] = g[i].is_connected()
      if master[i]['connected'] == True:
        connectedCount += 1
      master[i]['p'] = p
      for j in g[i]:
        g[i][j].clear()
      iters -= 1

  print('probability of being connected: {}%, for n: {} and p: {}'.format(((connectedCount/div)*100), 10, p))