
import pygame as pg

class Label(pg.Rect):
    # attributes:
        # bg_color
        # background
        # line_color
        # line_width
        # text
        # text_color
        # text_size
        # {pg.Rect}
    
    def __init__(self, left, top, width, height, text="", text_pos=None, text_size=None, text_color=pg.Color(0,0,0), bg_color=pg.Color(200,200,200), background=None, line_color=pg.Color(0,0,0), line_width=1):
        super().__init__(left, top, width, height)
        self.bg_color = bg_color
        self.background = background
        self.line_color = line_color
        self.line_width = line_width
        self.text = text
        self.text_color = text_color
        self.text_size = text_size
        self.text_pos = text_pos

    def draw(self, surface, delta_x=0, delta_y=0):
        surface.fill(self.bg_color, rect=self)
        pg.draw.rect(surface, self.line_color, self, self.line_width)
        if self.background != None:
            if self.background.get_width() > self.width or self.background.get_height() > self.height:
                fitted_rect = self.background.get_rect().fit(self)
                self.background = pg.transform.scale(self.background,(fitted_rect.width,fitted_rect.height))
            surface.blit(self.background, dest=self.background.get_rect(center=self.move(delta_x,delta_y).center))
        self._draw_text(surface,delta_x,delta_y)

    def _draw_text(self, surface, delta_x=0, delta_y=0):
        text_font = None
        text_renders = []
        if self.text != "": # Only render the text if necessary
            text_lines = self.text.splitlines()
            text_font = None
            if self.text_size != None:
                text_font = pg.font.Font(None,self.text_size)
            else:
                text_font = pg.font.Font(None,self.height//(len(text_lines)+1)) # TODO: Not a great solution...
            for l in self.text.splitlines():
                text_renders.append(text_font.render(l, True, self.text_color))
        if len(text_renders) > 0:
            total_text_height = 0
            max_text_width = 0
            for r in text_renders:
                total_text_height += r.get_height()
                if r.get_width() > max_text_width:
                    max_text_width = r.get_width()
            full_text = pg.Surface((max_text_width, total_text_height),pg.SRCALPHA)
            curr_y = 0
            if self.text_pos == None:
                for r in text_renders:
                    full_text.blit(r, r.get_rect(centerx=full_text.get_rect().centerx).move(0,curr_y))
                    curr_y += r.get_height()
                surface.blit(full_text,full_text.get_rect(center=self.center).move(delta_x, delta_y))
            else:
                for r in text_renders:
                    full_text.blit(r, r.get_rect().move(0,curr_y))
                    curr_y += r.get_height()
                surface.blit(full_text,pg.Rect(self.text_pos,(0,0)).move(self.left,self.top).move(delta_x, delta_y))

