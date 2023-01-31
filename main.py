import pygame
# from library.buttons import Button
from library.config import screen, SCREEN_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
from library.basic import Game
# from library.buttons import Button
def run():
    pygame.init()
    game = Game(screen)
    game.menu()


if __name__ == '__main__':
    run()
