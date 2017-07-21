import pygame as pg
from lib.Vector import Vector

class Bullet:
    # attributes:
        # pos
        # vel
        # target
        # hitpoints
        # alive
        
    def __init__(self,pos,target):
        self.pos = Vector(pos[0],pos[1])
        self.vel = 0.5
        self.target = target
        self.hitpoints = 10
        self.alive = True
        
    def update(self,dt,bounds):
        # move
        direction = self.target.pos - self.pos
        self.pos = self.pos + dt*self.vel * direction.normalize()
        # hit
        if  (self.pos-self.target.pos).norm() <= self.target.radius + 5:
            self.alive = False
            self.target.hit(self.hitpoints) # return, who got enemy
        # out of bounds
        if ((self.pos[0]<0 or self.pos[0]>bounds[0]) or
           (self.pos[1]<0 or self.pos[1]>bounds[1])) :
            self.alive = False
    
    def show(self,surface):
        pg.draw.circle(surface, (255,255,255), self.pos.asInt(), 5)
    