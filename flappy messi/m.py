from typing import Any
from pygame import*
from random import *

import math  

over = False

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_w, player_h, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_w, player_h)) #100 60
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class PLayer(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        
        if not(keys_pressed[K_SPACE]):
            self.rect.y += self.speed
        else:
            self.rect.y -= self.speed

class Prop(GameSprite):
    def update(self):
        side = random.randint(1,2)
        if side == 1:
            pass
        pass





score = 0
t = 1



window = display.set_mode((1200, 900))
display.set_caption('Flappy Messi')


bg = GameSprite('fon.png', 1200, 900, 0, 0, 0)

pl = PLayer('p1.jpg', 100, 200, 70, 300, 3 )

font.init()
font = font.Font(None, 70)

score_t = None 

s_txt = font.render(score_t, True, (255, 255 , 0))
lose = font.render('Ты проиграл ', True, (255, 0, 0))




clock = time.Clock()
FPS = 60

game = True

while game:
    if not over:
        t -= 1
        if t <= 0:
            score += 1
            t = 10
            score_t = "Счет: " + str(score)
            s_txt = font.render(score_t, True, (255, 255 , 0))


        bg.update()
        bg.reset()



        pl.update()
        pl.reset()

        if pl.rect.y >= 700:
            over = True
            window.blit(lose, (450, 350))
            window.blit(s_txt,(450, 450))


    for e in event.get():
        if e.type == QUIT:
            game = False



    display.update()
    clock.tick(FPS)