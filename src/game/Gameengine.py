from tower.Tower import Tower
from enemy.Enemy import Enemy
from tower.Bullet import Bullet
from map.Map import Map
from imageloader.imageloader import *

class Gameengine():
    # attributes:
        # gamemap
        # towers
        # enemies
        # bullets 
        # tower_types
        
        # money
        
    def __init__(self, global_images, path_data, map_size):
        self.global_images = global_images
        self.gamemap = Map(global_images["grass"],path_data,map_size)
        
        self.towers = []
        self.enemies = []
        self.bullets = []
        
        self.tower_types = {"turret":(global_images["tower_turret"],10,150,10), "fire":(global_images["tower_fire"],30,200,5)}
        
        self.money = 0
        
        self.wavetime = 0
        
    def update(self,dt): # dt := deltatime
        for tower in self.towers:
            if tower.alive:
                tower.update(dt)
                if tower.shooting:
                    self.add_bullet(tower.pos-tower.nozzle, tower.target, tower.shot_strength)
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
        
        self.wavetime += dt
        if self.wavetime > 1000:
            self.add_enemy(global_images["enemy"])
            self.wavetime = 0
            
    def draw(self, surface):
        self.gamemap.draw(surface)
        for tower in self.towers:
            tower.draw(surface)
        for bullet in self.bullets:
            bullet.show(surface)
        for enemy in self.enemies:
            enemy.draw(surface)
            
                
    def add_tower(self,img_path):
        self.towers.append( Tower(self.enemies,self.gamemap.path.subpaths, *self.tower_types["fire"]) )
    def del_tower(self,tower):
        del self.towers[ self.towers.index(tower) ]
    
    def add_bullet(self,pos,target,strength):
        self.bullets.append( Bullet(self.global_images["bullet"],pos,target,strength) )
    def del_bullet(self,bullet):
        del self.bullets[ self.bullets.index(bullet) ]
    
    def add_enemy(self,enemy_image):
        self.enemies.append( Enemy(enemy_image,self.gamemap.path.subpaths[0],speed=15) )
    def del_enemy(self,enemy):
        del self.enemies[ self.enemies.index(enemy) ]