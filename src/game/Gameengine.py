from tower.Tower import Tower
from enemy.Enemy import Enemy
from tower.Bullet import Bullet
from map.Map import Map
from imageloader.imageloader import global_images
from lib.Vector import Vector
from wavemanager.wavemanager import Wavemanager

class Gameengine():
    # attributes:
        # gamemap
        # towers
        # idle_tower
        # enemies
        # bullets 
        # tower_types, bullet_types, enemy_types
        # money
        # wavetime
        
    def __init__(self, path_data, map_size):
        self.gamemap = Map(global_images["grass"],path_data,map_size)
        
        self.towers = []
        self.idle_tower = None
        self.enemies = []
        self.bullets = []
        
        # image, shot_frequency, shot_range, shot_strength, cost
        self.tower_types = {"turret":(global_images["tower_turret"],5,200,10,150), 
                            "gatling":(global_images["tower_gatling"], 10,250, 5,250),
                            "poison":(global_images["tower_poison"], 1,150,20,200)}
        self.bullet_types = {"turret": global_images["turret"], 
                             "gatling": global_images["gatling"],
                             "poison": global_images["poison"]}
        # image, speed, health, value
        self.enemy_types = {"normal":(global_images["enemy"],7,40,5),
                            "strong":(global_images["strong_enemy"],4,80,20)}
        
        self.money = 150
        self.health = 100
        
        self.wavemanager = Wavemanager()
        
    def update(self,dt): # dt := deltatime
        # handle the idle_tower
        if self.idle_tower != None:
            self.checkIdleTower()
            self.idle_tower.update(dt)
        # handle the tower-list
        for tower in self.towers:
            if tower.alive:
                tower.update(dt)
                if tower.shooting:
                    self.add_bullet(tower.pos-tower.nozzle, tower.target,tower.shot_strength, tower.tower_type)
            else:
                del self.towers[self.towers.index(tower)]
                
        # handle the bullet-list
        for bullet in self.bullets:
            if bullet.alive:
                bullet.update(dt,self.gamemap.size)
            else:
                del self.bullets[self.bullets.index(bullet)]
                
        # handle the enemy-list
        for enemy in self.enemies:
            if enemy.alive:
                enemy.update(self.gamemap.path.subpaths,dt)
            else:
                if enemy.health <= 0:
                    self.money += enemy.value
                else:
                    self.health -= enemy.value
                del self.enemies[self.enemies.index(enemy)]
                
        # spawn enemies
        order = self.wavemanager.update(dt)
        if order != "hold" and order != None:
            self.add_enemy(order)
        
        #self.wavetime += dt
        #if self.wavetime > 1000:
        #    self.wavetime = 0 
        #    self.wavecount += 1
        #    if self.wavecount % 5 == 0:
        #        self.add_enemy("strong")
        #        #TODO:More enemies!
        #    else:
        #        self.add_enemy("normal")
            
            
    def draw(self, surface):
        self.gamemap.draw(surface)
        for tower in self.towers:
            tower.draw(surface)
        for bullet in self.bullets:
            bullet.show(surface)
        for enemy in self.enemies:
            enemy.draw(surface)
        if self.idle_tower != None :
            self.idle_tower.draw(surface)
        if self.health <= 0:
            surface.blit(global_images["game_over"], (0,0))
            self.health = 0
                
    def add_tower(self,tower_type):
        #self.towers.append( Tower(self.enemies,self.gamemap.path.subpaths, tower_type,*self.tower_types[tower_type]) )
        self.idle_tower = Tower(self.enemies, tower_type,*self.tower_types[tower_type])
    def del_tower(self,tower):
        del self.towers[ self.towers.index(tower) ]
    
    def add_bullet(self,pos,target,strength, bullet_type):
        self.bullets.append( Bullet(pos,target,strength, self.bullet_types[bullet_type]) )
    def del_bullet(self,bullet):
        del self.bullets[ self.bullets.index(bullet) ]
    
    def add_enemy(self,enemy_type):
        self.enemies.append( Enemy(self.gamemap.path.subpaths[0], *self.enemy_types[enemy_type]) )
    def del_enemy(self,enemy):
        del self.enemies[ self.enemies.index(enemy) ]
        
    def placeIdleTower(self):
        if self.idle_tower != None:
            if self.idle_tower.placeable:
                self.money -= self.idle_tower.cost
                self.idle_tower.idle = False
                self.towers.append(self.idle_tower)
                self.idle_tower = None
            
    def checkIdleTower(self):
        self.idle_tower.placeable = True
        # check if player has enough money
        if self.idle_tower.cost > self.money:
            self.idle_tower.placeable = False
            return
        
        # check if it's on the gamemap
        for point in self.idle_tower.edge:
            if not self.gamemap.collidepoint(point):
                self.idle_tower.placeable = False
                return
                    
        # check if it's on the paths
        for subpath in self.gamemap.path.subpaths:
            for point in self.idle_tower.edge:
                if subpath.collidepoint(point):
                    self.idle_tower.placeable = False
                    return
        # check if it's on other towers
        for other in self.towers:
            if Vector.norm(other.pos-self.idle_tower.pos) <= other.radius+self.idle_tower.radius:
                self.idle_tower.placeable = False # idle_tower is on another tower though
                return
                
                
                
