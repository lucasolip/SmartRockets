from pygame.math import Vector2
from math import atan2, sqrt
from dna import DNA
from triangle import drawTriangle
from init import width, height, lifespan


class Agent:

    def __init__(self, dna=None):
        self.pos = Vector2(width/2, height - 5)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.completed = False
        self.crashed = False
        if dna is not None:
            self.dna = dna
        else:
            self.dna = DNA()
        self.fitness = 0

    def calcFitness(self, target, count):
        # Euclidean distance
        distance = sqrt((target.x - self.pos.x)**2 + (target.y - self.pos.y)**2)
        # Manhattan distance
        # distance = abs((target.x - self.pos.x)) + abs((target.y - self.pos.y))

        self.fitness = width + -width * distance/width

        if self.completed:
            self.fitness *= lifespan*10/count
        elif self.crashed:
            self.fitness /= 10

    def update(self, count, target, obstacles):
        if self.collidingTarget(target) and not self.completed:
            self.completed = True
            self.pos = Vector2(target.x, target.y)
            self.calcFitness(target, count)
        for obstacle in obstacles:
            if self.collidingRect(obstacle):
                self.crashed = True
                break
        if not (0 < self.pos.x < width) or not (0 < self.pos.y < height):
            self.crashed = True

        if (not self.completed) and (not self.crashed):
            self.applyForce(self.dna.genes[count])
            self.vel.xy += self.acc.xy
            self.pos.xy += self.vel.xy
            self.acc.xy = 0, 0
            if self.vel.magnitude() > 4:
                self.vel = self.vel.normalize() * 4

    def collidingTarget(self, target):
        return sqrt((target.x - self.pos.x)**2 + (target.y - self.pos.y)**2) < target.radius

    def collidingRect(self, rect):
        return rect.x < self.pos.x < rect.x + rect.w and rect.y < self.pos.y < rect.y + rect.h

    def applyForce(self, force):
        self.acc.xy += force.xy

    def draw(self, screen, color):
        ang = atan2(self.vel.y, self.vel.x)
        drawTriangle(screen, self.pos.x, self.pos.y, ang, 10, color)
