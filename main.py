import pygame
from population import Population
from init import screen, clock, lifespan, count, width, height
from target import Target
from obstacle import Obstacle

target = Target(pygame.math.Vector2(width/2, 50), 10)
obstacles = [Obstacle(pygame.math.Vector2(width/4, 200), width/2, 10)]
population = Population(.03, 50, (255,255,255))

generation = 1
print("Generación", generation)

running = True
while running:
    clock.tick(60)
    screen.fill((0, 0, 0))

    if count == lifespan:
        population.evaluate(target, count)
        population.selection()
        count = 0
        generation += 1
        print("Generación", generation)
    population.run(screen, count, target, obstacles)

    target.draw()
    for obstacle in obstacles:
        obstacle.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    count += 1