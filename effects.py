from parameters import *
import parameters as p
from images import light_img

need_input = False
input_text = '|'
input_tick = 30


def print_text(message, x, y, font_colour=(0, 0, 0),
               font_type='D:\Projects\Python\Git\Dino\images\Effects/times-new-roman.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_colour)
    p.display.blit(text, (x, y))


def draw_mouse():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    mouse_size = [10, 12, 16, 20, 28, 34, 40, 45, 48, 54, 58]

    if click[0] or click[1]:
        p.need_draw_click = True

    if p.need_draw_click:
        draw_x = mouse[0] - mouse_size[p.mouse_counter] // 2
        draw_y = mouse[1] - mouse_size[p.mouse_counter] // 2

        p.display.blit(light_img[p.mouse_counter], (draw_x, draw_y))
        p.mouse_counter += 1

        if p.mouse_counter == 10:
            p.mouse_counter = 0
            p.need_draw_click = False


def get_input(x,y):
    global need_input, input_text, input_tick

    input_rect = pygame.Rect(x, y, 280, 70)

    pygame.draw.rect(p.display, (255, 255, 255), input_rect)

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if input_rect.collidepoint(mouse[0], mouse[1]) and click[0]:
        need_input = True

    if need_input:
        for event in pygame.event.get():
            if need_input and event.type == pygame.KEYDOWN:
                input_text = input_text.replace('|', '')
                input_tick = 30
                if event.key == pygame.K_RETURN:
                    need_input = False
                    message=input_text
                    input_text = ''
                    return message
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if len(input_text) < 11:
                        input_text += event.unicode
                input_text += '|'

    if len(input_text):
        print_text(message=input_text, x=input_rect.x + 10, y=input_rect.y + 10, font_size=50)

    input_tick -= 1

    if input_tick == 0:
        input_text = input_text[:- 1]
    if input_tick == -30:
        input_text += '|'
        input_tick = 30

    return None
