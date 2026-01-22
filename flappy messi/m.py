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
        # side = random.randint(1,2)
        # if side == 1:
        #     self.rect.y = randint(-10, 30)
        # else:
        #     self.rect.y = randint(900, 950)
        self.rect.x -= self.speed





score = 0
t = 1



window = display.set_mode((1200, 900))
display.set_caption('Flappy Messi')


bg = GameSprite('fon.png', 1200, 900, 0, 0, 0)

pl = PLayer('p1.jpg', 100, 200, 70, 300, 5)

igrok = sprite.Group(pl)
pr = sprite.Group()

for i in range(10):
    side = randint(1,2)
    if side == 1:
        vis = randint(-10, 5)
    else:
        vis = randint(880, 950)
    lim = Prop('lim.jpg', 125, randint(100, 150), 1200, vis, 5 )
    pr.add(lim)




font.init()
font = font.Font(None, 70)

score_t = None 
cd = 0


s_txt = font.render(score_t, True, (255, 255 , 0))
lose = font.render('Ты проиграл ', True, (255, 0, 0))




clock = time.Clock()
FPS = 60

game = True

while game:

    if not over:
        cd -= 1
        t -= 1
        if t <= 0:
            score += 1
            t = 10
            score_t = "Счет: " + str(score)
            s_txt = font.render(score_t, True, (255, 255 , 0))


        

        bg.update()
        bg.reset()

        igrok.update()
        igrok.draw(window)

        pr.update()
        pr.draw(window)
        if cd <= 0:
            side = randint(1,2)
            if side == 1:
                vis = randint(-10, 5)
            else:
                vis = randint(700, 800)
            lim = Prop('lim.jpg', 125, randint(200, 600), 1200, vis, 5 )
            pr.add(lim)
            cd = randint(65, 71)
        

        if sprite.groupcollide(igrok, pr, False, False):
            over = True
            window.blit(lose, (450, 350))
            window.blit(s_txt,(450, 450))
        if (pl.rect.y >= 700) or (pl.rect.y <= -50):
            over = True
            window.blit(lose, (450, 350))
            window.blit(s_txt,(450, 450))


    for e in event.get():
        if e.type == QUIT:
            game = False



    display.update()
    clock.tick(FPS)