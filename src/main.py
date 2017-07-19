#!/usr/bin/env python3

import pygame as pg
from tower.Tower import Tower
from map.Path import Path
from gui.Button import Button

framerate = 60
path_path = "../res/path_points.txt"
tower_path = "../res/tower.png"
background_image_path = "../res/background.png"

if __name__ == "__main__":
    pg.init()
    background_image = pg.image.load(background_image_path)
    main_surface = pg.display.set_mode((background_image.get_width(),background_image.get_height()))
    clock = pg.time.Clock()
    
    path = Path(path_path)
    twr = Tower(10,10,tower_path)
    btn = Button(0,0,200,100)
    

    while True:
        deltatime = clock.tick(framerate)
        
        for e in pg.event.get():
            if e.type == pg.QUIT:
                pg.quit()
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_q:
                    pg.quit()
            elif e.type == pg.MOUSEBUTTONDOWN:
                twr.active = True
                
                
        # all the updating
        twr.update()
        
        # all the drawing
        main_surface.blit(background_image,(0,0))
        path.drawPath(main_surface)
        twr.draw(main_surface,path.subpaths)
        btn.draw(main_surface)


        pg.display.flip()
