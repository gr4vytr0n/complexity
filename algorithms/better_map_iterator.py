from linear_map import LinearMap

class BetterMap(object):
    def __init__(self, n=100):
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())

    def find_map(self, k):
        index = hash(k) % len(self.maps)
        return self.maps[index]

    def add(self, k, v):
        m = self.find_map(k)
        m.add(k, v)

    def get(self, k):
        m = self.find_map(k)
        return m.get(k)

    def __len__(self):
        return len(self.maps)

    def iteritems(self):
        for i in self.maps:
            for j in i.items:
                yield j
