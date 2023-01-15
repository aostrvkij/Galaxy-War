import pygame.display


class Game:
    def __init__(self):
        self.screen_size = self.screen_width, self.screen_height = \
            pygame.display.Info().current_w, pygame.display.Info().current_h
        self.fps = 60

