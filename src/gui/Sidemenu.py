import pygame as pg
from gui.Label import Label
from gui.Button import Button

# TODO:
#   IMPORTANT
#   Wave-Nr.-Display
#   Wave-countdown-Display (to let player know, how long until next wave)
#   
#   OPTIONAL
#   Button to immediately send next wave
#   Wave-Preview (how many enemies of what kind)

class Sidemenu(pg.Rect):

    # atitributes:
        # bg_color
        # label_health
        # label_money
        # label_wave
        # label_timeleft
        # {pg.Rect}

        # gameengine   # A reference to the gameengine to call add_tower and access the tower_types

        # tower_keys   # A sorted list of tower_types.keys() from the gameengine
        # tower_buttons
        # tower_cost_labels
    # constants:
        # _label_height
        # _label_y_margin
        # _label_fontsize
        # _tower_y_start
        # _tower_wh
        # _tower_cost_fontsize

    def __init__(self, left, top, width, height, bg_color, gameengine):
        self._label_height = 40
        self._label_y_margin = 5
        self._label_fontsize = 30
        self._tower_wh = width//2
        self._tower_cost_fontsize = 25

        super().__init__(left, top, width, height)
        self.bg_color = bg_color
        self.label_health = Label(self.left, self.top + self._label_y_margin, width, self._label_height, text_size=self._label_fontsize)
        self.label_money = Label(self.left, self.label_health.bottom, self.width, self._label_height, text_size=self._label_fontsize)
        self.label_wave = Label(self.left, self.label_money.bottom+self._label_y_margin, self.width, self._label_height, text_size=self._label_fontsize)
        self.label_timeleft = Label(self.left, self.label_wave.bottom, self.width, self._label_height, text_size=self._label_fontsize)
        
        self._tower_y_start = self.label_timeleft.bottom + self._label_y_margin
        
        self.gameengine = gameengine
        self.tower_keys = sorted(self.gameengine.tower_types.keys(),key=lambda s:self.gameengine.tower_types[s][4])
        self.tower_buttons = {}
        self.tower_cost_labels = {}
        x = self.left
        y = self._tower_y_start
        for k in self.tower_keys:
            self.tower_buttons[k] = Button(x,y,self._tower_wh, self._tower_wh, background=pg.transform.scale(self.gameengine.tower_types[k][0], (self._tower_wh,self._tower_wh)))
            self.tower_cost_labels[k] = Label(x,y+self.tower_buttons[k].height, self._tower_wh,
                                              self._tower_cost_fontsize+2, text="$"+str(self.gameengine.tower_types[k][4]), text_size=self._tower_cost_fontsize)
            if x == self.left:
                x = self.left+self._tower_wh
            else:
                x = self.left
                y += self.tower_buttons[k].height+self.tower_cost_labels[k].height
    
    def check_press(self, pos):
        if self.collidepoint(pos):
            for k in self.tower_keys:
                if self.tower_buttons[k].check_press(pos):
                    self.gameengine.add_tower(k)

    def release(self):
        for k in self.tower_keys:
            self.tower_buttons[k].release()

    def draw(self, surface):
        if self.gameengine.health <= 0:
            surface.fill(self.bg_color, rect=self)
        else:
            surface.fill(self.bg_color, rect=self)
            self.label_health.text = "HP " + str(self.gameengine.health)
            self.label_money.text = "$  " + str(self.gameengine.money)
            self.label_wave.text = "Wave " + str(self.gameengine.wavemanager.current) + "/" + str(self.gameengine.wavemanager.max)
            self.label_timeleft.text = "Next " + str(self.gameengine.wavemanager.duration-self.gameengine.wavemanager.wavetick) + "s"
            self.label_health.draw(surface)
            self.label_money.draw(surface)
            self.label_wave.draw(surface)
            self.label_timeleft.draw(surface)
            
            for k in self.tower_keys:
                self.tower_buttons[k].draw(surface)
                self.tower_cost_labels[k].draw(surface)

