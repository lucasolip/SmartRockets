import pygame
from population import Population
from init import screen, clock, lifespan, count, width, height
from target import Target
from obstacle import Obstacle

target = Target(pygame.math.Vector2(width/2, 50), 10)
#obstacles = []
#obstacles = [Obstacle(pygame.math.Vector2(width/4, 200), width/2, 10)]
obstacles = [Obstacle(pygame.math.Vector2(width/4, 2*height/3), width/2, 10),
             Obstacle(pygame.math.Vector2(width/4, height/3), width/2, 10),
             Obstacle(pygame.math.Vector2(0, height/3 + height/6), width/4, 10),
             Obstacle(pygame.math.Vector2(width - width/4, height/3 + height/6), width/4, 10)]

population = Population(.01, 25, (255,255,255))

generation = 1
print("Generación", generation)

turbo = False
running = True
while running:
    if not turbo:
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            turbo = not turbo
    pygame.display.flip()
    count += 1