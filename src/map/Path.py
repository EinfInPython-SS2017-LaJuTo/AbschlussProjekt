import pygame as pg

class Path:
    points = []
    subpaths = []
    width = 20
    color = (200,200,100)
    
    def __init__(self,file):
        self.readWaypoints(file)
        self.assignSubpaths()
        
    def readWaypoints(self,file):
        file = open(file)
        for line in file:
            coords = line.strip().split(",")
            self.points.append( (int(coords[0]),int(coords[1])) )
    
    def assignSubpaths(self):
        for i in range(len(self.points)-1):
            left = min(self.points[i][0], self.points[i+1][0]) - self.width/2
            top  = min(self.points[i][1], self.points[i+1][1]) - self.width/2
            
            width = abs(left - max(self.points[i][0], self.points[i+1][0])) + self.width
            height = abs(top - max(self.points[i][1], self.points[i+1][1])) + self.width
            if width == 0:
                width = self.width
            if height == 0:
                height = self.width
            
            self.subpaths.append( pg.Rect(left, top, width, height ))

    def draw(self, surface):
        for subpath in self.subpaths:
            pg.draw.rect(surface, self.color, subpath)
        
        
        
        
        
    