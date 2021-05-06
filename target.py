from init import screen
from pygame.draw import ellipse
from pygame import Rect

class Target:
    def __init__(self, pos, radius):
        self.radius = radius
        self.x = pos.x
        self.y = pos.y

    def draw(self):
        ellipse(surface=screen, color=(0, 136, 255), rect=Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2))