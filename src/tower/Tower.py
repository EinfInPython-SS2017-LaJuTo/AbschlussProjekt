from pygame import Rect

class Tower:
    def __init__(self,x,y):
        self.box = Rect(x, y, 10, 10)
        
    def isOnPath(self,path):
        if self.box.collidelist(path) != -1:
            True
        else:
            return False
