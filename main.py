#!/usr/bin/env python3

import pygame as pg
from src.tower.Tower import Tower
from src.map.Path import Path

framerate = 60
path_path = "res/path_points.txt"
tower_path = "res/tower.png"
background_image_path = "res/background.png"

if __name__ == "__main__":
    pg.init()
    background_image = pg.image.load(background_image_path)
    main_surface = pg.display.set_mode((background_image.get_width(),background_image.get_height()))
    clock = pg.time.Clock()
    
    path = Path(path_path)
    twr = Tower(10,10,tower_path)
    

    while True:
        deltatime = clock.tick(framerate)
        
        ev = pg.event.poll()
        if ev.type == pg.QUIT:
            break
        elif ev.type == pg.KEYDOWN:
            if ev.key == pg.K_q:
                break
        
        
        main_surface.blit(background_image,(0,0))
        path.drawPath(main_surface)
        twr.draw(main_surface,path.subpaths)

        pg.display.flip()

    pg.quit()
