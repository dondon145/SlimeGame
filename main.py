import pygame
from pygame.locals import *
import slime
import training_dummy
import crosshair

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

        if key_list[K_SPACE]:
            print("works")

            if key_list[K_a]== True and event.type == KEYDOWN:
                print('also works')
                pressed[K_SPACE]= "DOWN"
                player.isBouncing = False
                if player.isBouncing == False:
                    print("bouncing")
                player.isIdle = False
                if player.isIdle == False :
                    print('idle')
                player.isDashing = True
                player.direction_is_y = False
                player.direction_is_x = True
                player.direction = -1

            elif key_list[K_w]== True and event.type == KEYDOWN:
                print('also works')
                pressed[K_SPACE]= "DOWN"
                player.isBouncing = False
                if player.isBouncing == False:
                    print("bouncing")
                player.isIdle = False
                if player.isIdle == False :
                    print('idle')
                player.isDashing = True
                player.direction_is_y = True
                player.direction_is_x = False
                player.direction = -1
            elif key_list[K_s]== True and event.type == KEYDOWN:
                print('also works')
                pressed[K_SPACE]= "DOWN"
                player.isBouncing = False
                if player.isBouncing == False:
                    print("bouncing")
                player.isIdle = False
                if player.isIdle == False :
                    print('idle')
                player.isDashing = True
                player.direction_is_y = True
                player.direction_is_x = False
                player.direction = 1

            elif key_list[K_d]== True and event.type == KEYDOWN:
                print('also works')
                pressed[K_SPACE]= "DOWN"
                player.isBouncing = False
                if player.isBouncing == False:
                    print("bouncing")
                player.isIdle = False
                if player.isIdle == False :
                    print('idle')
                player.isDashing = True
                player.direction_is_y = False
                player.direction_is_x = True
                player.direction = 1
        if event.type == KEYUP:
            pressed[K_SPACE]= "UP"
            player.isDashing = False
            pressed[K_d]= "UP"
            pressed[K_a]= "UP"
            player.isBouncing = False
            player.isIdle = True
            

        # BOUNCING/DASHING LEFT
        if key_list[K_a]== True:
            if event.type == KEYDOWN:
                pressed[K_a]= 'DOWN'

        # BOUNCING/DASHING RIGHT  
        if key_list[K_d]== True:
            if event.type == KEYDOWN:
                if pressed[K_SPACE]== "UP":
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

        # (prototype) hit training dummy 
        if key_list[K_h]== True:
            if event.type == pygame.KEYDOWN:
                training_dum_dum.isIdle = False
                training_dum_dum.isHit = True


        # get mouse button states
        mouse_list = pygame.mouse.get_pressed(num_buttons= 3)
        # hit training dummy with mouse
        if event.type == MOUSEBUTTONDOWN:
            if mouse_list[0]== True:
                colliding = pygame.sprite.collide_rect(slime_crosshair, training_dum_dum)
                if colliding == True:
                    print("MOUSE")
                    training_dum_dum.isIdle = False
                    training_dum_dum.isHit = True

        
            
WIDTH = 800
HEIGHT = 800
BACKGROUND = (80,160,80)
clock = pygame.time.Clock()
FPS = 60

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slime Game")
running = True


slime_pos_x = 250
slime_pos_y = 350

player = slime.Slime(slime_pos_x, slime_pos_y, 37, 37)
moving_objects = pygame.sprite.Group()
moving_objects.add(player)

training_dum_dum = training_dummy.Training_Dummy(500,200)
slime_crosshair = crosshair.Crosshair()
moving_objects.add(training_dum_dum)
moving_objects.add(slime_crosshair)

pressed = {K_a: "UP", K_d: 'UP', K_w: "UP", K_s: "UP", K_SPACE: "UP"}

pygame.mouse.set_visible(False)

while running:
    DISPLAYSURF.fill(BACKGROUND)
    events()
    
    
    moving_objects.update()
    moving_objects.draw(DISPLAYSURF)
    pygame.display.flip()
    print(player.current_sprite)
    clock.tick(FPS)

    