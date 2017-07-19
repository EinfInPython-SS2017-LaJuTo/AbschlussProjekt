import pygame as pg
from tools.Vector import Vector

class Enemy():
    # attributes:
        # pos (Position)
        # radius
        # waypoint (the waypoint, it's currently heading for)
        # vel
        # acc (for smooth turns around corners)               NOT YET IMPLEMENTED
        
    def __init__(self,subpath):
        self.pos = Vector(subpath.start[0],subpath.start[1])
        self.vel = 1
        self.radius  = 7 # is going to depend on its image
        self.waypoint = Vector(subpath.end[0],subpath.end[1])
        self.current = 0 # the subpath, it's currently on
        
    def update(self,path):
        self.followPath(path)
    
    def draw(self,surface):
        pg.draw.circle( surface, (255,0,0), self.pos.asInt(), self.radius )
        
    def followPath(self,path):
        vector_to_waypoint = self.waypoint - self.pos
        if vector_to_waypoint.norm() > 1: # go to current waypoint
            self.pos = self.pos + vector_to_waypoint.normalize() * self.vel
            
        elif self.current < len(path)-1:
            self.current += 1
            self.waypoint = path[self.current].end # get next waypoint
            
        elif self.current == len(path)-1:
            self.current = 0
            self.waypoint = path[self.current].end
            self.pos = path[self.current].start
            
        
        