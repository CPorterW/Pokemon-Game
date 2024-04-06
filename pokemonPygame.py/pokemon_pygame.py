import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pokemon")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        



    pygame.display.update()
    clock.tick(60)