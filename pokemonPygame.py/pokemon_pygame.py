import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pokemon")
clock = pygame.time.Clock()
test_font = pygame.font.Font("pokemonPygame.py/font/Pixeltype.ttf", 50)

bulb_surf = pygame.image.load("pokemonPygame.py/graphics/bulbasaur_back.png").convert()
ground_surf = pygame.image.load("pokemonPygame.py/graphics/ground.png").convert()

score_surf = test_font.render("My game", False, "black")
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load("pokemonPygame.py/graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(bottomleft = (600,305))

player_surf = pygame.image.load("pokemonPygame.py/graphics/player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(bottomleft=(50,305))
player_hp = 5
aegis = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint((event.pos)):
                print ("boom")
        
    screen.blit(ground_surf, (0,300))
    screen.blit(sky_surf,(0,0))
    pygame.draw.rect(screen, "Pink", score_rect, 0)
    pygame.draw.rect(screen, "Pink", score_rect)
    screen.blit(score_surf,score_rect)
    snail_rect.x -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800


    screen.blit(player_surf, player_rect)
    screen.blit(snail_surf, snail_rect)

    if player_rect.colliderect(snail_rect):
        if aegis == False:
            aegis = True
            player_hp -= 1
    else:
        aegis = False

    if player_hp == 0:
        snail_rect.left = 800

    pygame.display.update()
    clock.tick(60)