import pygame
from random import randrange
from agent import Agent

clock = pygame.time.Clock()


def main():

    pygame.init()

    pygame.display.set_caption("Programita")
    screen = pygame.display.set_mode((640, 480))
    width, height = screen.get_size()

    running = True

    lifespan = 200
    count = 0
    agents = []
    for _ in range(10):
        agents.append(Agent(pygame.math.Vector2(width/2, height), lifespan))

    while running:
        clock.tick(60)

        screen.fill((0, 0, 0))

        if count == lifespan:
            # Evolve
            count = 0

        for agent in agents:
            agent.update(count)
            agent.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        count += 1


if __name__ == "__main__":
    main()
