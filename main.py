from pygame import *
from random import randint
from time import time as timer


w_w, w_h = 700, 500

win = display.set_mode((w_w, w_h))

display.set_caption('Пинг-понг')

background = transform.scale(image.load('background.jpg'), (w_w, w_h))

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

player1 = Player('./Rocket.jpg', 20, 20, 5, 32, 100)
player2 = Player('./Rocket.jpg', 648, 400, 5, 32, 100)

finish = False
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        win.blit(background,(0, 0 ))
        player1.reset()
        player1.update_l()
        player2.reset()
        player2.update_r()

    display.update()
    clock.tick(FPS)