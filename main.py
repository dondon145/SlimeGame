import pygame
from pygame.locals import *
import slime

pygame.init()


"""def events():
    global running
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        key_list = pygame.key.get_pressed()

        # Current hit and Death trigger
        if key_list[K_h]== True:
            if event.type == pygame.KEYDOWN:
                player.isIdle = False
                player.isHit = True

        # Bouncing Movement and Dashing Movement

        if key_list[K_a]== True:
            if event.type == pygame.KEYDOWN:
                if key_list[K_SPACE]== True:
                    if event.type == pygame.KEYDOWN:
                        player.isDashing = True
                        player.isIdle = False
                        player.isBouncing = False
                        player.direction_is_y = False
                        player.direction_is_x = True
                        player.direction = -1
                    else:
                        player.isIdle = True
                        player.isBouncing = False
                        player.isDashing = False
                else:
                    player.isBouncing = True
                    player.isIdle = False
                    player.direction_is_y = False
                    player.direction_is_x = True
                    player.direction = -1

        elif key_list[K_d]== True:
            if event.type == pygame.KEYDOWN:
                if key_list[K_SPACE]== True:
                    if event.type == pygame.KEYDOWN:
                        player.isDashing = True
                        player.isIdle = False
                        player.isBouncing = False
                        player.direction_is_y = False
                        player.direction_is_x = True
                        player.direction = 1
                    else:
                        player.isIdle = True
                        player.isBouncing = False
                        player.isDashing = False
                else:
                    player.isBouncing = True
                    player.isIdle = False
                    player.direction_is_y = False
                    player.direction_is_x = True
                    player.direction = 1

        elif key_list[K_w]== True:
            if event.type == pygame.KEYDOWN:
                if key_list[K_SPACE]== True:
                    if event.type == pygame.KEYDOWN:
                        player.isDashing = True
                        player.isIdle = False
                        player.isBouncing = False
                        player.direction_is_y = True
                        player.direction_is_x = False
                        player.direction = -1
                    else:
                        player.isIdle = True
                        player.isBouncing = False
                        player.isDashing = False
                else:
                    player.isBouncing = True
                    player.isIdle = False
                    player.direction_is_y = True
                    player.direction_is_x = False
                    player.direction = -1
                    
        elif key_list[K_s]== True:
            if event.type == pygame.KEYDOWN:
                if key_list[K_SPACE]== True:
                    if event.type == pygame.KEYDOWN:
                        player.isDashing = True
                        player.isIdle = False
                        player.isBouncing = False
                        player.direction_is_y = True
                        player.direction_is_x = False
                        player.direction = 1
                    else:
                        player.isIdle = True
                        player.isBouncing = False
                        player.isDashing = False
                else:
                    player.isBouncing = True
                    player.isIdle = False
                    player.direction_is_y = True
                    player.direction_is_x = False
                    player.direction = 1
"""

count = 0

def events():
    global pressed
    global running
    global count
    

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        
        key_list = pygame.key.get_pressed()
        
        # DASH 

        if key_list[K_SPACE]== True and event.type == KEYDOWN:
            print("works")
            print(count)
            if key_list[K_a]== True and event.type == KEYDOWN:
                if count == 34:
                     player.isIdle = True
                     return
                print("also works")
                player.isBouncing = False
                player.isIdle = False
                player.isDashing = True
                player.direction_is_y = False
                player.direction_is_x = True
                player.direction = -1
                count +=1
                return count
            elif key_list[K_d]== True and event.type == KEYDOWN:
                if count == 34:
                    player.isIdle = True
                    return 
                print('also works')
                player.isBouncing = False
                player.isIdle = False
                player.isDashing = True
                player.direction_is_y = False
                player.direction_is_x = True
                player.direction = 1
                count+= 1
                return count
            elif key_list[K_w]== True and event.type == KEYDOWN:
                if count == 34:
                    player.isIdle = True
                    return
                print('also works')
                player.isBouncing = False
                player.isIdle = False
                player.isDashing = True
                player.direction_is_y = True
                player.direction_is_x = False
                player.direction = -1
                count +=1
                return count
            elif key_list[K_s]== True and event.type == KEYDOWN:
                if count == 34:
                    player.isIdle = True
                    return count
                print('also works')
                player.isBouncing = False
                player.isIdle = False
                player.isDashing = True
                player.direction_is_y = True
                player.direction_is_x = False
                player.direction = 1
                count += 1
                return count
            else :
                 print("No keys")
                 return count
            

        # BOUNCING/DASHING LEFT
        if key_list[K_a]== True:
            if event.type == KEYDOWN:
                pressed[K_a]= 'DOWN'

        # BOUNCING/DASHING RIGHT  
        if key_list[K_d]== True:
            if event.type == KEYDOWN:
                pressed[K_d]= "DOWN"

        # BOUNCING/DASHING UP
        if key_list[K_w]== True:
            if event.type == KEYDOWN:
                pressed[K_w]= 'DOWN'

        # BOUNCING/DASHING DOWN
        if key_list[K_s]== True:
            if event.type == KEYDOWN:
                pressed[K_s]= 'DOWN'
                

        # BOUNCING/DASHING LEFT WORKING
        if key_list[K_a]== True and pressed[K_a]== 'DOWN':
                player.isBouncing = True
                player.isIdle = False
                player.direction_is_y = False
                player.direction_is_x = True
                player.direction = -1

        # BOUNCING/DASHING LEFT NOT WORKING
        if key_list[K_a]== False and event.type == KEYUP:
            if pressed[K_a]== 'DOWN':
                pressed[K_a]= 'UP'

        # BOUNCINGIGHT WORKING
        if key_list[K_d]== True and pressed[K_d]== 'DOWN':
                player.isBouncing = True
                player.isIdle = False
                player.direction_is_y = False
                player.direction_is_x = True
                player.direction = 1

        # BOUNCING/DASHING RIGHT NOT WORKING
        if key_list[K_d]== False and event.type == KEYUP:
            if pressed[K_d]== 'DOWN':
                pressed[K_d]= 'UP'

        # BOUNCING UP WORKING
        if key_list[K_w]== True and pressed[K_w]== 'DOWN':
                player.isBouncing = True
                player.isIdle = False
                player.direction_is_y = True
                player.direction_is_x = False
                player.direction = -1

        # BOUNCING UP NOT WORKING
        if key_list[K_w]== False and event.type == KEYUP:
            if pressed[K_w]== 'DOWN':
                pressed[K_w]= 'UP'

        # BOUNCING DOWN WORKING
        if key_list[K_s]== True and pressed[K_s]== 'DOWN':
                player.isBouncing = True
                player.isIdle = False
                player.direction_is_y = True
                player.direction_is_x = False
                player.direction = 1

        # BOUNCING DOWN NOT WORKING
        if key_list[K_s]== False and event.type == KEYUP:
            if pressed[K_s]== 'DOWN':
                pressed[K_s]= 'UP'

        
            
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

pressed = {K_a: "UP", K_d: 'UP', K_w: "UP", K_s: "UP"}

while running:
    DISPLAYSURF.fill(BACKGROUND)
    events()
    
    
    moving_objects.update()
    moving_objects.draw(DISPLAYSURF)
    pygame.display.flip()
    clock.tick(FPS)

    