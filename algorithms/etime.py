import os

def etime():
    '''
        shows how much user and system time a process has used
    '''
    user, sys, chuser, chsys, real = os.times()

    return user + sys

if __name__ == '__main__':
    start = etime()

    # run a process here

    end = etime()

    elapsed_time = end - start
