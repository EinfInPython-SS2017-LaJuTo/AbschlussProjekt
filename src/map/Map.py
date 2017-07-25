from map.Path    import Path
import pygame as pg

class Map():
    # attributes:
        # size
        # towers
        # enemies
        # path
        # bullets
        
    def __init__(self,image_path, path_path, size):
        self.size = size
        self.tilesize = 50
        self.path = Path(path_path)
        self.bg_image = image_path
        self.bg_image = pg.transform.scale(self.bg_image, (self.tilesize,)*2)
    
    def draw(self, surface):
        # background_image
        for x in range(int(self.size[0]/self.tilesize)):
            for y in range(int(self.size[1]/self.tilesize)):
                surface.blit(self.bg_image, (x*self.tilesize,y*self.tilesize))
        # path
        self.path.draw(surface)        