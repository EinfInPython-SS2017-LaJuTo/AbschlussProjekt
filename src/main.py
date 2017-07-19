#!/usr/bin/env python3

import pygame as pg
import sys
from tower.Tower import Tower
from gui.Button import Button
from map.Map import Map

framerate = 60
tower_path = "../res/tower.png"
background_image_path = "../res/background.png"
path_path = "../res/path_points.txt"

if __name__ == "__main__":
    pg.init()
    background_image = pg.image.load(background_image_path)
    main_surface = pg.display.set_mode((background_image.get_width(),background_image.get_height()))
    clock = pg.time.Clock()
    
    gamemap = Map(path_path)
    gamemap.size = main_surface.get_size()
    gamemap.add_tower(10,10,tower_path)
    gamemap.add_enemy()
    
    while True:
        deltatime = clock.tick(framerate)
        
        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit()
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_q:
                    sys.exit()
            elif e.type == pg.MOUSEBUTTONDOWN:
                gamemap.towers[-1].place_down()
                gamemap.add_enemy()
                
        # all the updating
        gamemap.update()
        
        # all the drawing
        main_surface.blit(background_image,(0,0))
        gamemap.draw(main_surface)

        pg.display.flip()
