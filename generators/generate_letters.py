'''
    Generator: a function that contains a yield statement
        -- makes an iterator
'''
from string import ascii_lowercase


def generate_letters():
    '''
        next() -- returns next iteration of lowercase letter sequence
    '''
    for letter in ascii_lowercase:
        yield letter


if __name__ == '__main__':
    g = generate_letters()
    for i in g:
        print(i)
