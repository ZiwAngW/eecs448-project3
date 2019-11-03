import pygame

sharksize =20


class Player():

    def __init__(self,master,x,y,img_path):
        self._master = master
        self. image = pygame.image.load(img_path)
        self.x = x
        self.y = y
    def move (self,x,y):
        if 0 < self.x +sharksize/2+x <= self._master.get_width():
            self.x +=x
        if 0 < self.y +sharksize/2 + y <= self._master.get_height():
            self.y +=y
    def draw(self):
        self._master.blit(self.image,(self.x,self.y))