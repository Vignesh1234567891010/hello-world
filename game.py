from button import *
from bird import *
from object import *
import images as img
from states import *
from save import *
from inventory import inventory
from time import sleep
from highscore import *


class Game:
    def __init__(self):
        pygame.display.set_caption('Run Dino! Run!')
        pygame.display.set_icon(icon)

        pygame.mixer.music.load('D:\Projects\Python\Git\Dino\images\Sounds\Big_Slinker.mp3')
        pygame.mixer.music.set_volume(0.5)

        self.level = 1
        self.cactus_options = [50, 460, 55, 430, 60, 420]
        self.img_counter = 0
        self.health = 3
        self.make_jump = False
        self.jump_counter = 30
        self.jump_num = 0
        self.scores = 0
        self.max_scores = 0
        self.max_above = 0
        self.cooldown = 0
        self.game_state = GameState()

        self.save_data = Save()
        self.high_scores = HighScore(self.save_data.get('hs'))
        # self.save_data.get('hs', {})
        # print(self.save_data.get('hs'))

    def start(self):

        while True:
            if self.game_state.check(State.MENU):
                self.show_menu()
            elif self.game_state.check(State.START):
                self.choice_theme()
                self.choice_hero()
                self.start_game()

            elif self.game_state.check(State.CONTINUE):
                self.max_scores = self.save_data.get('max')
                self.start_game()
            elif self.game_state.check(State.LEVEL_2):
                self.level_2()
            elif self.game_state.check(State.QUIT):
                self.save_data.save()
                self.save_data.add('max', self.max_scores)
                print(self.save_data.get('hs'))
                break

    def show_menu(self):

        pygame.mixer.music.load('D:\Projects\Python\Git\Dino\images\Sounds\Big_Slinker.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        start_btn = Button(288, 70)
        continue_btn = Button(430, 70)
        lvl2_btn = Button(240, 70)
        quit_btn = Button(160, 70)
        show = True

        while show:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            display.blit(menu_bkgr, (0, 0))

            if start_btn.draw(230, 200, 'Начало игры', font_size=50):
                self.game_state.change(State.START)
                return

            if lvl2_btn.draw(250, 300, 'Уровень 2', font_size=50):
                self.game_state.change(State.LEVEL_2)
                return

            if continue_btn.draw(170, 400, 'Продолжение игры', font_size=50):
                self.game_state.change(State.CONTINUE)
                return

            if quit_btn.draw(300, 500, 'Выход', font_size=50):
                self.game_state.change(State.QUIT)
                return

            print_text(input_text, 500, 400, font_colour=(255, 255, 150))

            pygame.display.update()
            # clock.tick(60)

    def start_game(self):

        pygame.mixer.music.load('D:\Projects\Python\Git\Dino\images\Sounds/background.mp3')
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)

        while self.game_cycle():
            self.scores = 0
            self.make_jump = False
            self.jump_counter = 30
            p.dino_y = p.display_height - p.dino_height - 80
            self.health = 3
            self.cooldown = 0

    def jump(self):
        if self.jump_counter >= -30:
            if self.jump_counter == 30:
                pygame.mixer.Sound.play(jump_sound)
            if self.jump_counter == -10:
                pygame.mixer.Sound.play(fall_sound)

            p.dino_y -= self.jump_counter / 2.5
            self.jump_counter -= 1
        else:
            if p.dino_y < 440:
                p.dino_y = min(440, p.dino_y - self.jump_counter / 2.5)
                self.jump_counter -= 1
            else:
                self.jump_num = 0
                self.jump_counter = 30
                self.make_jump = False

    @staticmethod
    def find_radius(array):
        maximum = max(array[0].x, array[1].x, array[2].x)

        if maximum < display_width:
            radius = display_width
            if radius - maximum < 50:
                radius += 300
        else:
            radius = maximum
        choice = random.randrange(0, 5)
        if choice == 0:
            radius += random.randrange(10, 15)
        else:
            radius += random.randrange(250, 400)

        return radius

    def object_return(self, objects, obj):
        radius = self.find_radius(objects)

        choice = random.randrange(0, 3)
        img = cactus_img[choice]
        width = self.cactus_options[choice * 2]
        height = self.cactus_options[choice * 2 + 1]

        obj.return_self(radius, height, width, img)

    @staticmethod
    def open_random_objects():
        choice = random.randrange(0, 2)
        img_of_stone = stone_img[choice]

        choice = random.randrange(0, 2)
        img_of_cloud = cloud_img[choice]

        stone = Object(display_width, display_height - 80, 10, img_of_stone, 4)
        cloud = Object(display_width, 80, 80, img_of_cloud, 2)
        return stone, cloud

    @staticmethod
    def move_objects(stone, cloud):
        check = stone.move()
        if not check:
            choice = random.randrange(0, 2)
            img_of_stone = stone_img[choice]
            stone.return_self(p.display_width, 500 + random.randrange(10, 80), stone.width, img_of_stone)

        check = cloud.move()
        if not check:
            choice = random.randrange(0, 2)
            img_of_cloud = cloud_img[choice]
            cloud.return_self(p.display_width, random.randrange(10, 200), cloud.width, img_of_cloud)

    def draw_dino(self):
        if self.img_counter == 25:
            self.img_counter = 0

        display.blit(img.dino_img[self.img_counter // 5], (p.dino_x, p.dino_y))
        self.img_counter += 1

    @staticmethod
    def draw_birds(birds):
        for bird in birds:
            action = bird.draw()
            if action == 1:
                bird.show()
            elif action == 2:
                bird.hide()
            else:
                bird.shoot()

    @staticmethod
    def check_birds_dmg(bullets, birds):
        for bird in birds:
            for bullet in bullets:
                bird.check_dmg(bullet)

    def draw_array(self, array):
        for cactus in array:
            check = cactus.move()
            if not check:
                self.object_return(array, cactus)

    def create_cactus_arr(self, array):
        choice = random.randrange(0, 3)
        img = cactus_img[choice]
        width = self.cactus_options[choice * 2]
        height = self.cactus_options[choice * 2 + 1]
        array.append(Object(display_width + 20, height, width, img, 4))

        choice = random.randrange(0, 3)
        img = cactus_img[choice]
        width = self.cactus_options[choice * 2]
        height = self.cactus_options[choice * 2 + 1]
        array.append(Object(display_width + 300, height, width, img, 4))

        choice = random.randrange(0, 3)
        img = cactus_img[choice]
        width = self.cactus_options[choice * 2]
        height = self.cactus_options[choice * 2 + 1]
        array.append(Object(display_width + 600, height, width, img, 4))

    def check_collision(self, barriers):
        for barrier in barriers:
            if barrier.y == 460:  # little cactus
                if not self.make_jump:
                    if barrier.x <= p.dino_x + p.dino_width - 30 <= barrier.x + barrier.width:
                        if self.check_health():
                            self.object_return(barriers, barrier)
                            return False
                        else:
                            return True
                elif self.jump_counter >= 0:
                    if p.dino_y + p.dino_height - 5 >= barrier.y:
                        if barrier.x <= p.dino_x + p.dino_width - 40 <= barrier.x + barrier.width:
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
                else:
                    if p.dino_y + p.dino_height - 10 >= barrier.y:
                        if barrier.x <= p.dino_x <= barrier.x + barrier.width:
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
            else:
                if not self.make_jump:
                    if barrier.x <= p.dino_x + p.dino_width - 30 <= barrier.x + barrier.width:
                        if self.check_health():
                            self.object_return(barriers, barrier)
                            return False
                        else:
                            return True
                elif self.jump_counter >= 10:
                    if p.dino_y + p.dino_height - 5 >= barrier.y:
                        if barrier.x <= p.dino_x + p.dino_width - 5 <= barrier.x + barrier.width:
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
                elif self.jump_counter >= -1:
                    if p.dino_y + p.dino_height - 10 >= barrier.y:
                        if barrier.x <= p.dino_x + p.dino_width - 30 <= barrier.x + barrier.width:
                            if self.check_health():
                                self.object_return(barriers, barrier)
                                return False
                            else:
                                return True
                        else:
                            if p.dino_y + p.dino_height - 10 >= barrier.y:
                                if barrier.x <= p.dino_x <= barrier.x + barrier.width:
                                    if self.check_health():
                                        self.object_return(barriers, barrier)
                                        return False
                                    else:
                                        return True
        return False

    def count_scores(self, barriers):
        above_cactus = 0

        if -20 <= self.jump_counter < 20:
            for barrier in barriers:
                if p.dino_y + p.dino_height - 5 <= barrier.y:
                    if barrier.x <= p.dino_x <= barrier.x + barrier.width:
                        above_cactus += 1
                    elif barrier.x <= p.dino_x + p.dino_width <= barrier.x + barrier.width:
                        above_cactus += 1
            self.max_above = max(self.max_above, above_cactus)
        else:
            if self.jump_counter == -30:
                self.scores += self.max_above
                self.max_above = 0

    def hearts_plus(self, heart):

        if heart.x <= -heart.width:
            radius = p.display_width + random.randrange(500, 1500)
            heart.return_self(radius, heart.y, heart.width, heart.image)

        if p.dino_x <= heart.x <= p.dino_x + p.dino_width:
            if p.dino_y <= heart.y <= p.dino_y + p.dino_height:
                pygame.mixer.Sound.play(heart_plus_sound)
                if self.health < 5:
                    self.health += 1

                radius = p.display_width + random.randrange(500, 1700)
                heart.return_self(radius, heart.y, heart.width, heart.image)

    def show_health(self):
        show = 0
        x = 20
        while show != self.health:
            display.blit(health_img, (x, 20))
            x += 38
            show += 1

    def check_health(self):
        self.health -= 1
        if self.health == 0:
            pygame.mixer.Sound.play(loss_sound)
            return False
        else:
            pygame.mixer.Sound.play(fall_sound)
            return True

    @staticmethod
    def choice_theme():
        theme_1 = Button(300, 70)
        theme_2 = Button(300, 70)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            display.fill((255, 255, 255))

            if theme_1.draw(250, 200, 'Дневня тема', font_size=50):
                set_theme(1)
                return
            if theme_2.draw(250, 300, 'Ночная тема', font_size=50):
                set_theme(2)
                return

            pygame.display.update()
            clock.tick(60)

    @staticmethod
    def choice_hero():
        hero_1 = Button(300, 70)
        hero_2 = Button(300, 70)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            display.fill((255, 255, 255))

            if hero_1.draw(250, 200, 'Синий', font_size=50):
                set_hero(1)
                return
            if hero_2.draw(250, 300, 'Зеленый', font_size=50):
                set_hero(2)
                return

            pygame.display.update()
            clock.tick(60)

    def choice_level(self):
        lvl_1 = Button(300, 70)
        lvl_2 = Button(300, 70)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            display.fill((255, 255, 255))

            if lvl_1.draw(250, 200, 'Уровень 1', font_size=50):
                self.level = 1
                return
            if lvl_2.draw(250, 300, 'Уровень 2', font_size=50):
                self.level = 2
                return

            pygame.display.update()
            clock.tick(60)

    def level_2(self):

        pygame.mixer.music.play(-1)
        game = True
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                self.make_jump = True
                if 0 < self.jump_counter < 27:
                    if not self.jump_num:
                        self.jump_num += 1
                        self.jump_counter = 30

            if self.make_jump:
                self.jump()

            display.blit(img.land, (0, 0))

            self.draw_dino()

            if keys[pygame.K_ESCAPE]:
                self.pause()

            self.show_health()

            draw_mouse()
            pygame.display.update()
            clock.tick(80)
        return self.game_over()

    @staticmethod
    def pause():
        paused = True

        pygame.mixer.music.pause()

        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            print_text('Пауза. Нажмите Enter чтобы продолжить', 160, 300)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                paused = False
            pygame.display.update()
            clock.tick(15)

        pygame.mixer.music.unpause()

    def game_cycle(self):

        pygame.mixer.music.play(-1)

        game = True
        cactus_arr = []
        self.create_cactus_arr(cactus_arr)

        stone, cloud = self.open_random_objects()
        heart = Object(display_width, 280, 30, health_img, 4)

        all_btn_bullets = []
        all_ms_bullets = []

        bird1 = Birds(-80)
        bird2 = Birds(-80)

        all_birds = [bird1, bird2]

        hold_left = True

        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            keys = pygame.key.get_pressed()
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            if click[0] and not hold_left:
                print(mouse)
                inventory.set_start_cell(mouse[0], mouse[1])
                hold_left = True
            if hold_left and not click[0]:
                print(pygame.mouse.get_pos())
                inventory.set_end_cell(mouse[0], mouse[1])
                hold_left = False

            if keys[pygame.K_SPACE]:
                self.make_jump = True
                if 0 < self.jump_counter < 27:
                    if not self.jump_num:
                        self.jump_num += 1
                        self.jump_counter = 30

            if self.make_jump:
                self.jump()

            self.count_scores(cactus_arr)

            print_text('Scores: ' + str(self.scores), 660, 10)

            display.blit(img.land, (0, 0))

            inventory.draw_panel()

            if keys[pygame.K_TAB]:
                inventory.draw_whole()
            if keys[pygame.K_1]:
                inventory.increase("coal")
                sleep(0.1)
            if keys[pygame.K_2]:
                inventory.increase("emerald")
                sleep(0.1)
            if keys[pygame.K_3]:
                inventory.increase("ruby")
                sleep(0.1)
            if keys[pygame.K_q]:
                game = False

            self.draw_array(cactus_arr)
            self.move_objects(stone, cloud)

            self.draw_dino()

            if keys[pygame.K_ESCAPE]:
                self.pause()

            if not self.cooldown:
                if keys[pygame.K_m]:
                    pygame.mixer.Sound.play(bullet_sound)
                    all_btn_bullets.append(Bullet(p.dino_x + p.dino_width, p.dino_y + 28))
                    self.cooldown = 50
                elif click[0]:
                    pygame.mixer.Sound.play(bullet_sound)
                    add_bullet = (Bullet(p.dino_x + p.dino_width, p.dino_y + 28))
                    add_bullet.find_path(mouse[0], mouse[1])

                    all_ms_bullets.append(add_bullet)
                    self.cooldown = 50
            else:
                print_text('Cooldown time: ' + str(self.cooldown // 10), 570, 40)
                self.cooldown -= 1
            for bullet in all_btn_bullets:
                if not bullet.move():
                    all_btn_bullets.remove(bullet)

            for bullet in all_ms_bullets:
                if not bullet.move_to():
                    all_ms_bullets.remove(bullet)

            heart.move()
            self.hearts_plus(heart)

            if self.check_collision(cactus_arr):
                pygame.mixer.music.stop()
                game = False

            self.show_health()

            self.draw_birds(all_birds)
            self.check_birds_dmg(all_ms_bullets, all_birds)

            draw_mouse()
            pygame.display.update()
            clock.tick(80)
        return self.game_over()

    def game_over(self):
        if self.scores > self.max_scores:
            self.max_scores = self.scores

        stopped = True
        get_name = False

        while stopped:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            display.blit(img.land, (0, 0))

            print_text('Game over. Press Tab to play again, Esc to exit', 100, 370)
            print_text('Max scores: ' + str(self.max_scores), 270, 320)

            if not get_name:
                print_text('Введите свое имя: ', 30, 150)
                name = get_input(30, 200)
                if name:
                    get_name = True
                    print(name)
                    self.high_scores.update(name, self.scores)
            else:
                print_text("name", 30, 150)
                print_text("Scores", 250, 150)
                self.high_scores.print(30, 200)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_TAB]:
                return True
            if keys[pygame.K_ESCAPE]:
                self.game_state.change(State.QUIT)
                return False

            pygame.display.update()
            # clock.tick(15)
