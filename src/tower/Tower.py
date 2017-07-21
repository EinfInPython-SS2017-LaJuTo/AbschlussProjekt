import pygame as pg
from lib.Vector import Vector

class Tower:
    # attributes:
        # pos
        # radius
        
        # image
        
        # active
        # onPath
        # edge      (points that make up hitbox)
        
        # target
        # angle
        
        # reload_time
        # shot_ready 
        # range
        
    def __init__(self,img_path):
        self.pos = Vector(0,0)
        self.radius = 25
        
        self.image = pg.image.load(img_path)
        self.image = pg.transform.scale(self.image, (self.radius*2,)*2) # scale the image to size

        self.active = False
        self.onPath = False
        self.edge = self.setEdgePoints()
        
        self.target = None
        self.angle = 0
        
        self.range  = 150
        self.reload_time = 10
        self.shot_ready = 0
        
    def setEdgePoints(self):
        l = list( self.pos+(Vector(self.radius-4,0).rotate(a)) for a in range(0,360,int(360/8)))
        return l
    
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
        if self.shot_ready > 0:
            self.shot_ready -= 1
    
    def draw(self,surface): 
        rad2 = Vector(self.radius,self.radius)
        render_image = pg.transform.rotate(self.image,-self.angle)
        draw_center = self.pos - Vector( *render_image.get_size() )/2
        surface.blit(render_image, draw_center)
        
#       "hitbox"
#       for point in self.edge:
#           pg.draw.circle(surface, (0,0,0), point.asInt() , 2)
        
        if self.onPath:
            aSurf = pg.Surface((self.radius*2,)*2, pg.SRCALPHA)
            aSurf.convert_alpha()
            radius = int(self.radius)
            pg.draw.circle(aSurf,(255,0,0,50), rad2, radius)
            pg.draw.circle(aSurf,(255,0,0,250), rad2, radius, 3)
            surface.blit(aSurf,draw_center)
            
    def aim(self,gamemap):
        if self.active and self.shot_ready==0:
            for enemy in gamemap.enemies:
                if (enemy.pos - self.pos).norm() < self.range:
                    self.target = enemy # aquire target
                    self.angle = (self.pos-enemy.pos).angle("deg") # "aim at enemy"
                    self.shoot(gamemap) # fire!!
                    break
            
    def shoot(self,gamemap):
        gamemap.add_bullet(self.pos,self.target)
        self.shot_ready = self.reload_time
        