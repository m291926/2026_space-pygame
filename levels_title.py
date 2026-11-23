import pygame

class Title:
    def __init__(self, text, x, y, font_size=80, color=(255,255,0)):
        #make my title font
        self.font_fn = r"kenney_space-shooter-remastered\Bonus\kenvector_future.ttf"
        self.title_font = pygame.font.Font(self.font_fn, font_size)
        self.title_surface = self.title_font.render(text, True, color)
        self.title_rect = self.title_surface.get_rect(center = (x, y))
        
        self.text = text
        self.x = x
        self.y = y
        self.font_size = font_size
        self.color = color
    
    def delay(self):
        pygame.time.delay(3000)
        
    def draw(self,screen):
        screen.blit(self.title_surface, self.title_rect)