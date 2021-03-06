import pygame as pg
from lib.Vector import Vector

class Path:
    # attributes:
        # points
        # subpaths
        # width
        # color
    
    def __init__(self,file, width, color):
        self.points = []
        self.subpaths = []
        self.width = width
        self.color = color
        self.readWaypoints(file)
        self.assignSubpaths()
        
    def readWaypoints(self,file):
        file = open(file)
        for line in file:
            coords = line.strip().split(",")
            self.points.append( Vector(coords[0],coords[1]).asInt() )
    
    def assignSubpaths(self):
        for i in range(len(self.points)-1):
            left = min(self.points[i][0], self.points[i+1][0]) - self.width/2
            top  = min(self.points[i][1], self.points[i+1][1]) - self.width/2
            
            width = abs(left - max(self.points[i][0], self.points[i+1][0])) + self.width/2
            height = abs(top - max(self.points[i][1], self.points[i+1][1])) + self.width/2
            if width == 0:
                width = self.width
            if height == 0:
                height = self.width
            
            start = self.points[i]
            end = self.points[i+1]
            
            self.subpaths.append( self.Subpath(left,top,width,height, start,end))

    def draw(self, surface):
        for subpath in self.subpaths:
            pg.draw.rect(surface, self.color, subpath)
        #for subpath in self.subpaths:
        #    pg.draw.circle(surface, (0,0,255), subpath.start, 2)
        #    pg.draw.circle(surface, (0,0,255), subpath.end, 2)
            
    class Subpath(pg.Rect):
        def __init__(self,x,y,width,height,start,end):
            super().__init__(x,y,width,height)
            self.start = start
            self.end = end
         
