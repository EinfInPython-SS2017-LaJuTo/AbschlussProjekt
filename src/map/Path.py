from pygame import Rect

class Path:
    points = []
    subpaths = []
    width = 10
    
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
            left = self.points[i][0]
            top = self.points[i][1]
            width = abs(left - self.points[i+1][0])
            height = abs(top - self.points[i+1][1])
            if width == 0:
                width = self.width
            if height == 0:
                height = self.width
            self.subpaths.append( Rect(left, top, width, height ))
