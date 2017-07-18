#!/usr/bin/env python3

import pygame as pg

framerate = 60
background_image_path = "res/background.png"

if __name__ == "__main__":
    pg.init()

    background_image = pg.image.load(background_image_path)

    main_surface = pg.display.set_mode((background_image.get_width(),background_image.get_height()))
    
    clock = pg.time.Clock()

    while True:
        deltatime = clock.tick(framerate)
        
        ev = pg.event.poll()
        if ev.type == pg.QUIT:
            break
        elif ev.type == pg.KEYDOWN:
            if ev.key == pg.K_q:
                break
        
        main_surface.blit(background_image,(0,0))
        
        pg.display.flip()

    pg.quit()
