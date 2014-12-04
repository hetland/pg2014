# Rob Hetland
# 2014-10-14
# Homework 1, problem 2, trapazoidal integration
# Released under MIT license


import numpy as np

def trapz(f, dx=1.0):
    """Trapazoidal integration of function f, with spacing dx"""
    f = np.asarray(f)
    return dx * 0.5 * np.sum(f[1:] + f[:-1])


if __name__ == '__main__':
    
    # test with a flat funciton, of value 1
    f = np.ones(11)
    print trapz(f)  # should be 10
    print trapz(f, dx=0.5) # should be 5
    print trapz(f, dx=2.0) # should be 20
    
    dx = 0.001
    x = np.arange(0.0, 10.0+dx, dx)
    y = np.sin(x)
    print 'Should be close (give or take one..)'
    print trapz(y, dx=dx)
    print -np.cos(10.0) + 1