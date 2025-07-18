import pygame

pygame.init()


class Crosshair(pygame.sprite.Sprite):
    

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("crosshair_white_large.png"),(30,30))
        self.rect = self.image.get_rect()
        self.rect.center = [self.rect.width/2, self.rect.height/2]

    