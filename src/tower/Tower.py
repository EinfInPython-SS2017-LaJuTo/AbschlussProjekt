import pygame as pg

class Tower:
    # attributes:
        # pos
        # radius
        # range
        # img
        # active
        # onPath
        
    def __init__(self,x,y,img_path):
        self.pos = (x,y)
        self.radius = 20
        self.range  = 50
        self.img = pg.image.load(img_path)
        self.img = pg.transform.scale(self.img, (self.radius*2,)*2)
        
        self.active = False
        self.onPath = False
        self.edge = [(0,0)]*9
        self.setEdgePoints()
        
    def setEdgePoints(self):
        ''' Wenn du eine bessere Idee hierfür hast, nur zu! :) '''
        self.edge[0] = (self.pos[0],self.pos[1]-self.radius)  # top
        self.edge[1] = (self.pos[0],self.pos[1]+self.radius)  # bottom
        self.edge[2] = (self.pos[0]-self.radius,self.pos[1])  # left
        self.edge[3] = (self.pos[0]+self.radius,self.pos[1])  # right
        self.edge[4] = (self.pos[0]-self.radius/2,self.pos[1]-self.radius/2)  # topleft
        self.edge[5] = (self.pos[0]+self.radius/2,self.pos[1]-self.radius/2)  # topright
        self.edge[6] = (self.pos[0]-self.radius/2,self.pos[1]+self.radius/2)  # bottomleft
        self.edge[7] = (self.pos[0]+self.radius/2,self.pos[1]+self.radius/2)  # bottomright
        self.edge[8] = self.pos
        
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
        self.setEdgePoints()
        self.onPath = self.isOnPath(path)
        if not self.active:
            self.pos = pg.mouse.get_pos()
        elif self.active:
            pass
    
    def draw(self,surface): 
        surface.blit(self.img, (self.pos[0]-self.radius, self.pos[1]-self.radius))
        #for point in self.edge:
        #    pg.draw.circle(surface, (0,0,0), (int(point[0]),int(point[1])), 2)
        if self.onPath:
            aSurf = pg.Surface((self.radius*2,)*2, pg.SRCALPHA)
            aSurf.convert_alpha()
            radius = int(self.radius)
            pg.draw.circle(aSurf,(255,0,0,50), (radius,radius), radius)
            pg.draw.circle(aSurf,(255,0,0,250), (radius,radius), radius, 3)
            surface.blit(aSurf,(self.pos[0]-self.radius, self.pos[1]-self.radius))
            
    def aim(self,gamemap):
        if self.active:
            for enemy in gamemap.enemies:
                if self.norm(self.subtract(enemy.pos, self.pos)) < self.range:
                    self.shoot(gamemap,enemy)
                    break
            
    def shoot(self,gamemap,target):
        gamemap.add_bullet(self.pos,target)
        
    ''' WIRD DURCH ORDENTLICHE VEKTOR-KLASSE ERSETZT'''
    def subtract(self, tuple1, tuple2):
        return (tuple1[0]-tuple2[0], tuple1[1]-tuple2[1])
    def norm(self,tuple1):
        return ( tuple1[0]**2 + tuple1[1]**2)**0.5