import pygame
import time
import sys
from pygame.locals import *

clock = pygame.time.Clock()
pygame.init()


width = 750
height = 600
win = pygame.display.set_mode((width,height))
game_on = True

player = pygame.image.load('charmove/walk/walk_0.png')



player_x=10
player_y=10
player_direction = 'down'
player_frame = 0
#player_image = player[player_direction][player_frame]
player_offset_x, player_offset_y = (0,0)



def game_loop():
    global player_x, player_y
    global from_player_x, from_player_y
    global player_image, player_image_shadow
    global selected_item, item_carrying, energy
    global player_offset_x, player_offset_y
    global player_frame, player_direction
    
    if game_on == False:
        return
    
    
    if player_frame > 0:
        player_frame += 1
        if player_frame == 5:
             player_frame = 0
             player_offset_x = 0
             player_offset_y = 0
    old_player_x = player_x
    old_player_y = player_y

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            
            if player_frame == 0:
                if event.key == K_RIGHT:
                    from_player_x = player_x
                    from_player_y = player_y
                    player_x += 1
                    player_direction = 'right'
                    player_frame += 1
                elif event.key == K_LEFT:
                    from_player_x = player_x
                    from_player_y = player_y
                    player_x -= 1
                    player_direction = 'left'
                    player_frame += 1
                elif event.key == K_UP:
                    from_player_x = player_x
                    from_player_y = player_y
                    player_y -= 1
                    player_direction = 'up'
                    player_frame += 1
                elif event.key == K_DOWN:
                    from_player_x = player_x
                    from_player_y = player_y
                    player_y += 1
                    player_direction = 'down'
                    player_frame += 1
                
                if player_direction == 'right' and player_frame > 0:
                    player_offset_x = -1 + (0.25 * player_frame)
                if player_direction == 'left' and player_frame > 0:
                    player_offset_x = 1 - (0.25 * player_frame)
                if player_direction == 'up' and player_frame > 0:
                    player_offset_y = 1 - (0.25 * player_frame)
                if player_direction == 'down' and player_frame > 0:
                    player_offset_y = -1 + (0.25 * player_frame)








while game_on:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    win.fill((146,244,255))
    
    game_loop()

    #image_to_draw = player[player_direction][player_frame]
    win.blit(player, (player_x,player_y))
    








    pygame.display.update()
    clock.tick(30)
