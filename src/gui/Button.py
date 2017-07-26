
import pygame as pg

from gui.Label import Label

#TODO: Only inner part as Label for propper image scaling!

class Button(Label):
    # attributes:
        # pressed
        # {Label}
    
    pressed = False
    
    # __init__ is inherited from Label

    def check_press(self,pos):
        if self.collidepoint(*pos):
            self.pressed = True

    def release(self):
        self.pressed = False

    def draw(self, surface):
        if self.pressed:
#            surface.fill(self.bg_color-pg.Color(32,32,32), rect=self)
#            pg.draw.rect(surface, self.line_color, self, self.line_width)
            super().draw(surface,self.line_width, self.line_width)
            pg.draw.rect(surface, self.line_color, self.inflate(-8*self.line_width, -8*self.line_width).move(self.line_width, self.line_width), self.line_width)
        else:
            surface.fill(self.bg_color,rect=self)
            super().draw(surface, -self.line_width, -self.line_width)
            pg.draw.rect(surface, self.line_color, self.inflate(-8*self.line_width, -8*self.line_width).move(-self.line_width, -self.line_width), self.line_width)
