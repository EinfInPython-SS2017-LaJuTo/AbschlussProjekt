#!/usr/bin/env python3

import pygame as pg
import sys
from game.Gameengine import Gameengine
from gui.Sidemenu import Sidemenu
# import level?
# import wave?
# non-steering bullets ?

framerate = 60
path_data   = "../res/path_points.txt" # dann in map oder level je nachdem ...
# wave_data   = "../res/.txt" # Lars' Wavemanager!

if __name__ == "__main__":
    pg.init()
    pg.display.set_caption("TowerDefense_KIT_PY'17")
    window_size = (1280,720)
    #main_surface = pg.display.set_mode(window_size, pg.FULLSCREEN)
    main_surface = pg.display.set_mode(window_size)
    clock = pg.time.Clock()
    
    gameengine = Gameengine( path_data,(window_size[0]-100,window_size[1]))
    
    sidemenu = Sidemenu(window_size[0]-100,0,100,window_size[1], pg.Color(128,128,128), gameengine)
    
    running = True
    doublespeed = False

    while True:
        deltatime = clock.tick(framerate)
        if gameengine.health <= 0 or not running:
            deltatime = 0
        if doublespeed:
            deltatime *=2
        
        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit()
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_q:
                    sys.exit()
                elif e.key == pg.K_ESCAPE:
                    gameengine.idle_tower=None
                elif e.key == pg.K_SPACE:
                    running = not running
                elif e.key == pg.K_PLUS or e.unicode == '+' or e.key == pg.K_h:
                    doublespeed = not doublespeed

            elif e.type == pg.MOUSEBUTTONDOWN:
                if e.button == 1:
                #button.check_press(pg.mouse.get_pos())
                #gameengine.towers[-1].place_down()
                #gameengine.add_tower("turret")
                #gameengine.add_enemy("normal")
                    sidemenu.check_press(e.pos)
                    gameengine.placeIdleTower()
                if e.button == 3:
                    gameengine.idle_tower=None
            elif e.type == pg.MOUSEBUTTONUP:
                sidemenu.release()
                
        # all the updating
        gameengine.update(deltatime)

        # all the drawing
        gameengine.draw(main_surface)
        sidemenu.draw(main_surface)
        
        
#        # TEST
#        test_img = pg.image.load(enemy_path)
#        test_img = pg.transform.scale(test_img,(100,100))
#        render_img = pg.transform.rotate(test_img,pg.mouse.get_pos()[0])
#        main_surface.blit(render_img,(150,150))
#        # TEST END
        
        
        pg.display.flip() # Update the full display Surface to the screen \\ Update portions of the screen for software displays
