import pygame



class Meteor:
    def __init__(self, x, y):
        self.image = pygame.Surface((43,43), pygame.SRCALPHA)
        #"meteorGrey_med1.png" x="674" y="219" width="43" height="43"
        self.area = (674,219,43,43)
        self.spritesheet = pygame.image.load(r'kenney_space-shooter-remastered\Spritesheet\sheet.png')
        self.image.blit(self.spritesheet, (0,0), self.area)
        
        self.x = x
        self.y = 0
        
    def update(self,speed):
        self.speed = speed
        self.y += self.speed
        
    def draw(self, screen):
        self.rect = self.image.get_rect(center = (self.x, self.y))
        screen.blit(self.image, self.rect)