from library.config import FPS, MENU_BTN, SETTING_BTN, LIBRARY_BTN
from pygame.display import flip
from pygame.key import get_pressed
from pygame import event
import pygame


class Game:
    def __init__(self, screen, size, screen_width, screen_height):
        self.run_menu, self.run_game, self.run_settings, self.run_library = True, False, False, False

        self.menu_btn = MENU_BTN
        self.settings_btn = SETTING_BTN
        self.libr_btns = LIBRARY_BTN

        self.screen = screen

    def menu(self):
        self.run_menu, self.run_game, self.run_settings, self.run_library = True, False, False, False
        while self.run_menu:
            self.screen.fill('black')
            self.menu_btn.update(self)
            self.menu_btn.draw(self.screen)
            flip()

            keys = get_pressed()

            if keys[pygame.K_ESCAPE]:
                self.run_menu = False
                quit()
            for e in event.get():
                if e.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_settings, self.run_library = False, False, False, False

    def game(self):
        pass

    def settings(self):
        self.run_menu, self.run_game, self.run_settings, self.run_library = False, False, True, False
        while self.run_settings:
            self.screen.fill('black')
            self.settings_btn.update(self)
            self.settings_btn.draw(self.screen)
            flip()
            keys = get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.run_menu = False
                quit()
            for e in event.get():
                if e.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_settings, self.run_library = False, False, False, False

    def over_menu(self):
        pass

    def library(self):
        self.run_menu, self.run_game, self.run_settings, self.run_library = False, False, False, True
        while self.run_library:
            self.screen.fill('black')
            self.libr_btns.update(self)
            self.libr_btns.draw(self.screen)
            flip()
            keys = get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.run_menu = False
                quit()
            for e in event.get():
                if e.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_settings, self.run_library = False, False, False, False
