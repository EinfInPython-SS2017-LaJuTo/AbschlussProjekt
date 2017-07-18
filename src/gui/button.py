
import pygame as pg

def Button(pg.Rect):
    
    bg_color = pg.Color.Color(255,255,255,255)
    line_color = pg.Color.Color(0,0,0,255)
    line_width = 1
    
    def __init__(self, left, top, width, height, bg_color, line_color, line_width):
        super().__init__(self,left,top,width,height)


    def click(self):
        pass

    def release(self):
        pass

    def draw(self,surface):
        surface.fill(bg_color,rect=self)
        pg.draw.rect(
