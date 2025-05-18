from pygame import *
from random import randint as geforg
from time import time as timer



w_w, w_h = 700, 500

font.init()

font1 = font.Font(None, 50)
lose1 = font1.render('PLAYER 1 LOSE!', True, (180, 0, 0))
font2 = font.Font(None, 50)
lose2 = font2.render('PLAYER 2 LOSE!', True, (180, 0, 0))

win = display.set_mode((w_w, w_h))

display.set_caption('Пинг-понг')

background = transform.scale(image.load('backgroundd.png'), (w_w, w_h))
losee = transform.scale(image.load('losee.png'), (w_w, w_h))

clock = time.Clock()
FPS = 60
lost = 0
score = 0

# mixer.init()
# mixer.music.load('space.ogg')
# mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, player_size_x, player_size_y):
        super().__init__()
        self.player_size_x = player_size_x
        self.player_size_y = player_size_y
        self.image = transform.scale(image.load(player_image), (self.player_size_x, self.player_size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed

r, l = geforg(100, 600), geforg(50, 400)

player1 = Player('./Rocket1.png', 20, 20, 5, 32, 100)
player2 = Player('./Rocket1.png', 648, 400, 5, 32, 100)
ball = Player('./pngg.png', r, l, 3, 50, 50)

speed_x, speed_y = 3, 3
finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        win.blit(background,(0, 0))
        player1.reset()
        player1.update_l()
        player2.reset()
        player2.update_r()
        ball.update()
        ball.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > w_h - 50 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            finish = True
            losee = transform.scale(image.load('losee.png'), (w_w, w_h))
            win.blit(losee,(0, 0))
            win.blit(lose1, (200, 200))
        if ball.rect.x > 700:
            finish = True
            losee = transform.scale(image.load('losee.png'), (w_w, w_h))
            win.blit(losee,(0, 0))
            win.blit(lose2, (200, 200))

    display.update()
    clock.tick(FPS)