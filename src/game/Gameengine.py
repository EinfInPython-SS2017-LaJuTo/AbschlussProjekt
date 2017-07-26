from tower.Tower import Tower
from enemy.Enemy import Enemy
from tower.Bullet import Bullet

class Gameengine():
    # attributes:
        # gamemap
        # towers
        # enemies
        # bullets 
        
        # money
        
    def __init__(self, gamemap, image_bullet):
        self.gamemap = gamemap
        
        self.towers = []
        self.enemies = []
        self.bullets = []
        self.image_bullet = image_bullet
        
        self.money = 0
        
    def update(self,dt): # dt := deltatime
        for tower in self.towers:
            if tower.alive:
                tower.update(dt)
                if tower.shooting:
                    self.add_bullet(tower.pos-tower.nozzle, tower.target)
            else:
                del self.towers[self.towers.index(tower)]
                
        for bullet in self.bullets:
            if bullet.alive:
                bullet.update(dt,self.gamemap.size)
            else:
                del self.bullets[self.bullets.index(bullet)]
                
        for enemy in self.enemies:
            if enemy.alive:
                enemy.update(self.gamemap.path.subpaths,dt)
            else:
                self.money += enemy.value
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
        self.bullets.append( Bullet(self.image_bullet,pos,target) )
    def del_bullet(self,bullet):
        del self.bullets[ self.bullets.index(bullet) ]
    
    def add_enemy(self,enemy_image):
        self.enemies.append( Enemy(enemy_image,self.gamemap.path.subpaths[0],speed=15) )
    def del_enemy(self,enemy):
        del self.enemies[ self.enemies.index(enemy) ]