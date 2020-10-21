# Git bash Training: OOP Homework Line and cylinder
from math import sqrt

class Line:
    
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        dx = self.coor2[0]-self.coor1[0]
        dy = self.coor2[1]-self.coor1[1]
        
        d = sqrt((dx)**2+(dy)**2)
        
        return d
    
    def slope(self):
        dx = self.coor2[0]-self.coor1[0]
        dy = self.coor2[1]-self.coor1[1]
        
        a = dy/dx
        
        return a

#Example output

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)

d = li.distance()
a = li.slope()

print(d, a)