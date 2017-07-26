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
    
    def check_press(self, pos):
        x,y = pos
        for t in towers:
            x_t,y_t = t.pos
            if math.abs(x_t-x) <= t.radius and math.abs(y_t-y) <= t.radius:
                pass # TODO: Create new tower

    def release(self):
        pass

    def draw(self, surface):
        surface.fill(self.bg_color, rect=self)

