
from math import sqrt

class Point(object):
    """docstring for Point"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def norm(self):
        return sqrt(self.x**2 + self.y**2)
    
    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)
    

