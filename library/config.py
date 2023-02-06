import pygame
from library.buttons import Button

pygame.init()
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h))
clock = pygame.time.Clock()

FPS = 60
MENU_BTN = pygame.sprite.Group()
OVER_BTN = pygame.sprite.Group()
SETTING_BTN = pygame.sprite.Group()
LIBRARY_BTN = pygame.sprite.Group()
INFO_BTN = pygame.sprite.Group()
CONGAME_BTN = pygame.sprite.Group()

var_menu = [
    Button('Images/btns/newgame.png', 'newgame', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2,
           SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 - SCREEN_HEIGHT * 0.08 * 2),
    Button('Images/btns/hightscore.png', 'hightscore', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2,
           SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 - SCREEN_HEIGHT * 0.08 * 1),
    Button('Images/btns/shop.png', 'shop', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2,
           SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 - SCREEN_HEIGHT * 0.08 * 0),
    Button('Images/btns/settings.png', 'settgame', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2,
           SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 + SCREEN_HEIGHT * 0.08 * 1),
    Button('Images/btns/library.png', 'library', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2,
           SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 + SCREEN_HEIGHT * 0.08 * 2),
    Button('Images/btns/exit.png', 'exit', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2,
           SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 + SCREEN_HEIGHT * 0.08 * 3)]



var_over = [
    Button('Images/btns/exit.png', 'exit', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2,
           SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 + SCREEN_HEIGHT * 0.08 * 2)]
var_sett = [
    Button('Images/btns/newgame.png', 'newgame', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2,
           SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 - SCREEN_HEIGHT * 0.08 * 2),
    Button('Images/btns/exit.png', 'menu', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2,
           SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 - SCREEN_HEIGHT * 0.08)]

var_cong = [
    Button('Images/btns/congame.png', 'congame', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2,
           SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 - SCREEN_HEIGHT * 0.08 * 2),
    Button('Images/btns/exit.png', 'menu', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2,
           SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 - SCREEN_HEIGHT * 0.08)]

var_info = [
    Button('Images/btn_info/Buran1.png', 'buran', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2,
           SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 - SCREEN_HEIGHT * 0.08 * 2),
    Button('Images/btn_info/Sputnik_1.png', 'sputnik', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2),
    Button('Images/btn_info/Uragan.png', 'uragan', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2,
           SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 + SCREEN_HEIGHT * 0.08),
    Button('Images/btn_info/exit.png', 'exit', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2,
           SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 + SCREEN_HEIGHT * 0.08 * 2)]


for i in var_menu:
    MENU_BTN.add(i)
for i in var_info:
    INFO_BTN.add(i)
for i in var_over:
    OVER_BTN.add(i)
for i in var_sett:
    SETTING_BTN.add(i)
for i in var_cong:
    CONGAME_BTN.add(i)
