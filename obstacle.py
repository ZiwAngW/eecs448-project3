import pygame
import random
color = (255,0,0)
radius = 5
speed =2
cd =10
class Obstacle():
    speed =2
    def __init__(self,master,x,y):
        self._master=master
        self.x =x
        self.y =y

    def update(self):
        self.y += speed

    def draw(self):
        pygame.draw.circle(self._master,color,(self.x,self.y),radius)
class ObstacleM():
    def __init__(self,master):
        self._master =master
        self.list = []
        self.time = 0
        self.num =0
    def number(self):
        self.time +=1
        if self.time% cd ==0:
            x = random.randint(0,self._master.get_width()-radius*2)
            z=Obstacle(self._master,x,0)
            self.list.append(z)
            self.num +=1
    def update(self):
        temp = []
        for obstacle in self.list:
            obstacle.update()
            temp.append(obstacle)
            self.list =temp
    def draw(self):
        for obstacle in self.list:
            obstacle.draw()