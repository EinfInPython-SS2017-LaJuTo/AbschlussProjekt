import pygame as pg
import gui.Label as Label
import math

class Sidemenu(pg.Rect):

    # atitributes:
        # bg_color
        # towers
        # label_health
        # label_money
        # {pg.Rect}
    
    def __init__(self, left, top, width, height, bg_color, towers):
        super().__init__(self, left, top, width, height)
        self.bg_color = bg_color
        self.towers = towers
        self.label_health = Label(5, 5, self.width, 50)
        self.label_money = Label(5, 55, self.width, 50)
        self.next_tower = None
    
    def check_press(self, pos):
        if self.collidepoint(pos):
            x,y = pos
            for t in towers:
                x_t,y_t = t.pos
                if math.abs(x_t-x) <= t.radius and math.abs(y_t-y) <= t.radius:
                    self.next_tower = None#TODO

    def release(self):
        pass #TODO

    def draw(self, surface):
        surface.fill(self.bg_color, rect=self)

