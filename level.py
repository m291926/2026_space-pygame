class Level():
    def __init__(self, name, max_enemy_ships, enemy_ship_total, max_meteors, meteor_total, meteor_speed, goal):
        self.name = name
        self.max_enemy_ships = max_enemy_ships
        self.enemy_ship_total = enemy_ship_total
        self.max_meteors = max_meteors
        self.meteor_total = meteor_total
        self.meteor_speed = meteor_speed
        self.goal = goal
    
    def score(self, x, y, font_size=20, color=(255,255,0)):
        #make title font
        self.font_fn = r"kenney_space-shooter-remastered\Bonus\kenvector_future.ttf"
        self.title_font = pygame.font.Font(self.font_fn, font_size)
    
        self.color = color
        self.x = x
        self.y = y

        self.title_surface = self.title_font.render(f"SCORE: {self.score}", True, self.color)
        self.title_rect = self.title_surface.get_rect(center = (self.x, self.y))