#!/usr/bin/env python3

import pygame as pg

background_image_path = "res/background.png"

def main():
    pg.init()

    background_image = pg.image.load(background_image_path)

    main_surface = pg.display.set_mode((background_image.get_width(),background_image.get_height()))

    while True:
        ev = pg.event.poll()  
        if ev.type == pg.QUIT:
            break
        elif ev.type == pg.KEYDOWN:
            if ev.key == ord('q'):
                break
        
        main_surface.blit(background_image,(0,0))
        
        pg.display.flip()

    pg.quit()     # Once we leave the loop, close the window.

main()
