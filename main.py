import pygame
from library.config import screen
from library.basic import Game


def run():
    pygame.init()
    game = Game(screen)
    game.menu()


if __name__ == '__main__':
    run()
