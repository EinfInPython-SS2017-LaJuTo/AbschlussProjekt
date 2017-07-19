import pygame as pg
from tools.Vector import Vector
import math

class Tower:
    # attributes:
        # pos
        # radius
        # range
        # img
        # active
        # onPath
        
    def __init__(self,x,y,img_path):
        self.pos = Vector(x,y)
        self.radius = 25
        self.range  = 50
        self.img = pg.image.load(img_path)
        self.img = pg.transform.scale(self.img, (self.radius*2,)*2)
        
        self.active = False
        self.onPath = False
        self.edge = self.setEdgePoints()
        
    def setEdgePoints(self):
        l = list( self.pos+(Vector(self.radius-4,0).rotate(a)) for a in range(0,360,int(360/8)))
        return l
        
        ''' Wenn du eine bessere Idee hierfür hast, nur zu! :) 
        self.edge[0] = (self.pos[0],self.pos[1]-self.radius)  # top
        self.edge[1] = (self.pos[0],self.pos[1]+self.radius)  # bottom
        self.edge[2] = (self.pos[0]-self.radius,self.pos[1])  # left
        self.edge[3] = (self.pos[0]+self.radius,self.pos[1])  # right
        self.edge[4] = (self.pos[0]-self.radius/2,self.pos[1]-self.radius/2)  # topleft
        self.edge[5] = (self.pos[0]+self.radius/2,self.pos[1]-self.radius/2)  # topright
        self.edge[6] = (self.pos[0]-self.radius/2,self.pos[1]+self.radius/2)  # bottomleft
        self.edge[7] = (self.pos[0]+self.radius/2,self.pos[1]+self.radius/2)  # bottomright
        self.edge[8] = self.pos
        '''
    def isOnPath(self,path):
        for subpath in path:
            for point in self.edge:
                if ((point[0]>subpath.left and point[0]<subpath.right)and
                    (point[1]>subpath.top and point[1]<subpath.bottom) ):
                    return True
        
    def place_down(self):
        if (not self.active) and (not self.onPath):
            self.active = True
            
    def update(self,path):
        self.onPath = self.isOnPath(path)
        if not self.active:
            self.edge = self.setEdgePoints()
            self.pos = Vector(pg.mouse.get_pos()[0],pg.mouse.get_pos()[1])
        elif self.active:
            pass
    
    def draw(self,surface): 
        rad2 = Vector(self.radius,self.radius)
        drawCenter = self.pos-rad2
        surface.blit(self.img, drawCenter)
        #for point in self.edge:
        #    pg.draw.circle(surface, (0,0,0), point.asInt() , 2)
        if self.onPath:
            aSurf = pg.Surface((self.radius*2,)*2, pg.SRCALPHA)
            aSurf.convert_alpha()
            radius = int(self.radius)
            pg.draw.circle(aSurf,(255,0,0,50), rad2, radius)
            pg.draw.circle(aSurf,(255,0,0,250), rad2, radius, 3)
            surface.blit(aSurf,drawCenter)
            
    def aim(self,gamemap):
        if self.active:
            for enemy in gamemap.enemies:
                if (enemy.pos - self.pos).norm() < self.range:
                    self.shoot(gamemap,enemy)
                    break
            
    def shoot(self,gamemap,target):
        gamemap.add_bullet(self.pos,target)
        