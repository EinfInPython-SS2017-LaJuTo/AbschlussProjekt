import pygame as pg

class Bullet:
    # attributes:
        # pos
        # vel
        # target
        
    def __init__(self,pos,target):
        self.pos = pos
        self.vel = 10
        self.target = target
        
    def update(self,gamemap):
        # move
        direction = self.subtract(self.target.pos, self.pos)
        direction = self.scalmult(self.vel/self.norm(direction),direction)
        self.pos = self.add(self.pos, direction)
        
        # delete (on hit, or when off screen)
        if ((self.norm(self.subtract(self.pos,self.target.pos)) <= self.target.radius) or
           (self.pos[0]<0 or self.pos[0]>gamemap.size[0]) or
           (self.pos[1]<0 or self.pos[1]>gamemap.size[1])):
            gamemap.del_bullet(self)
        
    def show(self,surface):
        pg.draw.circle(surface, (255,255,255), (int(self.pos[0]),int(self.pos[1])), 5)
    
    
    ''' WIRD DURCH ORDENTLICHE VEKTOR-KLASSE ERSETZT'''
    def add(self, tuple1, tuple2):
        return (tuple1[0]+tuple2[0], tuple1[1]+tuple2[1])
    def subtract(self, tuple1, tuple2):
        return (tuple1[0]-tuple2[0], tuple1[1]-tuple2[1])
    def scalmult(self, scalar,tuple1):
        return (scalar*tuple1[0], scalar*tuple1[1])
    def norm(self,tuple1):
        return ( tuple1[0]**2 + tuple1[1]**2)**0.5