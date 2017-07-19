
import pygame as pg

class Button(pg.Rect):
    
    bg_color = None
    line_color = None
    line_width = None
    pressed = False
    
    def __init__(self, left, top, width, height, bg_color=pg.Color(200,200,200), line_color=pg.Color(0,0,0), line_width=1):
        super().__init__(left, top, width, height)
        self.bg_color = bg_color
        self.line_color = line_color
        self.line_width = line_width

    def check_press(self,x,y):
        if self.collidepoint(x,y):
            self.pressed = True

    def release(self):
        self.pressed = False

    def draw(self, surface):
        if self.pressed:
            surface.fill(self.bg_color-pg.Color(32,32,32), rect=self)
            pg.draw.rect(surface, self.line_color, self, self.line_width)
            pg.draw.rect(surface, self.line_color, self.inflate(-8*self.line_width, -8*self.line_width).move(self.line_width, self.line_width), self.line_width)
        else:
            surface.fill(self.bg_color,rect=self)
            pg.draw.rect(surface, self.line_color, self, self.line_width)
            pg.draw.rect(surface, self.line_color, self.inflate(-8*self.line_width, -8*self.line_width).move(-self.line_width, -self.line_width), self.line_width)
