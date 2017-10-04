import pygame as pg
from lib.Vector import Vector
import random

class Enemy():
    # attributes:
        # pos      (Position)
        # angle 
        # radius   (Hitbox)
        # image
        # waypoint (the waypoint, it's currently heading for)
        # current  (the subpath, it's currently on)
             
        # alive
        # health
        # speed
        # value
        
    def __init__(self, subpath, image,speed=10, health_start=100, angle=90, radius=10, value=1):
        self.pos        = Vector(subpath.start[0],subpath.start[1])
        self.pos        = self.pos + (random.randint(-10,10), random.randint(-10,10))
        self.radius     = radius
        self.image      = image
        self.image      = pg.transform.scale(self.image, (self.radius*2,)*2)
        self.waypoint   = Vector(subpath.end[0],subpath.end[1])
        self.angle      = (self.waypoint-self.pos).angle("deg")
        self.varyPath(20)
        self.current    = 0 
        
        self.alive      = True
        self.health_start = health_start
        self.health     = self.health_start
        self.speed      = speed/100
        self.value      = value
        
    def update(self,subpaths,dt):
        if self.health <= 0:
            self.alive = False
        self.followPath(subpaths,dt)
        if (self.waypoint-self.pos) == 0:
            pass
        else:
            self.angle = (self.waypoint-self.pos).angle("deg")
    
    def draw(self,surface):
        # render enemy
        rad2 = Vector(self.radius,self.radius)
        render_image = pg.transform.rotozoom(self.image,-self.angle,1)
        draw_center = self.pos - Vector( *render_image.get_size() )/2
        surface.blit(render_image, draw_center)
        
        # render healthbar
        if self.health < self.health_start:
            self.draw_bar(surface, self.pos-rad2-Vector(0,5), (self.radius*2, 5), (0,0,0))
            self.draw_bar(surface, self.pos-rad2-Vector(0,5), (self.radius*2/self.health_start*self.health, 5), (255,0,0))
        
    def draw_bar(self,surface, topleft, size, color):
        pg.draw.rect(surface, color, (topleft,size) )
    
    def hit(self,hitpoints):
        self.health -= hitpoints
        
    def followPath(self,subpaths,dt):
        vector_to_waypoint = self.waypoint - self.pos
        rand_offset = subpaths[0].width # [0] doesn't matter, just need an element of subpaths
        
        # NOT YET AT WAYPOINT
        if vector_to_waypoint.norm() > 5:                                   
            self.pos = self.pos + vector_to_waypoint.normalize() * self.speed*dt 
        # AT WAYPOINT != END
        elif self.current < len(subpaths)-1:
            self.current += 1
            self.waypoint = subpaths[self.current].end 
            self.varyPath(rand_offset)
        # AT WAYPOINT == END
        elif self.current == len(subpaths)-1:
            self.current = 0
            self.waypoint = subpaths[self.current].end
            self.pos = subpaths[self.current].start
            self.varyPath(rand_offset)
            
    def varyPath(self,amount):
        self.waypoint = self.waypoint + (random.randint(-amount/4,amount/4),random.randint(-amount/4,amount/4))
        
