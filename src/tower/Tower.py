from pygame import Rect
import pygame as pg

class Tower(Rect):
    
    def __init__(self,x,y,img_path):
        super().__init__(x, y, 50, 50)
        self.img = pg.image.load(img_path)
        self.img = pg.transform.scale(self.img, self.size)
        
        self.active = False
        self.onPath = False
        
    def isOnPath(self,path):
        if self.collidelist(path) != -1:
            return True
        else:
            return False
    
    def place_down(self):
        if (not self.active) and (not self.onPath):
            self.active = True
            
    def update(self,path):
        #print(self.onPath)
        self.onPath = self.isOnPath(path)
        if not self.active:
            self.center = pg.mouse.get_pos()
        elif self.active:
            pass
    
    
    def draw(self,surface): 
        surface.blit(self.img, self.topleft)
        
        if self.onPath:
            aSurf = pg.Surface(self.size, pg.SRCALPHA)
            aSurf.convert_alpha()
            radius = int(self.width/2)
            pg.draw.circle(aSurf,(255,0,0,50), (radius,radius), radius)
            pg.draw.circle(aSurf,(255,0,0,250), (radius,radius), radius, 3)
            surface.blit(aSurf,self.topleft)
            
