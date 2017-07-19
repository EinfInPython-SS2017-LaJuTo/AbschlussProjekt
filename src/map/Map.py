from map.Path    import Path
from tower.Tower import Tower
from enemy.Enemy import Enemy

class Map():
    def __init__(self,path_path):
        self.towers = []
        self.enemies = []
        self.path = Path(path_path)
    
    def getPaths(self):
        return self.path.subpaths
    
    def update(self):
        for tower in self.towers:
            tower.update(self.getPaths())
        for enemy in self.enemies:
            enemy.update(self.getPaths())
    
    def draw(self, surface):
        self.path.draw(surface)
        for tower in self.towers:
            tower.draw(surface)
        for enemy in self.enemies:
            enemy.draw(surface)
        
        
    def add_tower(self,x,y,img_path):
        self.towers.append( Tower(x,y,img_path) )

    def del_tower(self,tower):
        pass
    
    def add_enemy(self):
        self.enemies.append( Enemy(self.getPaths()[0]) )