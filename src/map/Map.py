from map.Path    import Path
from tower.Tower import Tower
from enemy.Enemy import Enemy
from tower.Bullet import Bullet

class Map():
    # attributes:
        # size
        # towers
        # enemies
        # path
        # bullets
        
    def __init__(self,path_path):
        self.size = (0,0)
        self.towers = []
        self.enemies = []
        self.bullets = []
        self.path = Path(path_path)
    
    def getPaths(self):
        return self.path.subpaths
    
    def update(self):
        for tower in self.towers:
            tower.update(self.getPaths())
            tower.aim(self)
        for bullet in self.bullets:
            bullet.update(self)
        for enemy in self.enemies:
            enemy.update(self.getPaths())
        
    
    def draw(self, surface):
        self.path.draw(surface)
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
    
    def add_enemy(self):
        self.enemies.append( Enemy(self.getPaths()[0]) )