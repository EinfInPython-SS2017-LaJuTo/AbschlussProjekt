
import pygame as pg

from gui.Label import Label

class Button(Label):
    
    pressed = False
    
    # __init__ is inherited from Label

    def check_press(self,x,y):
        if self.collidepoint(x,y):
            self.pressed = True

    def release(self):
        self.pressed = False

    def draw(self, surface):
        text_font,text_render = None, None
        if self.text != "":
            text_font = pg.font.Font(None,self.text_size)
            text_render = text_font.render(self.text, True, self.text_color)
        if self.pressed:
            surface.fill(self.bg_color-pg.Color(32,32,32), rect=self)
            pg.draw.rect(surface, self.line_color, self, self.line_width)
            pg.draw.rect(surface, self.line_color, self.inflate(-8*self.line_width, -8*self.line_width).move(self.line_width, self.line_width), self.line_width)
            if text_font != None and text_render != None:
                surface.blit(text_render,text_render.get_rect(center=self.center).move(self.line_width,self.line_width))
        else:
            surface.fill(self.bg_color,rect=self)
            pg.draw.rect(surface, self.line_color, self, self.line_width)
            pg.draw.rect(surface, self.line_color, self.inflate(-8*self.line_width, -8*self.line_width).move(-self.line_width, -self.line_width), self.line_width)
            if text_font != None and text_render != None:
                surface.blit(text_render,text_render.get_rect(center=self.center).move(-self.line_width,-self.line_width))
