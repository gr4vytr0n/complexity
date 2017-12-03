from sys import path

path.insert(0, '/media/gtron/files/complexity/algorithms/')
path.insert(0, '/media/gtron/files/complexity/algorithms/perf/')

from etime import etime
from linear_map import LinearMap

lm = LinearMap()

# build map
for i in range(10000):
    key = '{}'.format(i)
    lm.add(key, i)

start = etime()

for i in range(10000):
    key = '{}'.format(i)
    lm.get(key)

end = etime()

print(end - start)
