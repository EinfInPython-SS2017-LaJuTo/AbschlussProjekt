from map.Path import Path

class Map():
    def __init__(self,path_path):
        self.towers = []
        self.enemies = []
        self.path = Path(path_path)
    
    def getPaths(self):
        return self.path.subpaths
    
    def draw(self, surface):
        self.path.draw(surface)
        for tower in self.towers:
            tower.draw(surface)
        #for enemy in self.enemies:
        #    enemy.draw(surface)