import pygame


class Background():
    def __init__(self):
        g_fp = r"   "
        
        
        
        
        
        
        g = pygame.image.load(g_fp)
        
        
        
        self.tile_matrix = [
            [g,.....],
            [],
            [],
            [],
            [],
            [],
            [],
            ]
        
        self.size = size
        self.ts = ts
        
    def make_bg(self):
        self.bg = pygame.Surface(self.size)
        for r in range(len(self.tile_matrix)):
            for c in range(len(self.tile_matrix[r])):
                self.bg.blit(self.tile_matrix[r][c], (c*self.ts, r*self.ts))
                
        return self.bg      
    
#bg_builder = Background(SIZE,TS)
#bg = bg_builder.make_bg()