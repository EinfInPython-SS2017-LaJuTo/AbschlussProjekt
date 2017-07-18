#!/usr/bin/env python3

import pygame
from Tile import Grass, Path


def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surface_sz = 500   # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    map_bw = pygame.image.load("../res/map_bw.png")
    
    # Set up some data to describe a small rectangle and its color
    grid = [[None for x in range(10)] for y in range(10)]
    for x in range(10):
        for y in range(10):
            if map_bw.get_at((x,y))[0] <= 50:
                grid[x][y] = Path(x,y)
            else:
                grid[x][y] = Grass(x,y)
                
    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...
        
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill((0, 200, 255))

        # Overpaint a smaller rectangle on the main surface
        for row in grid:
            for cell in row:
                main_surface.fill(cell.color, (cell.pxPos,cell.size))
        #main_surface.fill(some_color, small_rect)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()
