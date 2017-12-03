'''
    Genenerate alpha-numeric pairs (e.g. a1...z1, a2...z2, ...)
'''
from string import ascii_lowercase


def alpha_num():
    while True:
        for l in ascii_lowercase:
            for i in range(len(ascii_lowercase)):
                yield l + str(i)


if __name__ == '__main__':
    for an in alpha_num():
        print(an)
