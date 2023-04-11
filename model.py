import random

import pygame
width_win=100
height_win=300
rect=pygame.Rect(250,0,50,100)
flower_rect = pygame.Rect(100, 250, 50, 100)
flower_rect.left=0

flower_rect_2=pygame.Rect(100, 250, 50, 100)


def drive_rect():
    global height_win, width_win, flower_rect
    rect.bottom+=5

    if rect.top<height_win and rect.bottom>=height_win:
        pygame.display.set_mode([width_win+3,height_win])
        width_win+=3

    flower_rect.width = width_win / 2
    flower_rect.height=flower_rect.width*2
    flower_rect.bottom=height_win

    flower_rect_2.left = width_win / 2
    flower_rect_2.width = width_win / 2
    flower_rect_2.height = flower_rect.width * 2
    flower_rect_2.bottom=height_win




    if rect.top>=height_win:
        rect.bottom=0
        rect.width = random.randint(10, 50)
        rect.height = random.randint(10, 100)
        rect.left = random.randint(0, width_win)


