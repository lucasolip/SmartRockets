from pygame.draw import polygon
from pygame import Color
from math import sin, cos, pi


def drawTriangle(surface, x, y, angle, radius, color):
    pointA = (cos(angle)*radius+x, sin(angle)*radius+y)
    separation = 0.7
    angle += pi
    pointB = (cos(angle+separation)*radius+x, sin(angle+separation)*radius+y)
    pointC = (cos(angle-separation)*radius+x, sin(angle-separation)*radius+y)
    polygon(surface=surface, points=(pointA, pointB, pointC), color=color)
