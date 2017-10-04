import pygame as pg
from gui.Label import Label
from gui.Button import Button
import math

class Sidemenu(pg.Rect):

    # atitributes:
        # bg_color
        # label_health
        # label_money
        # {pg.Rect}

        # gameengine   # A reference to the gameengine to call add_tower and access the tower_types

        # tower_keys   # A sorted list of tower_types.keys() from the gameengine
        # tower_buttons
        # tower_cost_labels
    # constants:
        # _label_height
        # _label_y_margin
        # _tower_y_start
        # _tower_wh
        # _tower_cost_fontsize

    def __init__(self, left, top, width, height, bg_color, gameengine):
        self._label_height = 50
        self._label_y_margin = 5
        self._tower_y_start = 2*(self._label_height+self._label_y_margin)
        self._tower_wh = width//2
        self._tower_cost_fontsize = 20

        super().__init__(left, top, width, height)
        self.bg_color = bg_color
        self.label_health = Label(self.left, self.top + self._label_y_margin, width, self._label_height)
        self.label_money = Label(self.left, self.top + self._label_height + self._label_y_margin, self.width, self._label_height)
        self.gameengine = gameengine
        self.tower_keys = sorted(self.gameengine.tower_types.keys(),key=lambda s:self.gameengine.tower_types[s][4])
        self.tower_buttons = {}
        self.tower_cost_labels = {}
        x = self.left
        y = self._tower_y_start
        for k in self.tower_keys:
            self.tower_buttons[k] = Button(x,y,self._tower_wh, self._tower_wh, background=pg.transform.scale(self.gameengine.tower_types[k][0], (self._tower_wh,self._tower_wh)))
            self.tower_cost_labels[k] = Label(x,y+self.tower_buttons[k].height, self._tower_wh,
                                              self._tower_cost_fontsize+2, text="$"+str(self.gameengine.tower_types[k][4]), text_size=self._tower_cost_fontsize)
            if x == self.left:
                x = self.left+self._tower_wh
            else:
                x = self.left
                y += self.tower_buttons[k].height+self.tower_cost_labels[k].height
    
    def check_press(self, pos):
        if self.collidepoint(pos):
            for k in self.tower_keys:
                if self.tower_buttons[k].check_press(pos):
                    self.gameengine.add_tower(k)

    def release(self):
        for k in self.tower_keys:
            self.tower_buttons[k].release()

    def draw(self, surface):
        surface.fill(self.bg_color, rect=self)
        self.label_health.text = "HP "+str(self.gameengine.health)
        self.label_money.text = "$  "+str(self.gameengine.money)
        self.label_health.draw(surface)
        self.label_money.draw(surface)
        

        for k in self.tower_keys:
            self.tower_buttons[k].draw(surface)
            self.tower_cost_labels[k].draw(surface)

