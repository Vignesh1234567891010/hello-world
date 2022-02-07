import pygame

pygame.init()

icon = pygame.image.load('D:\Projects\Python\Git\Dino\images\Backgrounds\icon.png')
menu_bkgr = pygame.image.load('D:\Projects\Python\Git\Dino\images\Backgrounds\Menu.jpg')
lvl2_bkgr = pygame.image.load('D:\Projects\Python\Git\Dino\images\Backgrounds\LandLevel.jpg')

land = pygame.image.load('D:\Projects\Python\Git\Dino\images\Backgrounds\land1.jpg')

cactus_img = [
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Objects\Cactus 0.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Objects\Сactus 1.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Objects\Cactus 2.png')]
cactus_options = [50, 460, 55, 430, 60, 420]

stone_img = [
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Objects\Stone 0.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Objects\Stone 1.png')
]

cloud_img = [
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Objects\cloud 0.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Objects\cloud 1.png')]

dino_img = [
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Dino\dino 0.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Dino\dino 1.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Dino\dino 2.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Dino\dino 3.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Dino\dino 4.png')]

bird_img = [
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Birds/bird 0.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Birds/bird 1.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Birds/bird 2.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Birds/bird 3.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Birds/bird 4.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Birds/bird 5.png'),
]

health_img = pygame.image.load('D:\Projects\Python\Git\Dino\images\Effects\heart.png')
health_img = pygame.transform.scale(health_img, (30, 30))

bullet_img = pygame.image.load('D:\Projects\Python\Git\Dino\images\Effects\shot.png')
bullet_img = pygame.transform.scale(bullet_img, (30, 10))

light_img = [
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Effects\Light0.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Effects\Light1.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Effects\Light2.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Effects\Light3.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Effects\Light4.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Effects\Light5.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Effects\Light6.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Effects\Light7.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Effects\Light8.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Effects\Light9.png'),
    pygame.image.load('D:\Projects\Python\Git\Dino\images\Effects\Light10.png')
]


def set_theme(num):
    global land
    land = pygame.image.load('D:\Projects\Python\Git\Dino\images\Backgrounds\land{}.jpg'.format(num))


def set_hero(num):
    global dino_img

    if num == 1:
        dino_img = [
            pygame.image.load('D:\Projects\Python\Git\Dino\images\Dino\dino 0.png'),
            pygame.image.load('D:\Projects\Python\Git\Dino\images\Dino\dino 1.png'),
            pygame.image.load('D:\Projects\Python\Git\Dino\images\Dino\dino 2.png'),
            pygame.image.load('D:\Projects\Python\Git\Dino\images\Dino\dino 3.png'),
            pygame.image.load('D:\Projects\Python\Git\Dino\images\Dino\dino 4.png')
        ]
    else:
        dino_img = [
            pygame.image.load('D:\Projects\Python\Git\Dino\images\Dino\Dino2_0.png'),
            pygame.image.load('D:\Projects\Python\Git\Dino\images\Dino\Dino2_1.png'),
            pygame.image.load('D:\Projects\Python\Git\Dino\images\Dino\Dino2_2.png'),
            pygame.image.load('D:\Projects\Python\Git\Dino\images\Dino\Dino2_3.png'),
            pygame.image.load('D:\Projects\Python\Git\Dino\images\Dino\Dino2_4.png')
        ]
