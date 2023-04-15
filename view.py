import random

import pygame.display

import model

def background():


    window.fill([255,70,70])
    small_water=pygame.transform.scale(water,model.rect.size)
    window.blit(small_water,[model.rect.x,model.rect.y])

    flower_view_1=pygame.transform.scale(flower_1,model.flower_rect.size)
    window.blit(flower_view_1,model.flower_rect.topleft)

    flower_view_2=pygame.transform.scale(flower_2,model.flower_rect_2.size)
    window.blit(flower_view_2,model.flower_rect_2.topleft)


    pygame.display.flip()


window=pygame.display.set_mode([model.width_win,model.height_win])
window=pygame.display.set_mode([model.width_win,model.height_win])
water = pygame.image.load("images/water_drop.png")
flower_1=pygame.image.load("images/flower1.png")
flower_2=pygame.image.load("images/flower2.png")




