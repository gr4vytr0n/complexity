from sys import path

path.insert(0, '/media/gtron/files/complexity/algorithms/')
path.insert(0, '/media/gtron/files/complexity/algorithms/perf/')
path.insert(0, '/media/gtron/files/complexity/pyplot/')

from plots import make_plot
from etime import etime
from hash_table import HashMap

hm = HashMap()

ns = []
times = []

for n in range(5000, 30000, 1000):
    ns.append(n)

    # build map of size n
    for i in range(n):
        key = '{}'.format(i)
        hm.add(key, i)

    start = etime()

    # search map for specific key
    for i in range(n):
        key = '{}'.format(i)
        hm.get(key)

    end = etime()

    times.append(end - start)

make_plot(ns, times)
