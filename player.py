import pygame

TS = 50
HEIGHT = 14*TS
WIDTH = 15*TS
SIZE = (WIDTH,HEIGHT)


class Player:
    def __init__(self, x, y):
        self.image = pygame.Surface((99,75), pygame.SRCALPHA)
        #"playerShip1_blue.png" x="211" y="941" width="99" height="75"
        self.area = (211,941,99,75)
        self.spritesheet = pygame.image.load(r'kenney_space-shooter-remastered\Spritesheet\sheet.png')
        self.image.blit(self.spritesheet, (0,0), self.area)
        self.x = x
        self.y = y
        self.new_image = pygame.transform.rotozoom(self.image, 0, 1/2)
        self.rect = self.new_image.get_rect(center = (self.x, self.y))
        
    def move_ship(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.x -= 3
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.y -= 3
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.y += 3
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.x += 3
            
                    
    def get_tip(self):
        x_offset = self.x
        y_offset = self.y - 35
        return (x_offset, y_offset)

    def update(self):
        #update x,y,and rect
        self.rect.center = (self.x,self.y)
        if self.x >= 15*TS-35:
            self.x = 15*TS-35
        if self.y >= 14*TS-35:
            self.y = 14*TS-35
        if self.x <= 35:
            self.x = 35
        if self.y <= 9*TS:
            self.y = 9*TS
    
    def draw(self,screen):
        screen.blit(self.new_image, self.rect)
        

