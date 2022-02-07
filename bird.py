import random
from sounds import *
from bullet import *
from images import *


class Birds:
    def __init__(self, away_y):
        self.x = random.randrange(550, 750)
        self.y = away_y
        self.width = 110
        self.height = 60
        self.ay = away_y
        self.speed = 3
        self.dest_y = self.speed * random.randrange(20, 70)
        self.img_cnt = 0
        self.cd_hide = 0
        self.fly = True
        self.fly_away = False
        self.cd_shoot = 0
        self.all_bullets = []

    def draw(self):
        if self.img_cnt == 30:
            self.img_cnt = 0

        display.blit(bird_img[self.img_cnt // 5], (self.x, self.y))
        self.img_cnt += 1

        if self.fly and self.cd_hide == 0:
            return 1
        elif self.fly_away:
            return 2
        elif self.cd_hide > 0:
            self.cd_hide -= 1

        return 0

    def show(self):
        if self.y < self.dest_y:
            self.y += self.speed
        else:
            self.fly = False
            self.fly_away = True
            self.dest_y = self.ay

    def hide(self):
        if self.y > self.dest_y:
            self.y -= self.speed
        else:
            self.fly = True
            self.fly_away = False
            self.x = random.randrange(550, 750)
            self.dest_y = self.speed * random.randrange(20, 70)
            self.cd_hide = 80

    def check_dmg(self, bullet):
        if self.x <= bullet.x <= self.x + self.width:
            if self.y <= bullet.y >= self.y + self.height:
                self.fly_away = True

    def shoot(self):
        if not self.cd_shoot:
            pygame.mixer.Sound.play(bullet_sound)
            new_bullet = Bullet(self.x, self.y)
            new_bullet.find_path(dino_x + dino_width // 2, dino_y + dino_height // 2)

            self.all_bullets.append(new_bullet)
            self.cd_shoot = 200
        else:
            self.cd_shoot -= 1

        for bullet in self.all_bullets:
            if not bullet.move_to(reverse=True):
                self.all_bullets.remove(bullet)
