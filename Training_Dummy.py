import pygame

class Training_Dummy(pygame.sprite.Sprite):
    
    def __init__(self):
        super().__init__()
        self.isHit = False
        self.image = pygame.