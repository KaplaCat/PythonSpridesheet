import pygame, time
from Views.Character.SpriteSheet import SpriteSheet

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_sheet = SpriteSheet('Tex/sprite.png')


BG = (50, 50, 50)
BLACK = (0, 0, 0)

idle_up = sprite_sheet.image_at((6,3,18,33), BLACK)
move_up_1 = sprite_sheet.image_at((38,2,18,33), BLACK)
move_up_2 = sprite_sheet.image_at((70,2,18,33), BLACK)
move_up = [move_up_1,move_up_2]
##
idle_down = sprite_sheet.image_at((5,35,19,33), BLACK)
move_down_1 = sprite_sheet.image_at((37,35,19,33), BLACK)
move_down_2 = sprite_sheet.image_at((69,35,19,33), BLACK)
move_down = [move_down_1,move_down_2]
##
idle_left = sprite_sheet.image_at((4,68,19,32), BLACK)
move_left_1 = sprite_sheet.image_at((36,68,19,32), BLACK)
move_left_2 = sprite_sheet.image_at((68,68,19,32), BLACK)
move_left = [move_left_1,move_left_2]
##
idle_right = sprite_sheet.image_at((7,100,18,32), BLACK)
move_right_1 = sprite_sheet.image_at((39,100,18,32), BLACK)
move_right_2 = sprite_sheet.image_at((71,100,18,32), BLACK)
move_right = [move_right_1,move_right_2]

run = True
pos_x = 250
pos_y = 250
direction = 0
vitesse = 0.1
pas = 3


def update():
    global pos_x, pos_y
    if(pos_x >= 481):
        pos_x = 481
    if(pos_x <= 0):
        pos_x = 0
    if(pos_y <= 0):
        pos_y = 0
    if(pos_y >= 468):
        pos_y = 468

current_image = 0
while run:
    screen.fill(BG)



    keys = pygame.key.get_pressed()

    if(keys[pygame.K_TAB]):
        if(vitesse == 0.1):
            vitesse = 0.01
        else:
            vitesse = 0.1
        time.sleep(0.1)
        
    if(keys[pygame.K_z]):
        direction = 1
        current_image += 1
        pos_y -= pas
        update()
        if current_image == len(move_up):
            current_image = 0
        screen.blit(move_up[current_image], (pos_x, pos_y))
        time.sleep(vitesse)
       
    elif(keys[pygame.K_s]):
        direction = 0
        current_image += 1
        pos_y += pas
        update()
        if current_image == len(move_down):
            current_image = 0
        screen.blit(move_down[current_image], (pos_x, pos_y))
        time.sleep(vitesse)
    
    elif(keys[pygame.K_q]):
        direction = 2
        current_image += 1
        pos_x -= pas
        update()
        if current_image == len(move_left):
            current_image = 0
        screen.blit(move_left[current_image], (pos_x, pos_y))
        time.sleep(vitesse)
    
    elif(keys[pygame.K_d]):
        direction = 3
        current_image += 1
        pos_x += pas
        update()
        if current_image == len(move_right):
            current_image = 0
        screen.blit(move_right[current_image], (pos_x, pos_y))
        time.sleep(vitesse)

    else:
        if direction == 0:
            screen.blit(idle_down, (pos_x, pos_y))
        elif direction == 1:
            screen.blit(idle_up, (pos_x, pos_y))
        elif direction == 2:
            screen.blit(idle_left, (pos_x, pos_y))
        elif direction == 3:
            screen.blit(idle_right, (pos_x, pos_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    pygame.display.update()

pygame.quit()