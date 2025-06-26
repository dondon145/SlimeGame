import pygame
from pygame.locals import *
import slime

pygame.init()


def events():
    global running
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        key_list = pygame.key.get_pressed()

        if key_list[K_a]== True:
            if event.type == pygame.KEYDOWN:
                player.isBouncing = True
                player.isIdle = False
                player.direction_is_y = False
                player.direction_is_x = True
                player.direction = -1
        elif key_list[K_d]== True:
            if event.type == pygame.KEYDOWN:
                player.isBouncing = True
                player.isIdle = False
                player.direction_is_y = False
                player.direction_is_x = True
                player.direction = 1
        elif key_list[K_w]== True:
            if event.type == pygame.KEYDOWN:
                player.isBouncing = True
                player.isIdle = False
                player.direction_is_y = True
                player.direction_is_x = False
                player.direction = -1
        elif key_list[K_s]== True:
            if event.type == pygame.KEYDOWN:
                player.isBouncing = True
                player.isIdle = False
                player.direction_is_y = True
                player.direction_is_x = False
                player.direction = 1


WIDTH = 800
HEIGHT = 800
BACKGROUND = (80,160,80)
clock = pygame.time.Clock()
FPS = 60

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slime Game")
running = True


slime_pos_x = 350
slime_pos_y = 350

player = slime.Slime(slime_pos_x, slime_pos_y)
moving_objects = pygame.sprite.Group()
moving_objects.add(player)

while running:
    DISPLAYSURF.fill(BACKGROUND)
    events()
    
    
    moving_objects.update()
    moving_objects.draw(DISPLAYSURF)
    pygame.display.flip()
    clock.tick(FPS)

    