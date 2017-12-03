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
    
    def __str__(self):
        res = ''
        for k, v in self.items:
            print('hello')
        return res
