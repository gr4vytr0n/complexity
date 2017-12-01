'''
    Iterator that always returns True
'''
class AllTrue(object):
    '''
        Always returns True
    '''
    def __next__(self):
        return True

    def __iter__(self):
        return self

if __name__ == '__main__':
    print(list(zip('abc', AllTrue())))
