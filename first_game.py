import pygame as pg

import random
import math
#<div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
#<div>Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>
#<div>Icons made by <a href="https://www.flaticon.com/authors/good-ware" title="Good Ware">Good Ware</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a></div>

pg.init()

height = 500
width = 500
screen = pg.display.set_mode((width, height))

pg.display.set_caption('First Game')

player_img = pg.image.load('spaceship.png')
player_x = 236
player_y = 450
move_x = 0

enemy_img = []
enemy_x = []
enemy_y = []
enemy_move_y = []
enemy_move_x = []
num_of_enemies = 3

for i in range(num_of_enemies):
    
    enemy_img.append(pg.image.load('ufo.png'))
    enemy_x.append(random.random()*468)
    enemy_y.append(20)
    enemy_move_y.append(0.01)
    enemy_move_x.append(0.1)
    

bullet_img = pg.image.load('bullet.png')
bullet_x = 0
bullet_y = 436
bullet_move_x = 0
bullet_move_y = -0.1
bullet_state = 'inactive'

score_value = 0
font = pg.font.Font('freesansbold.ttf', 16)
text_x = 10
text_y = 10

game_over_font = pg.font.Font('freesansbold.ttf', 32)

def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
    
def game_over_text():
    game_over_text = game_over_font.render('GAME OVER!', True, (255, 255, 255))
    screen.blit(game_over_text, (140, 240))

def player(x, y):
    screen.blit(player_img, (x, y))
    
def enemy(x, y, i):
    screen.blit(enemy_img[i], (x, y))
    
def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'active' 
    screen.blit(bullet_img, (x + 8, y + 16))
    
def is_collision(x1, x2, y1, y2):
    x1 += 8
    x2 += 8
    y1 += 8
    y2 += 8
    distance = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 -y1), 2))
    if distance < 16:
        return True
    else:
        return False
    
running = True
while running:

    screen.fill((0,0,100))

    for event in pg.event.get():
    
        if event.type == pg.QUIT:
            running = False
            
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                move_x = -0.1
            if event.key == pg.K_RIGHT:
                move_x = 0.1
            if event.key == pg.K_SPACE:
                if bullet_state == 'inactive':
                    bullet_x = player_x
                fire_bullet(bullet_x, bullet_y)
                
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or pg.K_RIGHT:
                move_x = 0   
               

    player_x += move_x
    
    if player_x <= 0:
        player_x = 0
    if player_x >= 468:
        player_x = 468
    
    
    for i in range(num_of_enemies):
    
        enemy_x[i] += enemy_move_x[i]                 #(random.random() - 0.5) * random.randint(3, 5)
        enemy_y[i] += enemy_move_y[i]
        
        if enemy_y[i] >= 436:
            for j in range(num_of_enemies):    
                enemy_x[j] = 2000
                enemy_y[j] = 2000
            game_over_text()
    
        if enemy_x[i] <= 0:
            enemy_x[i] = 0
            enemy_move_x[i] = -enemy_move_x[i]
        if enemy_x[i] >= 468:
            enemy_x[i] = 468
            enemy_move_x[i] = -enemy_move_x[i]
        
    if bullet_y <= 0:
        bullet_y = 436
        bullet_state = 'inactive'
    if bullet_state == 'active':
        fire_bullet(bullet_x, bullet_y)
        bullet_y += bullet_move_y
    
    for i in range(num_of_enemies):
    
        collision = is_collision(bullet_x, enemy_x[i], bullet_y, enemy_y[i])
    
        if collision:
            bullet_y = 436
            bullet_state = 'inactive'
            score_value += 1
            print(score_value)
            enemy_x[i] = random.random()*468
            enemy_y[i] = 20
            
    player(player_x, player_y)
    
    for i in range(num_of_enemies):
    
        enemy(enemy_x[i], enemy_y[i], i)
     
    show_score(text_x, text_y)
        
    
    pg.display.update()
