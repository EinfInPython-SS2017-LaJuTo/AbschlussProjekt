#!/usr/bin/env python3

import pygame as pg
import sys
from tower.Tower import Tower
from gui.Button import Button
from map.Map import Map
from game.Gameengine import Gameengine

framerate = 60
tower_path  = "../res/tower.png"
grass_path  = "../res/grass.png"
path_path   = "../res/path_points.txt"
enemy_path  = "../res/enemy.png"

if __name__ == "__main__":
    pg.init()
    window_size = (800,600)
    main_surface = pg.display.set_mode(window_size)
    clock = pg.time.Clock()
    
    gameengine = Gameengine( Map(grass_path, path_path, main_surface.get_size()), )
    gameengine.add_tower(tower_path)
    gameengine.add_enemy(enemy_path)
    
    gametime = 0
    
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
                gameengine.add_enemy(enemy_path)
                
        # all the updating
        gameengine.update(deltatime)
        
        gametime += deltatime/1000

        if gametime > 1:
            gameengine.add_enemy(enemy_path)
            gametime = 0
        
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
