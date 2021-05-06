from init import screen
from pygame.draw import rect
from pygame import Rect

class Obstacle:
    def __init__(self, pos, w, h):
        self.x = pos.x
        self.y = pos.y
        self.w = w
        self.h = h

    def draw(self):
        rect(surface=screen, color=(150,150,150), rect=Rect(self.x, self.y, self.w, self.h))