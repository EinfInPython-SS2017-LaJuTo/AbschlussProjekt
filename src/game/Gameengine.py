from tower.Tower import Tower
from enemy.Enemy import Enemy
from tower.Bullet import Bullet

class Gameengine():
    def __init__(self, gamemap):
        self.gamemap = gamemap
        
        self.towers = []
        self.enemies = []
        self.bullets = []
        
    def update(self,dt): # dt := deltatime
        for tower in self.towers:
            if tower.alive == True:
                tower.update(dt)
                if tower.shooting:
                    self.add_bullet(tower.pos-tower.nozzle, tower.target)
            else:
                del self.towers[self.towers.index(tower)]
                
        for bullet in self.bullets:
            if bullet.alive == True:
                bullet.update(dt,self.gamemap.size)
            else:
                del self.bullets[self.bullets.index(bullet)]
                
        for enemy in self.enemies:
            if enemy.alive == True:
                enemy.update(self.gamemap.path.subpaths,dt)
            else:
                del self.enemies[self.enemies.index(enemy)]
            
    def draw(self, surface):
        self.gamemap.draw(surface)
        for tower in self.towers:
            tower.draw(surface)
        for bullet in self.bullets:
            bullet.show(surface)
        for enemy in self.enemies:
            enemy.draw(surface)
            
                
    def add_tower(self,img_path):
        self.towers.append( Tower(img_path, self.enemies, self.gamemap.path.subpaths) )
    def del_tower(self,tower):
        del self.towers[ self.towers.index(tower) ]
    
    def add_bullet(self,pos,target):
        self.bullets.append( Bullet(pos,target) )
    def del_bullet(self,bullet):
        del self.bullets[ self.bullets.index(bullet) ]
    
    def add_enemy(self,enemy_image):
        self.enemies.append( Enemy(enemy_image,self.gamemap.path.subpaths[0] , 0.1) )
    def del_enemy(self,enemy):
        del self.enemies[ self.enemies.index(enemy) ]