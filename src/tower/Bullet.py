import pygame as pg
from lib.Vector import Vector

class Bullet:
    # attributes:
        # radius
        # image
        
        # pos
        # vel
        # target
        # hitpoints
        # alive
        
    def __init__(self,pos,target,hitpoints ,image_bullet):
        self.radius = 7
        self.image = image_bullet
        self.image = pg.transform.scale(self.image, (self.radius*2,)*2) # scale the image to size
        
        self.pos = Vector(pos[0],pos[1])
        self.vel = 0.5 # perhaps later implement as 'tower-specific' variable?
        self.target = target
        self.hitpoints = hitpoints
        self.alive = True
        
    def update(self,dt,bounds):
        # move
        direction = self.target.pos - self.pos
        self.pos = self.pos + dt*self.vel * direction.normalize()
        # hit
        if  (self.pos-self.target.pos).norm() <= self.target.radius + 5:
            self.alive = False
            self.target.hit(self.hitpoints) # return, who got hit
        # out of bounds
        if ((self.pos[0]<0 or self.pos[0]>bounds[0]) or
           (self.pos[1]<0 or self.pos[1]>bounds[1])) :
            self.alive = False
    
    def show(self,surface):
        rad2 = Vector(self.radius,self.radius)
        draw_center = self.pos - rad2
        surface.blit(self.image, draw_center)
        #pg.draw.circle(surface, (255,255,255), self.pos.asInt(), 5)
    