import pygame as pg
from gui.Label import Label
import math

class Sidemenu(pg.Rect):

    # atitributes:
        # bg_color
        # label_health
        # label_money
        # {pg.Rect}

        # gameengine   # A reference to the gameengine to call add_tower and access the tower_types

        # tower_keys   # A sorted list of tower_types.keys() from the gameengine
        # tower_images # A dictionary
    # constants:
        # _label_height
        # _label_y_margin
        # _tower_y_start
        # _tower_wh

    def __init__(self, left, top, width, height, bg_color, gameengine):
        self._label_height = 50
        self._label_y_margin = 5
        self._tower_y_start = 2*(self._label_height+self._label_y_margin)
        self._tower_wh = width//2

        super().__init__(left, top, width, height)
        self.bg_color = bg_color
        self.label_health = Label(self.left, self.top + self._label_y_margin, width, self._label_height)
        self.label_money = Label(self.left, self.top + self._label_height + self._label_y_margin, self.width, self._label_height)
        self.gameengine = gameengine
        self.tower_keys = sorted(self.gameengine.tower_types.keys())
        self.tower_images = {}
        for k in self.tower_keys:
            self.tower_images[k] = pg.transform.scale(self.gameengine.tower_types[k][0], (self._tower_wh,self._tower_wh))
    
    def check_press(self, pos):
        if self.collidepoint(pos):
            x,y = pos
            index = ((y-self._tower_y_start)//(self._tower_wh))*2 + ((x-self.left) >= self._tower_wh) # Calculating the index in tower_keys 
            if index>=0 and index < len(self.tower_keys):
                self.gameengine.add_tower(self.tower_keys[index])



    def release(self):
        pass

    def draw(self, surface):
        surface.fill(self.bg_color, rect=self)
        self.label_health.text = "HP "+str(self.gameengine.health)
        self.label_money.text = "$  "+str(self.gameengine.money)
        self.label_health.draw(surface)
        self.label_money.draw(surface)
        
        x = self.left
        y = self._tower_y_start

        for k in self.tower_keys:
            surface.blit(self.tower_images[k],(x,y))

            if x == self.left:
                x = self.left+self._tower_wh
            else:
                x = self.left
                y += self._tower_wh
