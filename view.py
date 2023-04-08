import random

import pygame.display

import model

def background():


    window.fill([255,70,70])
    small_water=pygame.transform.scale(water,model.rect.size)
    window.blit(small_water,[model.rect.x,model.rect.y])

    height_flovers_new=flower_1.get_height()*50/flower_1.get_width()
    flower_1_start=pygame.transform.scale(flower_1,[50,height_flovers_new])
    window.blit(flower_1_start, [0, model.height_win-flower_1_start.get_height()])

    rect_fl=pygame.draw.rect(window,[10,100,62],model.flower_rect)



    pygame.display.flip()


window=pygame.display.set_mode([model.width_win,model.height_win])
water = pygame.image.load("images/water_drop.png")
flower_1=pygame.image.load("images/flower1.png")
flower_2=pygame.image.load("images/flower2.png")




