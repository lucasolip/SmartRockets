from pygame.math import Vector2
from random import random, randrange
from init import lifespan, maxForce


class DNA:

    def __init__(self, genes=None):
        if genes is not None:
            self.genes = genes
        else:
            self.genes = []
            for i in range(lifespan):
                self.genes.append(Vector2(random() - 0.5, random() - 0.5).normalize()*maxForce)

    def crossover(self, partner):
        newGenes = []
        mid = randrange(len(self.genes))
        for i in range(len(self.genes)):
            if i > mid:
                newGenes.append(self.genes[i])
            else:
                newGenes.append(partner.genes[i])
        return DNA(newGenes)

    def mutate(self, mutationRate):
        for i in range(len(self.genes)):
            if random() < mutationRate:
                self.genes[i] = Vector2(random() - 0.5, random() - 0.5).normalize()*maxForce