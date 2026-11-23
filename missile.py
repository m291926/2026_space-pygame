import pygame

class Missile:
    def __init__(self, x, y):
        self.image = pygame.Surface((9,54), pygame.SRCALPHA)
        self.area = (858,230,9,54)
        self.spritesheet = pygame.image.load(r'kenney_space-shooter-remastered/Spritesheet/sheet.png')
        self.image.blit(self.spritesheet, (0,0), self.area)
        self.image = pygame.transform.rotate(self.image, 180)
        
        self.x = float(x)
        self.y = float(y)
        
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def update(self):
        self.y -= 5
        self.rect.center = (self.x,self.y)
        
    def draw(self,screen):
        screen.blit(self.image, self.rect)