import pygame
from pygame.locals import *
import spritesheet


pygame.init()
BLACK = (0,0,0,0)
RED = (255,0,0)
BACKGROUND = (80,160,80)

class Slime(pygame.sprite.Sprite):
    
    
    def idle_get_frames(self):
        global BLACK
        global RED
        global BACKGROUND

        # separating spritesheet into multiple frames
        # makes it possible to stich it all together later into an animation
        image = pygame.image.load('/home/big-orange/Desktop/SlimeGame/Assets/IdleSpritesheet.png')
        idle_spritesheet = spritesheet.SpriteSheet(image)
        frame_0 = idle_spritesheet.get_frames(0, 16, 16, BLACK, 0)
        frame_1 = idle_spritesheet.get_frames(1, 16, 16, BLACK, 0)
        frame_2 = idle_spritesheet.get_frames(0, 16, 16, BLACK, 1)
        frame_3 = idle_spritesheet.get_frames(1, 16, 16, BLACK, 1)
        frame_4 = idle_spritesheet.get_frames(0, 16, 16, BLACK, 2)
        frame_5 = idle_spritesheet.get_frames(1, 16, 16, BLACK, 2)

        # the sprites are too small, so rescaling them is better for visual and comfort 
        self.idle_sprites.append(pygame.transform.scale(frame_0,(50,50)))
        self.idle_sprites.append(pygame.transform.scale(frame_1,(50,50)))
        self.idle_sprites.append(pygame.transform.scale(frame_2,(50,50)))
        self.idle_sprites.append(pygame.transform.scale(frame_3,(50,50)))
        self.idle_sprites.append(pygame.transform.scale(frame_4,(50,50)))
        self.idle_sprites.append(pygame.transform.scale(frame_5,(50,50)))


    def bouncing_get_frames(self):
        
        image = pygame.image.load('/home/big-orange/Desktop/SlimeGame/Assets/BouncingSpritesheet.png')
        bouncing_spritesheet = spritesheet.SpriteSheet(image)

        # separating spritesheet into multiple frames
        # makes it possible to stich it all together later into an animation
        frame_0 = bouncing_spritesheet.get_frames(0, 16, 16, BLACK, 0)
        frame_1 = bouncing_spritesheet.get_frames(1, 16, 16, BLACK, 0)
        frame_2 = bouncing_spritesheet.get_frames(2, 16, 16, BLACK, 0)
        frame_3 = bouncing_spritesheet.get_frames(0, 16, 16, BLACK, 1)
        frame_4 = bouncing_spritesheet.get_frames(1, 16, 16, BLACK, 1)
        frame_5 = bouncing_spritesheet.get_frames(2, 16, 16, BLACK, 1)
        frame_6 = bouncing_spritesheet.get_frames(0, 16, 16, BLACK, 2)

        # the sprites are too small, so rescaling them is better for visual and comfort 
        self.bouncing_sprites.append(pygame.transform.scale(frame_0,(50,50)))
        self.bouncing_sprites.append(pygame.transform.scale(frame_1,(50,50)))
        self.bouncing_sprites.append(pygame.transform.scale(frame_2,(50,50)))
        self.bouncing_sprites.append(pygame.transform.scale(frame_3,(50,50)))
        self.bouncing_sprites.append(pygame.transform.scale(frame_4,(50,50)))
        self.bouncing_sprites.append(pygame.transform.scale(frame_5,(50,50)))
        self.bouncing_sprites.append(pygame.transform.scale(frame_6,(50,50)))









    def animate_idle(self):

        if self.isIdle == True:
            self.current_animation = 0
            self.current_sprite += 0.12

            if self.current_sprite > len(self.idle_sprites):
                self.current_sprite = 0

            self.image = self.animations[self.current_animation][int(self.current_sprite)]
        else :
            return



    def animate_bouncing(self):

        if self.isBouncing == True:
            self.current_animation = 1
            self.current_sprite += 0.12

            if self.current_sprite > len(self.bouncing_sprites):
                    self.change_pos(15,self.direction)
                    self.current_sprite = 0
                    self.isIdle = True
                    self.isBouncing = False

            self.image = self.animations[self.current_animation][int(self.current_sprite)]
        else :
            return

    def animate_dash(self):
        # 4 sprites froum bouncing would make up a great dash
        pass


    def animate_hit(self):
        pass

    def animate_death(self):
        pass




    def update(self):
        self.animate_idle()
        self.animate_bouncing()

        



    


    def set_pos_x(self, val):
        self.pos_x = val
    
    def set_pos_y(self, val):
        self.pos_y = val

    def get_pos_x(self):
        return self.pos_x
    
    def get_pos_y(self):
        return self.pos_y
    
    def add_to_pos_x(self, val, direction):
        val *= direction
        self.pos_x += val
        self.rect.topleft = [self.pos_x, self.pos_y]
    
    def add_to_pos_y(self, val, direction):
        val*= direction
        self.pos_y += val
        self.rect.topleft = [self.pos_x, self.pos_y]

    def change_pos(self, val, direction):
        if self.direction_is_y == True:
            self.add_to_pos_y(val,direction)
        if self.direction_is_x == True:
            self.add_to_pos_x(val, direction)



    def __init__(self, position_x, position_y):
        
        # initialising the super class, (pygame.sprite.Sprite)
        super().__init__()

        # actions booleans
        self.isIdle = True
        self.isBouncing = False
        self.isHit = False
        self.isDead = False

        # all sprites for each action
        self.idle_sprites = []
        self.bouncing_sprites = []
        self.hit_sprites = []
        self.death_sprites = []

        # getting all sprites for each action 
        self.idle_get_frames()
        self.bouncing_get_frames()

        # making it easier to switch between actions during game 
        self.animations = [self.idle_sprites, self.bouncing_sprites, self.hit_sprites, self.death_sprites]
        self.current_animation = 0
        self.current_sprite = 0

        # position values
        self.pos_x = position_x
        self.pos_y = position_y
        self.direction = 1
        self.direction_is_y = False
        self.direction_is_x = False


        # this stores all the visual that is being put on the display
        self.image = pygame.Surface((100,100))
        self.image = self.animations[self.current_animation][self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]

    
