import pygame as pg

class Enemy():
    # attributes:
        # pos (Position)
        # width
        # height
        # waypoint (the waypoint, it's currently heading for)
        # vel
        # acc (for smooth turns around corners) NOT YET IMPLEMENTED
        
    def __init__(self,subpath):
        self.pos = subpath.start
        self.vel = 1
        self.radius  = 7 # is going to depend on its image
        self.waypoint = subpath.end
        self.current = 0 # the subpath, it's currently on
        
    def update(self,path):
        self.followPath(path)
    
    def draw(self,surface):
        pg.draw.circle( surface, (255,0,0), (int(self.pos[0]),int(self.pos[1])), self.radius )
        
    def followPath(self,path):
        vector_to_waypoint = self.subtract(self.waypoint,self.pos)
        if self.norm( vector_to_waypoint ) > 1: # go to current waypoint
            self.moveBy( vector_to_waypoint, self.vel )
        elif self.current < len(path)-1:
            self.current += 1
            self.waypoint = path[self.current].end # get next waypoint
        elif self.current == len(path)-1:
            self.current = 0
            self.waypoint = path[self.current].end
            self.pos = path[self.current].start
            
    def moveBy(self, direction, amount):
        self.pos = self.add(self.pos, self.scaldiv(direction,self.norm( direction )/amount) )
        
        
    def add(self, tuple1, tuple2):
        return (tuple1[0]+tuple2[0], tuple1[1]+tuple2[1])
    def subtract(self, tuple1, tuple2):
        return (tuple1[0]-tuple2[0], tuple1[1]-tuple2[1])
    def scalmult(self, scalar,tuple1):
        return (scalar*tuple1[0], scalar*tuple1[1])
    def scaldiv(self, tuple1, scalar):
        if scalar != 0:
            return (tuple1[0]/scalar, tuple1[1]/scalar)
        else:
            return 0
    def norm(self,tuple1):
        return ( tuple1[0]**2 + tuple1[1]**2)**0.5