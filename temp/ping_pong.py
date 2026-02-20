from pygame import *
init()

window = display.set_mode((700, 500))
window.fill((66,170,255))

clock = time.Clock()

chet = 0
chet_p1 = 0
chet_p2 = 0

class GameSprite(sprite.Sprite):
    def __init__(self, speed, x, y, player_file_name, w, h):
        super().__init__()
        self.speed = speed
        self.image = transform.scale(image.load(player_file_name), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Ball(GameSprite):
    def __init__(self, speed, x, y, player_file_name, w, h):
        super().__init__(speed, x, y, player_file_name, w, h)
        self.reverse = -1
        self.speed_x = self.speed
        self.speed_y = self.speed

    def update(self):
        global chet_p1
        global chet_p2
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.x <= 0:
            self.rect.x = 350
            self.rect.y = 350
            self.speed_x *= self.reverse
            chet_p2 += 1

        if self.rect.x >= 650:
            self.rect.x = 350
            self.rect.y = 350
            self.speed_x *= self.reverse
            chet_p1 += 1
         
        if self.rect.y <= 0 or self.rect.y >= 450:
            self.speed_y *= self.reverse
        
class Platform(GameSprite):
    def __init__(self, speed, x, y, player_file_name, w, h):
        super().__init__(speed, x, y, player_file_name, w, h)
        self.speed = speed
    
    def update(self):
        if key_pressed[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y <= 400:
            self.rect.y += self.speed

    def update_2(self):
        if key_pressed[K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y <= 400:
            self.rect.y += self.speed



ball1 = Ball(10, 350, 250, 'cyborg.png', 50, 50)
platform1 = Platform(10, 30, 250, 'gray_platform.png', 15, 100)
platform2 = Platform(10, 670, 250, 'gray_platform.png', 15, 100)

platforms = sprite.Group()
platforms.add(platform1)
platforms.add(platform2)

font1 = font.Font(None, 25)

game = True
while game:
    clock.tick(60)
    display.update()
    window.fill((66,170,255))
    ball1.reset()
    ball1.update()
    key_pressed = key.get_pressed()
    platform1.reset()
    platform1.update()
    platform2.reset()
    platform2.update_2()

    question = font1.render(
        'Счёт_p1: ' + str(chet_p1), True, (255, 255, 255)
    ) 
    window.blit(question, (25, 40))

    question = font1.render(
        'Счёт_p2: ' + str(chet_p2), True, (255, 255, 255)
    ) 
    window.blit(question, (25, 60))

    question = font1.render(
        'Общий счёт: ' + str(chet), True, (255, 255, 255)
    ) 
    window.blit(question, (25, 20))

    sprites_list = sprite.spritecollide(
        ball1, platforms, False
    )   

    sprites_list1 = sprite.collide_rect(
        ball1, platform1
    )   

    sprites_list2 = sprite.collide_rect(
        ball1, platform2
    )   

    if sprites_list1:
        ball1.speed_x *= ball1.reverse

    if sprites_list2:
        ball1.speed_x *= ball1.reverse

    if sprites_list:
        chet += 1

    for e in event.get():
        if e.type == QUIT:
            game = False
