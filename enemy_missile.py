import pygame

class Enemymissile:
    def __init__(self, x, y):
        self.image = pygame.Surface((13,54), pygame.SRCALPHA)
        #laserBlue16.png x="843" y="62" width="13" height="54"
        self.area = (843,62,13,54)
        self.spritesheet = pygame.image.load(r'kenney_space-shooter-remastered/Spritesheet/sheet.png')
        self.image.blit(self.spritesheet, (0,0), self.area)
        self.image = pygame.transform.rotozoom(self.image, 180, 1/2)
        
        self.speed = 3
        self.x = float(x)
        self.y = float(y)
        
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def update(self):
        self.y += self.speed
        self.rect.center = (self.x,self.y)
        
    def draw(self,screen):
        screen.blit(self.image, self.rect)