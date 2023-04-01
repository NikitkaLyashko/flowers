import random

import pygame.display

import model

def background():

    window.fill([255,70,70])
    small_water=pygame.transform.scale(water,model.rect.size)
    window.blit(small_water,[model.rect.x,model.rect.y])

    pygame.display.flip()


window=pygame.display.set_mode([model.width_win,model.height_win])
water = pygame.image.load("images/water_drop.png")




