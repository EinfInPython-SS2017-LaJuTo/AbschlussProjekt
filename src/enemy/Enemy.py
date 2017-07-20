import pygame as pg
from tools.Vector import Vector
import random

class Enemy():
    # attributes:
        # pos (Position)
        # angle 
        # radius
        # image
        # vel
        # waypoint (the waypoint, it's currently heading for)
        # current
        # acc (for smooth turns around corners)               NOT YET IMPLEMENTED
              
        # health
        
    def __init__(self,image_path,subpath):
        self.pos = Vector(subpath.start[0],subpath.start[1])
        self.pos = self.pos + (random.randint(-10,10),random.randint(-10,10))
        self.radius  = 10 
        self.image = pg.image.load(image_path)
        self.image = pg.transform.scale(self.image, (self.radius*2,)*2)
        self.vel = 1
        self.waypoint = Vector(subpath.end[0],subpath.end[1])
        self.angle = (self.waypoint-self.pos).angle("deg")
        self.varyPath(20)
        self.current = 0 # the subpath, it's currently on
        
        self.health_start = 100
        self.health = self.health_start
        
    def update(self,gamemap):
        if self.health <= 0:
            gamemap.del_enemy(self)
        self.followPath(gamemap)
        self.angle = (self.waypoint-self.pos).angle("deg")
    
    def draw(self,surface):
        # render enemy
        rad2 = Vector(self.radius,self.radius)
        drawCenter = self.pos-rad2
        self.render_image = pg.transform.rotate(self.image,-self.angle)
        surface.blit(self.render_image, drawCenter)
        
        # render healthbar
        if self.health < self.health_start:
            pg.draw.rect(surface, (255,0,0), (self.pos-rad2,(self.radius*2/self.health_start*self.health,5)) )
        
    def hit(self,hitpoints):
        self.health -= hitpoints
        
    def followPath(self,gamemap):
        path = gamemap.getPaths()
        vector_to_waypoint = self.waypoint - self.pos
        if vector_to_waypoint.norm() > 1: # go to current waypoint
            self.pos = self.pos + vector_to_waypoint.normalize() * self.vel
            
        elif self.current < len(path)-1:
            self.current += 1
            self.waypoint = path[self.current].end # get next waypoint
            self.varyPath(gamemap.path.width)
        elif self.current == len(path)-1:
            self.current = 0
            self.waypoint = path[self.current].end
            self.pos = path[self.current].start
            self.varyPath(gamemap.path.width)
            
    def varyPath(self,amount):
        self.waypoint = self.waypoint + (random.randint(-amount/4,amount/4),random.randint(-amount/4,amount/4))
        