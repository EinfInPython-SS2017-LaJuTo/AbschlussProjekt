import pygame as pg
from lib.Vector import Vector

class Bullet:
    # attributes:
        # pos
        # vel
        # target
        # hitpoints
        
    def __init__(self,pos,target):
        self.pos = Vector(pos[0],pos[1])
        self.vel = 10
        self.target = target
        self.hitpoints = 10
        
    def update(self,gamemap):
        # move
        direction = self.target.pos - self.pos
        direction = self.vel * direction.normalize()
        self.pos = self.pos + direction
        
        # hit
        if  (self.pos-self.target.pos).norm() <= self.target.radius:
            self.target.hit(self.hitpoints)
            self.delete(gamemap)
            
        # out of bounds
        if ((self.pos[0]<0 or self.pos[0]>gamemap.size[0]) or
           (self.pos[1]<0 or self.pos[1]>gamemap.size[1])) :
            gamemap.del_bullet(self)
    
    def show(self,surface):
        pg.draw.circle(surface, (255,255,255), self.pos.asInt(), 5)
    
    def delete(self,gamemap):
        gamemap.del_bullet(self)