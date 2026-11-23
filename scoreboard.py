import pygame

class Scoreboard:
    def __init__(self, text, x, y, font_size=20, color=(255,255,0)):
        #make title font
        self.font_fn = r"kenney_space-shooter-remastered\Bonus\kenvector_future.ttf"
        self.title_font = pygame.font.Font(self.font_fn, font_size)
        
        self.color = color
        self.x = x
        self.y = y
        self.score = 0
        self.text = text

        self.title_surface = self.title_font.render(self.text, True, self.color)
        self.title_rect = self.title_surface.get_rect(center = (self.x, self.y))

    
    def points(self, points):
        self.score += points
        
        self.title_surface = self.title_font.render(f"SCORE: {self.score}", True, self.color)
        self.title_rect = self.title_surface.get_rect(center = (self.x, self.y))
    
    def read_scoreboard(self):
        return self.score

    def draw(self, screen):
        screen.blit(self.title_surface, self.title_rect)