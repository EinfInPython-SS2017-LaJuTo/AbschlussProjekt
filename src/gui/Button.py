
import pygame as pg

class Button(pg.Rect):
    
    bg_color = None
    line_color = None
    line_width = None
    
    text = None
    text_color = None
    text_size = None

    pressed = False
    
    def __init__(self, left, top, width, height, text="", text_size=None, text_color=pg.Color(0,0,0), bg_color=pg.Color(200,200,200), line_color=pg.Color(0,0,0), line_width=1):
        super().__init__(left, top, width, height)
        self.bg_color = bg_color
        self.line_color = line_color
        self.line_width = line_width
        self.text = text
        self.text_color = text_color
        if text_size == None:
            text_size = height//2
        self.text_size = text_size

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
