from sys import path

path.insert(0, '/media/gtron/files/complexity/algorithms/')
path.insert(0, '/media/gtron/files/complexity/algorithms/perf/')

from etime import etime
from hash_table import HashMap
hm = HashMap()

# build map
for i in range(1000000):
    key = '{}'.format(i)
    hm.add(key, i)

start = etime()

for i in range(10000):
    key = '{}'.format(i)
    hm.get(key)

end = etime()

print(end - start)
