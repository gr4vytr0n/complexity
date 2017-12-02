class LinearMap(object):
    def __init__(self):
        self.items = []

    def add(self, k, v):
        self.items.append((k, v))
    
    def get(self, k):
        for key, val in self.items:
            if key == k:
                return val
        raise KeyError

if __name__ == '__main__':
    lm = LinearMap()
    lm.add('cat', 'meow')
    print(lm.get('cat'))
