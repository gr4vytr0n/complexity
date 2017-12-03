from sys import path

path.insert(0, '/media/gtron/files/complexity/algorithms/')
path.insert(0, '/media/gtron/files/complexity/algorithms/perf/')

from etime import etime
from better_map_iterator import BetterMap
bm = BetterMap()

# build map
for i in range(10000000):
    key = '{}'.format(i)
    bm.add(key, i)

start = etime()

for i in range(10000):
    key = '{}'.format(i)
    bm.get(key)

end = etime()

print(end - start)
