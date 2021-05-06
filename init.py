import pygame

clock = pygame.time.Clock()

pygame.init()

pygame.display.set_caption("Programita")
screen = pygame.display.set_mode((640, 480))

width, height = screen.get_size()
maxForce = 1
lifespan = 400
count = 0
