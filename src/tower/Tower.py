import pygame as pg
from lib.Vector import Vector

class Tower:
    # attributes:
        # tower_type
        
        # pos
        # nozzle_original
        # nossle    (point of exit for the bullets) (relative to pos)
        # radius    (size of tower-image)
        
        # image
        
        # alive
        # idle
        # palceable
        # edge      (points that make up hitbox)
        
        # target
        # angle
        
        # shot_frequency
        # shot_dt   (time since last shot)
        # shooting
        # shot_range 
        
    # references:
        # enemies       (from gamemap)
        # subpaths      (from gamemap)
    
    def __init__(self, enemies, tower_type,image,shot_frequency,shot_range,shot_strength):
        self.tower_type = tower_type
        self.pos = Vector(0,0)
        self.radius = 25
        self.nozzle_original = Vector(0,self.radius-5) # sorry, but has to be hardcoded
        self.nozzle = self.nozzle_original
        
        self.image = image
        self.image = pg.transform.scale(self.image, (self.radius*2,)*2) # scale the image to size

        self.alive = True
        self.idle = True
        self.placeable = False
        self.edge = self.setEdgePoints()
        
        self.target = None
        self.angle = 0
        
        self.shot_range         = shot_range
        self.shot_frequency     = shot_frequency
        self.shot_strength      = shot_strength
        self.shot_dt = 0
        self.shooting = False
        
        
        self.enemies = enemies
        
    def setEdgePoints(self):
        l = list( self.pos+(Vector(self.radius-4,0).rotate(a)) for a in range(0,360,int(360/8)))
        return l
            
    def update(self,dt):
        if self.idle:
            self.edge = self.setEdgePoints()
            self.pos = Vector(pg.mouse.get_pos()[0],pg.mouse.get_pos()[1])
        else:
            self.aim(dt) # doesn't aim, if not placed down
    
    def aim(self,dt):
        if self.shooting: self.shooting = False
        for enemy in self.enemies:
            if (enemy.pos - self.pos).norm() < self.shot_range:
                self.target = enemy # aquire target
                self.angle = (self.pos-enemy.pos).angle("deg")  # "aim at enemy"
                self.nozzle = self.nozzle_original.rotate(self.angle)
                
                if self.shot_dt >= 1000/self.shot_frequency:    # "may I shoot?"
                    self.shooting = True                        # fire!!
                    self.shot_dt = 0
                else:
                    self.shot_dt += dt                          # count time since last shot
                break
        
    def draw(self,surface): 
        rad2 = Vector(self.radius,self.radius)
        
        if self.idle:
            surf = pg.Surface((self.shot_range*2,)*2, pg.SRCALPHA)
            pg.draw.circle(surf, (0,0,255,50), (self.shot_range,)*2, self.shot_range)
            surface.blit(surf, self.pos-(self.shot_range,)*2)
            pg.draw.circle(surface, (0,0,255), self.pos, self.shot_range,3)
        
        render_image = pg.transform.rotozoom(self.image,-self.angle,1)
        draw_center = self.pos - Vector( *render_image.get_size() )/2
        surface.blit(render_image, draw_center)
        
#       "hitbox"
#       for point in self.edge:
#           pg.draw.circle(surface, (0,0,0), point.asInt() , 2)
        
        if self.placeable:
            aSurf = pg.Surface((self.radius*2,)*2, pg.SRCALPHA)
            aSurf.convert_alpha()
            radius = int(self.radius)
            pg.draw.circle(aSurf,(255,0,0,50), rad2, radius)
            pg.draw.circle(aSurf,(255,0,0,250), rad2, radius, 3)
            surface.blit(aSurf,draw_center)
            
