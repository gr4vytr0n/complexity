import string
import random

from RandomGraph import RandomGraph

# connectedness of a graph can display the `phase-chage`
#

# generate random graphs for n (number of vertices) and p (probabilty)
def generate_graphs(num_graphs, n):
  graphs = []

  # generate 10 lists of randomly sized list of unique letters for vertices
  alpha = list(string.ascii_lowercase[::1])
  vLists = []
  i = num_graphs
  while i > 0:
    # random sized list of random alphabetic characters -- vertex labels
    # lists will have from 2 to 26 (inclusive) vertices
    sample = random.sample(alpha, n)
    # append to vList if a similar list is not already existing
    if sample in vLists:
      break
    else:
      vLists.append(sample)
      i -= 1

  for v in vLists:
    graphs.append(RandomGraph(v))
  return graphs

if __name__ == '__main__':
  import matplotlib.pyplot as plt

  x = 10000
  p = random.uniform(0, 1)
  connectedCount = 0
  while x > 0:
    master = {}
    g = generate_graphs(1, 10) 
    for i in range(len(g)):
      g[i].add_random_edges(p)
      master[i] = {}
      master[i]['connected'] = g[i].is_connected()
      if master[i]['connected'] == True:
        connectedCount += 1
      master[i]['p'] = p
      for j in g[i]:
        g[i][j].clear()
      x -= 1

  print('probability of being connected: %f, for n: %d and p: %f' % (((connectedCount/10000)*100), 10, p))