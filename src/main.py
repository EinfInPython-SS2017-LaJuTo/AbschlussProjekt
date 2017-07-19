#!/usr/bin/env python3

import pygame as pg
from tower.Tower import Tower
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
    twr = Tower(10,10,tower_path)
    

    while True:
        deltatime = clock.tick(framerate)
        
        for e in pg.event.get():
            #print(e)
            if e.type == pg.QUIT:
                pg.quit()
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_q:
                    pg.quit()
            elif e.type == pg.MOUSEBUTTONDOWN:
                twr.place_down()
                
                
        # all the updating
        twr.update()
        
        # all the drawing
        main_surface.blit(background_image,(0,0))
        gamemap.draw(main_surface)
        twr.draw(main_surface,gamemap.getPaths())

        pg.display.flip()
