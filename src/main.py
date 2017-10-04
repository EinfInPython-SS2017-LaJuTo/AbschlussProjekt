#!/usr/bin/env python3

import pygame as pg
import sys
from game.Gameengine import Gameengine
# import level?
# import wave?

framerate = 60
path_data   = "../res/path_points.txt" # dann in map oder level je nachdem ...

if __name__ == "__main__":
    pg.init()
    window_size = (800,600)
    #main_surface = pg.display.set_mode(window_size, pg.FULLSCREEN)
    main_surface = pg.display.set_mode(window_size)
    clock = pg.time.Clock()
    
    gameengine = Gameengine( path_data, window_size )
    gameengine.add_tower("fire")
    gameengine.add_enemy("normal")
    
    #button = Button(200,200,100,70)
    
    while True:
        deltatime = clock.tick(framerate)
        
        for e in pg.event.get():
            if e.type == pg.QUIT:
                sys.exit()
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_q:
                    sys.exit()
            elif e.type == pg.MOUSEBUTTONDOWN:
                #button.check_press(pg.mouse.get_pos())
                gameengine.towers[-1].place_down()
                gameengine.add_tower("turret")
                
        # all the updating
        gameengine.update(deltatime)

        # all the drawing
        gameengine.draw(main_surface)
        #button.draw(main_surface)
        
        
#        # TEST
#        test_img = pg.image.load(enemy_path)
#        test_img = pg.transform.scale(test_img,(100,100))
#        render_img = pg.transform.rotate(test_img,pg.mouse.get_pos()[0])
#        main_surface.blit(render_img,(150,150))
#        # TEST END
        
        
        pg.display.flip()
