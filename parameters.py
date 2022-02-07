import pygame

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))

mouse_counter = 0
need_draw_click = False

dino_width = 60
dino_height = 80
dino_x = display_width // 3
dino_y = display_height - dino_height - 80

clock = pygame.time.Clock()
