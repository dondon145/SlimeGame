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
        global BLACK

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


    def dash_get_frames(self):
        global BLACK

        # There is no initial spritesheet for dash, but few frames from bouncing will make up a solid dashing animation
        image = pygame.image.load('/home/big-orange/Desktop/SlimeGame/Assets/BouncingSpritesheet.png')
        dash_spritesheet = spritesheet.SpriteSheet(image)

        frame_0 = dash_spritesheet.get_frames(1, 16, 16, BLACK, 0)
        frame_1 = dash_spritesheet.get_frames(2, 16, 16, BLACK, 0)
        frame_2 = dash_spritesheet.get_frames(2, 16, 16, BLACK, 0)
        frame_3 = dash_spritesheet.get_frames(1, 16, 16, BLACK, 0)
        frame_4 = dash_spritesheet.get_frames(0, 16, 16, BLACK, 0)

        self.dash_sprites.append(pygame.transform.scale(frame_0,(50,50)))
        self.dash_sprites.append(pygame.transform.scale(frame_1,(50,50)))
        self.dash_sprites.append(pygame.transform.scale(frame_2,(50,50)))
        self.dash_sprites.append(pygame.transform.scale(frame_3,(50,50)))
        self.dash_sprites.append(pygame.transform.scale(frame_4,(50,50)))

    def death_get_frames(self):
        global BLACK

        image = pygame.image.load('/home/big-orange/Desktop/SlimeGame/Assets/DeathSpritesheet.png')
        death_spritesheet = spritesheet.SpriteSheet(image)

        frame_0 = death_spritesheet.get_frames(0, 20, 20, BLACK, 0)
        frame_1 = death_spritesheet.get_frames(1, 20, 20, BLACK, 0)
        frame_2 = death_spritesheet.get_frames(2, 20, 20, BLACK, 0)
        frame_3 = death_spritesheet.get_frames(0, 20, 20, BLACK, 1)
        frame_4 = death_spritesheet.get_frames(1, 20, 20, BLACK, 1)
        frame_5 = death_spritesheet.get_frames(2, 20, 20, BLACK, 1)
        frame_6 = death_spritesheet.get_frames(0, 20, 20, BLACK, 2)
        frame_7 = death_spritesheet.get_frames(1, 20, 20, BLACK, 2)

        self.death_sprites.append(pygame.transform.scale(frame_0,(50,50)))
        self.death_sprites.append(pygame.transform.scale(frame_1,(50,50)))
        self.death_sprites.append(pygame.transform.scale(frame_2,(50,50)))
        self.death_sprites.append(pygame.transform.scale(frame_3,(50,50)))
        self.death_sprites.append(pygame.transform.scale(frame_4,(50,50)))
        self.death_sprites.append(pygame.transform.scale(frame_5,(50,50)))
        self.death_sprites.append(pygame.transform.scale(frame_6,(50,50)))
        self.death_sprites.append(pygame.transform.scale(frame_7,(50,50)))

    def hit_get_frames(self):
        global BLACK

        # separating spritesheet into multiple frames
        # makes it possible to stich it all together later into an animation
        image = pygame.image.load('/home/big-orange/Desktop/SlimeGame/Assets/HitSpritesheet.png')
        hit_spritesheet = spritesheet.SpriteSheet(image)
        frame_0 = hit_spritesheet.get_frames(0, 16, 16, BLACK, 0)
        frame_1 = hit_spritesheet.get_frames(1, 16, 16, BLACK, 0)
        frame_2 = hit_spritesheet.get_frames(0, 16, 16, BLACK, 1)
        frame_3 = hit_spritesheet.get_frames(1, 16, 16, BLACK, 1)

        # the sprites are too small, so rescaling them is better for visual and comfort 
        self.hit_sprites.append(pygame.transform.scale(frame_0,(50,50)))
        self.hit_sprites.append(pygame.transform.scale(frame_1,(50,50)))
        self.hit_sprites.append(pygame.transform.scale(frame_2,(50,50)))
        self.hit_sprites.append(pygame.transform.scale(frame_3,(50,50)))


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

            if self.current_animation != 1:
                self.current_sprite = 0

            self.current_animation = 1
            self.current_sprite += 0.12
            self.change_pos(0.50,self.direction)

            if self.current_sprite > len(self.bouncing_sprites):
                    
                    self.current_sprite = 0
                    self.isIdle = True
                    self.isBouncing = False

            self.image = self.animations[self.current_animation][int(self.current_sprite)]
        else :
            return

    def animate_dash(self):
        # 5 sprites from bouncing would make up a great dash

        if self.isDashing == True:

            if self.current_animation != 2:
                self.current_sprite = 0

            self.current_animation = 2
            self.current_sprite += 0.12
            self.change_pos(2,self.direction)

            if self.current_sprite > len(self.dash_sprites):
                    
                    self.current_sprite = 0
                    self.isIdle = True
                    self.isDashing = False

            self.image = self.animations[self.current_animation][int(self.current_sprite)]
        else :
            return

    def animate_death(self):

        if self.isDead == True:

            if self.current_animation != 3:
                self.current_sprite = 0
            if self.current_sprite > (len(self.death_sprites))-1:
                    
                self.isDead = False
                self.isBouncing = False
                self.isDashing = False
                self.isIdle = False
                self.current_sprite = -1
                self.image = self.animations[self.current_animation][int(self.current_sprite)]
                return
            elif self.current_sprite <=(len(self.death_sprites))-1:
                self.isIdle = False
                self.current_animation = 3
                self.current_sprite += 0.12

                self.image = self.animations[self.current_animation][int(self.current_sprite)]
        else :
            return

    def animate_hit(self):

        if self.isHit == True:
            if self.current_animation != 4:
                self.current_animation = 4
                self.current_sprite = 0
                self.health -= 10

            if self.health <= 0:
                self.isHit = False
                self.isIdle = False
                self.isBouncing = False
                self.isDashing = False
                self.isDead = True
                return
            if self.current_sprite >= len(self.hit_sprites)-1:
                self.current_sprite = 0
                self.isIdle = True
                self.isHit = False
                return
            
            else:
                self.current_sprite += 0.12
                self.image = self.animations[self.current_animation][int(self.current_sprite)]
        else:
                return




    def update(self):

        self.animate_idle()
        self.animate_bouncing()
        self.animate_dash()
        self.animate_death()
        self.animate_hit()


    


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
        self.isDashing = False

        # all sprites for each action
        self.idle_sprites = []
        self.bouncing_sprites = []
        self.dash_sprites = []
        self.hit_sprites = []
        self.death_sprites = []

        # getting all sprites for each action 
        self.idle_get_frames()
        self.bouncing_get_frames()
        self.dash_get_frames()
        self.death_get_frames()
        self.hit_get_frames()

        # making it easier to switch between actions during game 
        self.animations = [self.idle_sprites, self.bouncing_sprites, self.dash_sprites, self.death_sprites, self.hit_sprites,]
        self.current_animation = 0
        self.current_sprite = 0

        # position values
        self.pos_x = position_x
        self.pos_y = position_y
        self.direction = 1
        self.direction_is_y = False
        self.direction_is_x = False

        # Characters Stats
        self.health = 100
        self.stamina = 100
        self.mana = 100


        # this stores all the visual that is being put on the display
        self.image = pygame.Surface((100,100))
        self.image = self.animations[self.current_animation][self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]

    
