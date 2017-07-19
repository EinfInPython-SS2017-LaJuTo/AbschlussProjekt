
import pygame as pg

class Button(pg.Rect):
    
    bg_color = None
    line_color = None
    line_width = None
    pressed = False
    
    def __init__(self, left, top, width, height, bg_color=pg.Color(255,255,255,255), line_color=pg.Color(0,0,0,255), line_width=1):
        super().__init__(left,top,width,height)
        self.bg_color = bg_color
        self.line_color = line_color
        self.line_width = line_width

    def press(self):
        self.pressed = True

    def release(self):
        self.pressed = False

    def draw(self,surface):
        surface.fill(self.bg_color,rect=self)
        pg.draw.rect(surface,self.line_color,self,self.line_width)
        pg.draw.rect(surface, self.line_color, self.inflate(-4*self.line_width, -4*self.line_width), self.line_width)
