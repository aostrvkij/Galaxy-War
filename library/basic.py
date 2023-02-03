from library.config import FPS, MENU_BTN, SETTING_BTN, LIBRARY_BTN, CONGAME_BTN
from pygame.display import flip
from pygame.key import get_pressed
from library import game_main
from pygame import event
import pygame


class Game:
    def __init__(self, screen):
        self.run_menu, self.run_game, self.run_settings, self.run_library, self.run_congame = \
            True, False, False, False, False

        self.menu_btn = MENU_BTN
        self.settings_btn = SETTING_BTN
        self.libr_btns = LIBRARY_BTN
        self.congame_btns = CONGAME_BTN
        self.screen = screen
        self.run_pause = None

    def menu(self):
        self.run_menu, self.run_game, self.run_settings, self.run_library, self.run_congame = \
            True, False, False, False, False
        while self.run_menu:
            self.screen.fill('black')
            self.menu_btn.update(self)
            self.menu_btn.draw(self.screen)
            flip()
            for e in event.get():
                if e.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_settings, self.run_library, self.run_congame = \
                        False, False, False, False, False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()

    def game(self):
        self.run_menu, self.run_game, self.run_settings, self.run_library, self.run_congame = \
            False, True, False, False, False
        game_main.main(FPS, 70, 5, [100, 100, 0, 1, None, None], self)
        self.menu()

    def settings(self):
        self.run_menu, self.run_game, self.run_settings, self.run_library, self.run_congame = \
            False, False, True, False, False
        while self.run_settings:
            self.screen.fill('black')
            self.settings_btn.update(self)
            self.settings_btn.draw(self.screen)
            flip()
            for e in event.get():
                if e.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_settings, self.run_library, self.run_congame = \
                        False, False, False, False, False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.menu()

    def game_over_menu(self):
        pass

    def pause_menu(self):
        self.run_menu, self.run_game, self.run_settings, self.run_library, self.run_congame = \
            False, False, False, False, True
        while self.run_congame:
            self.screen.fill('black')
            self.congame_btns.update(self)
            self.congame_btns.draw(self.screen)
            flip()
            if self.run_pause:
                self.run_pause = None
                return True

            for e in event.get():
                if e.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_settings, self.run_library, self.run_congame = \
                        False, False, False, False, False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        return True

    def library(self):
        self.run_menu, self.run_game, self.run_settings, self.run_library, self.run_congame = \
            False, False, False, True, False
        while self.run_library:
            self.screen.fill('black')
            self.libr_btns.update(self)
            self.libr_btns.draw(self.screen)
            flip()

            for e in event.get():
                if e.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_settings, self.run_library, self.run_congame = \
                        False, False, False, False, False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.menu()