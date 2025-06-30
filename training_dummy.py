import pygame
import spritesheet

BLACK = (0,0,0)
class Training_Dummy(pygame.sprite.Sprite):

    def get_idle_frames(self, scale_size, width, height):
        global BLACK

        image = pygame.image.load("/home/big-orange/Desktop/SlimeGame/Training Dummy Sprite Sheet.png")
        idle_spritesheet = spritesheet.SpriteSheet(image)

        frame_0 = idle_spritesheet.get_frames(0, width, height, BLACK, 0)
        frame_1 = idle_spritesheet.get_frames(1, width, height, BLACK, 0)
        frame_2 = idle_spritesheet.get_frames(2, width, height, BLACK, 0)
        frame_3 = idle_spritesheet.get_frames(3, width, height, BLACK, 0)

        self.idle_animation.append(pygame.transform.scale(frame_0, (scale_size, scale_size)))
        self.idle_animation.append(pygame.transform.scale(frame_1, (scale_size, scale_size)))
        self.idle_animation.append(pygame.transform.scale(frame_2, (scale_size, scale_size)))
        self.idle_animation.append(pygame.transform.scale(frame_3, (scale_size, scale_size)))
    
    def animate_idle(self):

        if self.isIdle == True:
            self.current_animation = 0
            self.current_sprite += 0.06
            
            if self.current_sprite > len(self.idle_animation):
                self.current_sprite = 0
                return
            
            self.image = self.all_animations[self.current_animation][int(self.current_sprite)]
        
        else :
            return

    def update(self):
        self.animate_idle()



    def __init__(self, position_x, position_y):
        super().__init__()
        # 
        self.idle_animation = []
        self.hit_animation = []
        self.all_animations = [self.idle_animation, self.hit_animation]

        self.get_idle_frames(150,33, 36)
        # Booleans
        self.isHit = False
        self.isIdle = True

        # 
        self.pos_x = position_x
        self.pos_y = position_y
        self.image = pygame.Surface([150,150])
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.pos_x, self.pos_y]

        # 
        self.current_animation = 0
        self.current_sprite = 0
        self.image = self.all_animations[self.current_animation][self.current_sprite]