class Tile:
    def __init__(self,x,y):
        self.size = (50,50)
        self.gridPos = (x,y)
        self.pxPos = (self.size[0]*self.gridPos[0], self.size[1]*self.gridPos[1])

class Grass(Tile):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.color = (70,170,90)
        
class Path(Tile):
    def __init__(self,x,y):
        super().__init__(x,y)
        self.color = (255,200,100)