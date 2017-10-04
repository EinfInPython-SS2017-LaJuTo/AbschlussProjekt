from map.Path    import Path
import pygame as pg

class Map(pg.Rect):
    # attributes:
        # size
        # towers
        # enemies
        # path
        # bullets
        
    def __init__(self,image_map, path_data, size):
        super().__init__(0,0,*size)
        self.tilesize = 50
        self.path = Path(path_data, 40, (200,200,100))
        self.bg_image = image_map
        self.bg_image = pg.transform.scale(self.bg_image, (self.tilesize,)*2)
    
    def draw(self, surface):
        # background_image
        for x in range(int(self.size[0]/self.tilesize)+1):
            for y in range(int(self.size[1]/self.tilesize)+1):
                surface.blit(self.bg_image, (x*self.tilesize,y*self.tilesize))
        # path
        self.path.draw(surface)        
