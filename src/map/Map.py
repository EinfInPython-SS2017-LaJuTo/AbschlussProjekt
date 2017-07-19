from map.Path    import Path
from tower.Tower import Tower
from enemy.Enemy import Enemy
from tower.Bullet import Bullet
import pygame as pg

class Map():
    # attributes:
        # size
        # towers
        # enemies
        # path
        # bullets
        
    def __init__(self,image_path,path_path):
        self.size = (0,0)
        self.tilesize = 50
        self.towers = []
        self.enemies = []
        self.bullets = []
        self.path = Path(path_path)
        self.bg_image = pg.image.load(image_path)
        self.bg_image = pg.transform.scale(self.bg_image, (self.tilesize,)*2)
    
    def getPaths(self):
        return self.path.subpaths
    
    def update(self):
        for tower in self.towers:
            tower.update(self.getPaths())
            tower.aim(self)
        for bullet in self.bullets:
            bullet.update(self)
        for enemy in self.enemies:
            enemy.update(self)
        
    
    def draw(self, surface):
        # background_image
        for x in range(int(self.size[0]/self.tilesize)):
            for y in range(int(self.size[1]/self.tilesize)):
                surface.blit(self.bg_image, (x*self.tilesize,y*self.tilesize))
        # path
        self.path.draw(surface)
        # objects
        for tower in self.towers:
            tower.draw(surface)
        for bullet in self.bullets:
            bullet.show(surface)
        for enemy in self.enemies:
            enemy.draw(surface)
        
        
    def add_tower(self,x,y,img_path):
        self.towers.append( Tower(x,y,img_path) )

    def del_tower(self,tower):
        pass
    
    def add_bullet(self,pos,target):
        self.bullets.append( Bullet(pos,target) )
        
    def del_bullet(self,bullet):
        del self.bullets[ self.bullets.index(bullet) ]
    
    def add_enemy(self,enemy_image):
        self.enemies.append( Enemy(enemy_image,self.getPaths()[0]) )
        
    def del_enemy(self,enemy):
        del self.enemies[ self.enemies.index(enemy) ]