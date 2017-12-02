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

if __name__ == '__main__':
    bm = BetterMap()
    bm.add('dog', 'roof')
    print(bm.get('dog'))
