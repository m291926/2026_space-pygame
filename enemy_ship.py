import pygame

TS = 50

class Enemy:
    def __init__(self, x, y):
        self.image = pygame.Surface((93,84), pygame.SRCALPHA)
        self.area = (423,728,93,84)
        self.spritesheet = pygame.image.load(r'kenney_space-shooter-remastered\Spritesheet\sheet.png')
        self.image.blit(self.spritesheet, (0,0), self.area)
        self.x = x
        self.y = y
        self.new_image = pygame.transform.rotozoom(self.image, 0, 1/2)
        self.rect = self.new_image.get_rect(center = (self.x, self.y))
       
    def get_tip(self):
        x_offset = self.x
        y_offset = self.y + 35
        return (x_offset, y_offset)

    def update(self):
        #update x,y,and rect
        self.rect.center = (self.x,self.y)
        if self.y < 6*TS:
            self.y += 1
            if self.y > 6*TS:
                self.y = 6*TS       
    
    def draw(self,screen):
        screen.blit(self.new_image, self.rect)
        

