


class Foo(object):
    """docstring for Foo"""
    def __init__(self, x):
        self.x = x
    
    def descending_list(self, N):
        if N == 1:
            print 0
            return 0
        else:
            print N-1
            return self.descending_list(N-1)


foo = Foo(5)
foo.descending_list(10)

