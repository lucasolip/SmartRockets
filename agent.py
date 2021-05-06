from pygame import Vector2
from math import atan2
from random import random
from triangle import drawTriangle


class Agent:

    def __init__(self, pos, nGenes):
        self.pos = pos
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.genes = []
        for i in range(nGenes):
            self.genes.append(Vector2(random()-0.5, random()-0.5).normalize())

    def update(self, count):
        self.applyForce(self.genes[count])
        self.vel.xy += self.acc.xy
        self.pos.xy += self.vel.xy
        self.acc.xy = 0, 0
        if self.vel.magnitude() > 4:
            self.vel = self.vel.normalize() * 4

    def applyForce(self, force):
        self.acc.xy += force.xy

    def draw(self, screen):
        ang = atan2(self.vel.y, self.vel.x)
        drawTriangle(screen, self.pos.x, self.pos.y, ang, 10)
