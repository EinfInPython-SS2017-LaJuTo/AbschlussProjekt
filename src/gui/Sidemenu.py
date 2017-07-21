import pygame as pg

class Sidemenu(pg.Rect):
    # attributes:
        # bg_color
        # {pg.Rect}
    
    def __init__(self, left, top, width, height, bg_color):
        self.width = width
        self.height = height
        self.bg_color = bg_color
    
    def draw(self, surface):
        surface.fill(self.bg_color, rect=self
