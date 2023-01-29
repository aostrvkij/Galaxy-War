import sys
import pygame

# --- constants --- (UPPER_CASE_NAMES)

WHITE = (255,255,255)
BLACK = (  0,  0,  0)

RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)

YELLOW = (255,255, 0)

# --- classes --- (CamelCaseNanes)

# empty

# --- functions --- (lower_case_names_

def button_create(text, rect, inactive_color, active_color, action):

    font = pygame.font.Font(None, 40)

    button_rect = pygame.Rect(rect)

    text = font.render(text, True, BLACK)
    text_rect = text.get_rect(center=button_rect.center)

    return [text, text_rect, button_rect, inactive_color, active_color, action, False]


def button_check(info, event):

    text, text_rect, rect, inactive_color, active_color, action, hover = info

    if event.type == pygame.MOUSEMOTION:
        # hover = True/False
        info[-1] = rect.collidepoint(event.pos)

    elif event.type == pygame.MOUSEBUTTONDOWN:
        if hover and action:
            action()


def button_draw(screen, info):

    text, text_rect, rect, inactive_color, active_color, action, hover = info

    if hover:
        color = active_color
    else:
        color = inactive_color

    pygame.draw.rect(screen, color, rect)
    screen.blit(text, text_rect)

# ---

def on_click_button_1():
    global stage
    stage = 'Buran'

    print('You clicked Button 1')

def on_click_button_2():
    global stage
    stage = 'options'

    print('You clicked Button 2')

def on_click_button_3():
    global stage
    global running

    stage = 'exit'
    running = False

    print('You clicked Button 3')

def on_click_button_return():
    global stage
    stage = 'menu'

    print('You clicked Button Return')

# --- main ---  (lower_case_names)

# - init -

pygame.init()
screen = pygame.display.set_mode((800,600))
screen_rect = screen.get_rect()

# - objects -

stage = 'menu'

button_1 = button_create("Buran", (300, 100, 200, 75), RED, GREEN, on_click_button_1)
button_2 = button_create("OPTIONS", (300, 200, 200, 75), RED, GREEN, on_click_button_2)
button_3 = button_create("EXIT", (300, 300, 200, 75), RED, GREEN, on_click_button_3)

button_return = button_create("RETURN", (300, 400, 200, 75), RED, GREEN, on_click_button_return)

# - mainloop -

running = True

while running:

    # - events -

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if stage == 'menu':
            button_check(button_1, event)
            button_check(button_2, event)
            button_check(button_3, event)
        elif stage == 'Buran':
            button_check(button_return, event)

        elif stage == 'options':
            button_check(button_return, event)
        #elif stage == 'exit':
        #    pass

    # - draws -

    screen.fill(BLACK)

    if stage == 'menu':
        button_draw(screen, button_1)
        button_draw(screen, button_2)
        button_draw(screen, button_3)
    elif stage == 'Buran':
        button_draw(screen, button_return)
        car_surf = pygame.image.load("Burancheme.jpg")
        car_rect = car_surf.get_rect(center=(900 // 2, 400 // 2))

        screen.blit(car_surf, car_rect)
    elif stage == 'options':
        button_draw(screen, button_return)
    #elif stage == 'exit':
    #    pass

    pygame.display.update()

# - end -

pygame.quit()
