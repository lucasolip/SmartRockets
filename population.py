from agent import Agent
from random import randrange
from serializer import serialize

class Population:
    def __init__(self, mutationRate, size, color):
        self.agents = []
        self.size = size
        self.matingPool = []
        self.mutationRate = mutationRate
        self.color = color

        self.historicalMax = 0

        for i in range(self.size):
            self.agents.append(Agent())

    def evaluate(self, target, count):
        maxFit = 0
        best = None
        for agent in self.agents:
            if not agent.completed:
                agent.calcFitness(target, count)
            if agent.fitness > maxFit:
                maxFit = agent.fitness
                best = agent
        for agent in self.agents:
            agent.fitness /= maxFit

        self.matingPool = []

        for agent in self.agents:
            n = agent.fitness * 100
            for i in range(int(n)):
                self.matingPool.append(agent)
        print("Puntuación del mejor agente:", maxFit)
        if maxFit > self.historicalMax:
            self.historicalMax = maxFit

    def selection(self):
        newAgents = []
        for _ in range(len(self.agents)):
            while True:
                parentA = self.matingPool[randrange(len(self.matingPool))].dna
                parentB = self.matingPool[randrange(len(self.matingPool))].dna
                if parentA != parentB:
                    break
            child = parentA.crossover(parentB)
            child.mutate(self.mutationRate)
            newAgents.append(Agent(dna=child))
        self.agents = newAgents

    def run(self, screen, count, target, obstacles):
        for agent in self.agents:
            agent.update(count, target, obstacles)
            agent.draw(screen, self.color)