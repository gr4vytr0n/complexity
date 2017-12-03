from better_map_iterator import BetterMap

class HashMap(object):
    def __init__(self):
        self.maps = BetterMap(2)
        self.num = 0

    def get(self, k):
        return self.maps.get(k)

    def add(self, k, v):
        if self.num == len(self.maps):
            self.resize()
        
        self.maps.add(k, v)
        self.num += 1

    def resize(self):
        new_maps = BetterMap(self.num * 2)

        for k, v in self.maps.items():
            new_maps.add(k, v)
        
        self.maps = new_maps

if __name__ == '__main__':
    hm = HashMap()
    for i in range(100):
        hm.add('{}'.format(i), i)
    
    for i in range(100):
        print(hm.get(str(i)))