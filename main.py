import pygame
from library.config import screen
from library.basic import Game


def run():
    pygame.mixer.pre_init(44100, -16 * 5, 100, 512 * 5)
    pygame.init()
    game = Game(screen)
    game.menu()


if __name__ == '__main__':
    run()
