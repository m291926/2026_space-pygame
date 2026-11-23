import pygame
import random
from player import Player
from missile import Missile
from meteor import Meteor
from enemy_ship import Enemy
from enemy_missile import Enemymissile
from scoreboard import Scoreboard
from level import Level
from levels_title import Title


TS = 50
WIDTH = 15*TS
HEIGHT = 14*TS
SIZE = (WIDTH,HEIGHT)

pygame.init()

screen = pygame.display.set_mode(SIZE)

scoreboard = Scoreboard("SCORE: 0", 13*TS, 20)

levels = [
    Level("LEVEL 1", 5, 20, 5, 20, 1, 200),
    Level("LEVEL 2", 6, 24, 5, 20, 1, 440),
    Level("LEVEL 3", 7, 28, 5, 20, 2, 720),
    Level("LEVEL 4", 8, 32, 5, 20, 2, 1040),
    Level("LEVEL 5", 9, 36, 5, 20, 3, 1400),
    Level("LEVEL 6", 10, 50, 6, 30, 3, 1900),
    Level("LEVEL 7", 10, 60, 7, 42, 4, 2500),
    Level("LEVEL 8", 10, 70, 8, 56, 4, 3200),
    Level("LEVEL 9", 10, 80, 9, 72, 5, 4000),
    Level("LEVEL 10", 10, 90, 10, 90, 5, 4900),
    ]

level = 0
new_level = levels[level]

introtitle = Title("Press space to begin", 375, 6*TS, font_size=20)
title = Title("NEW LEVEL", 375, 6*TS)
title1 = Title("You won!!", 375,6*TS)
endtitle = Title("You died. . . \nEnter your name below to save your score:", 375, 6*TS, font_size=20)
highscoretitle = Title("NEW HIGH SCORE!!! \nEnter your name below to save your score!", 375, 6*TS, font_size=20)

image = pygame.image.load(r"kenney_space-shooter-remastered\Backgrounds\purple.png")
bg = pygame.transform.scale(image, (2*TS,2*TS))

player = Player(375,10*TS)

clock = pygame.time.Clock()

missiles = []
meteors = []
enemy_ships = []
enemy_missiles = []

meteors_in_round = 0
enemy_ships_in_round = 0

running = 1
while running:
    for x in range(0,15*TS,TS):
        for y in range(0,14*TS,TS):
            screen.blit(bg,(x,y))
    introtitle.draw(screen)
    pygame.display.flip()
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                running = 0
        if e.type == pygame.QUIT:
            pygame.quit()

running = 1
while running:
    for x in range(0,15*TS,TS):
        for y in range(0,14*TS,TS):
            screen.blit(bg,(x,y))
    player.draw(screen)
    player.update()
    events = pygame.event.get()
    player.move_ship()
    meteors = [m for m in meteors if m.y < 14*TS+50]
    missiles = [m for m in missiles if m.y > -50]
    enemy_missiles = [e for e in enemy_missiles if e.y < 14*TS+50]
    for e in events:
        if e.type == pygame.QUIT:
            running = 0
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                missiles.append(Missile(*player.get_tip()))
    for m in missiles:
        m.update()
        m.draw(screen)
    if random.randint(0,100) == 1 and len(meteors) < new_level.max_meteors and meteors_in_round < new_level.meteor_total:
        meteors.append(Meteor(random.randint(20,15*TS-43),0))
        meteors_in_round += 1
    if random.randint(0,100) == 1 and len(enemy_ships) < new_level.max_enemy_ships and enemy_ships_in_round < new_level.enemy_ship_total:
        enemy_ships.append(Enemy(random.randint(20,15*TS-84),0))
        enemy_ships_in_round += 1
    for m in meteors:
        m.update(new_level.meteor_speed)
        m.draw(screen)
    for e in enemy_ships:
        e.update()
        e.draw(screen)
    for e in enemy_ships:
        if random.randint(0,60) == 1:
            enemy_missiles.append(Enemymissile(*e.get_tip()))
    for e in enemy_missiles:
        e.update()
        e.draw(screen)
    for m in missiles[:]:
        for enemy in enemy_ships[:]:
            if m.rect.colliderect(enemy.rect):
                enemy_ships.remove(enemy)
                missiles.remove(m)
                scoreboard.points(20)
                break
    for enemy in enemy_missiles:
        if enemy.rect.colliderect(player):
            running = 0
    for m in meteors[:]:
        if m.rect.colliderect(player):
            running = 0
        
    scoreboard.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    pygame.display.set_caption("Space game")
    
    if new_level.goal < 4900 and scoreboard.read_scoreboard() >= new_level.goal:
        level += 1
        new_level = levels[level]
        enemy_ships.clear()
        enemy_missiles.clear()
        meteors.clear()
        missiles.clear()
        meteors_in_round = 0
        enemy_ships_in_round =0
        for x in range(0,15*TS,TS):
            for y in range(0,14*TS,TS):
                screen.blit(bg,(x,y))
        title.draw(screen)
        pygame.display.flip()
        title.delay()



font = pygame.font.Font(None, 32)
input_box = pygame.Rect(4*TS, 7*TS, 2*TS, TS)
user_text = ''
filename = "scores.txt"
box_status = False


running = 1
while running:
    filename = "scores.txt"
    events = pygame.event.get()
    for e in events:
        if e.type == pygame.QUIT:
            running = 0
        if e.type == pygame.MOUSEBUTTONDOWN and 7*TS < x < 8*TS and 7*TS < y < 10*TS:
            box_status = input_box.collidepoint(e.pos)
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_BACKSPACE:
                user_text = user_text[:-1]
            elif e.key == pygame.K_RETURN:
                with open(filename, 'a') as file_object:
                    file_object.write(f"{user_text}:{scoreboard.read_scoreboard()}\n")
                user_text = ''
                running = 0
            else:
                user_text += e.unicode
        else:
            active = False
            
    for x in range(0,15*TS,TS):
        for y in range(0,14*TS,TS):
            screen.blit(bg,(x,y))
    endtitle.draw(screen)
    
    
    txt_surface = font.render(user_text, True, (255,255,255))
    width = max(200,txt_surface.get_width()+10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
    pygame.draw.rect(screen, (255,255,255), input_box, 2)
    pygame.display.flip()


pygame.quit()