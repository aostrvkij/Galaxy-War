import library.classes
from library.config import FPS, MENU_BTN, SETTING_BTN, LIBRARY_BTN, CONGAME_BTN, OVER_BTN, INFO_BTN
from pygame.display import flip
from pygame.key import get_pressed
from library import game_main
from library.work_with_db import *
from pygame import event
import pygame


class Game:
    def __init__(self, screen):
        self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
            True, False, False, False, False, False
        self.menu_btn = MENU_BTN
        self.over_btn = OVER_BTN
        self.settings_btn = SETTING_BTN
        self.libr_btns = LIBRARY_BTN
        self.congame_btns = CONGAME_BTN
        self.info_btn = INFO_BTN
        self.screen = screen
        self.run_pause = None
        self.exit = None

    def menu(self):
        self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
            True, False, False, False, False, False
        while self.run_menu:
            self.screen.fill('black')
            self.menu_btn.update(self)
            self.menu_btn.draw(self.screen)
            flip()
            for e in event.get():
                if e.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
                        False, False, False, False, False, False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()

    def game(self):
        self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
            False, True, False, False, False, False
        info = read_info_ship()
        score, money = game_main.main(FPS, 70, 5, [info[1], info[2], info[3], info[4], eval(info[5]), eval(info[6])],
                                      self)
        self.run_game = False
        add_cell('Player', score)
        update_cell(1, 'money', money)
        if self.exit:
            self.exit = None
            self.menu()
        else:
            self.game_over(score)

    def game_over(self, score):
        self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
            False, False, True, False, False, False
        while self.run_over:
            self.screen.fill('black')
            self.over_btn.update(self)
            self.over_btn.draw(self.screen)
            flip()
            for e in event.get():
                if e.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
                        False, False, False, False, False, False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.menu()
        self.menu()

    def settings(self):
        self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
            False, False, False, True, False, False
        while self.run_settings:
            self.screen.fill('black')
            self.settings_btn.update(self)
            self.settings_btn.draw(self.screen)
            flip()
            for e in event.get():
                if e.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
                        False, False, False, False, False, False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.menu()

    def pause_menu(self):
        self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
            False, False, False, False, False, True
        while self.run_congame:
            self.screen.fill('black')
            self.congame_btns.update(self)
            self.congame_btns.draw(self.screen)
            flip()
            if self.run_pause:
                self.run_pause = None
                self.run_congame = False
                return True

            if self.exit:
                self.run_congame = False
                return False

            for e in event.get():
                if e.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
                        False, False, False, False, False, False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.run_congame = False
                        return True

    def library(self):
        self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
            True, False, False, False, True, False

        def info_of_shuttles(*some_info):
            run = True
            while run:
                self.screen.fill('black')

        while self.run_library:
            self.screen.fill('black')
            self.info_btn.update(self)
            self.info_btn.draw(self.screen)
            flip()

            for e in event.get():
                if e.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
                        False, False, False, False, False, False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.menu()

    def Buran(self):
        self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
            True, False, False, False, True, False
