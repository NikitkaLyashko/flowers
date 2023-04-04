import random

import pygame
width_win=300
height_win=300
rect=pygame.Rect(250,0,50,100)

def drive_rect():
    global height_win, width_win
    rect.bottom+=5

    if rect.top<height_win and rect.bottom>=height_win:
        pygame.display.set_mode([width_win+3,height_win])
        width_win+=3

    if rect.top>=height_win:
        rect.bottom=0
        rect.width = random.randint(10, 50)
        rect.height = random.randint(10, 100)
        rect.left = random.randint(0, width_win)



