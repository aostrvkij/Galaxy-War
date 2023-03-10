import datetime

import library.classes
from library.config import FPS, MENU_BTN, SETTING_BTN, LIBRARY_BTN, CONGAME_BTN, OVER_BTN, INFO_BTN, \
    SCREEN_HEIGHT, SCREEN_WIDTH, HIGHT_BTN, INFO_SHATLE_BTN
from pygame.display import flip
from pygame.key import get_pressed
from library import game_main
from library.work_with_db import *
from pygame import event
import pygame


class Game:
    def __init__(self, screen):
        self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame, self.run_info = \
            True, False, False, False, False, False, False
        self.menu_btn = MENU_BTN
        self.over_btn = OVER_BTN
        self.settings_btn = SETTING_BTN
        self.libr_btns = LIBRARY_BTN
        self.congame_btns = CONGAME_BTN
        self.info_btn = INFO_BTN
        self.hight_btn = HIGHT_BTN
        self.info_shatle_btn = INFO_SHATLE_BTN
        self.count_enemy = 5
        self.spawn_enemy = 15
        self.count_asteroids = 50
        self.spawn_asteroids = 5
        self.screen = screen
        self.run_pause = None
        self.exit = None

    def menu(self):
        self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
            True, False, False, False, False, False
        while self.run_menu:
            self.screen.fill('black')
            self.menu_btn.draw(self.screen)
            flip()
            for e in event.get():
                if e.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
                        False, False, False, False, False, False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        pygame.quit()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        self.menu_btn.update(self)

    def game(self):
        self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
            False, True, False, False, False, False
        info = read_info_ship()
        score, money = game_main.main(FPS, [self.count_asteroids, self.count_enemy, self.spawn_asteroids / 10,
                                            self.spawn_enemy / 10], [info[1], info[2], info[3], info[4], eval(info[5]),
                                                                     eval(info[6])], self)
        self.run_game = False
        add_cell(str(datetime.datetime.today())[:16], score)
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
            self.over_btn.draw(self.screen)
            score_text = pygame.font.SysFont('impact', 100).render(f'{score}', 1, (152, 146, 173))
            self.screen.blit(score_text,
                             score_text.get_rect(center=(SCREEN_WIDTH // 2,
                                                         SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 +
                                                         SCREEN_HEIGHT * 0.08 * 0)))
            flip()
            for e in event.get():
                if e.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
                        False, False, False, False, False, False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.menu()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        self.over_btn.update(self)

    def settings(self):
        self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
            False, False, False, True, False, False
        while self.run_settings:
            self.screen.fill('black')
            self.settings_btn.draw(self.screen)
            # ???????????????????? ????????????
            count_enemy = pygame.font.SysFont('impact', int(SCREEN_HEIGHT * 0.05)).render(f'{self.count_enemy}', 1,
                                                                                          (152, 146, 173))
            self.screen.blit(count_enemy, (
                SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2 + SCREEN_WIDTH * 0.085,
                0 + SCREEN_HEIGHT * 0.15 - SCREEN_HEIGHT * 0.2 * 0))

            text_count_enemy = pygame.font.SysFont('impact', int(SCREEN_HEIGHT * 0.05)).render(f'???????????????????? ????????????', 1,
                                                                                               (152, 146, 173))
            self.screen.blit(text_count_enemy, (
                (SCREEN_WIDTH // 2 + 20 * int(SCREEN_HEIGHT * 0.05) // 2) // 2,
                0 + SCREEN_HEIGHT * 0.15 + SCREEN_HEIGHT * 0.2 * -0.5))

            # ???? ???????????? ????????????
            spawn_enemy = pygame.font.SysFont('impact', int(SCREEN_HEIGHT * 0.05)).render(f'{self.spawn_enemy / 10}', 1,
                                                                                          (152, 146, 173))
            self.screen.blit(spawn_enemy, (
                SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2 + SCREEN_WIDTH * 0.085,
                0 + SCREEN_HEIGHT * 0.15 + SCREEN_HEIGHT * 0.2 * 1))

            text_spawn_enemy = pygame.font.SysFont('impact', int(SCREEN_HEIGHT * 0.05)).render(f'???? ???????????? ????????????', 1,
                                                                                               (152, 146, 173))
            self.screen.blit(text_spawn_enemy, (
                (SCREEN_WIDTH // 2 + 20 * int(SCREEN_HEIGHT * 0.05) // 2) // 2,
                0 + SCREEN_HEIGHT * 0.15 + SCREEN_HEIGHT * 0.2 * 0.5))
            # ???????????????????? ????????????????????
            count_astoroids = pygame.font.SysFont('impact', int(SCREEN_HEIGHT * 0.05)).render(f'{self.count_asteroids}',
                                                                                              1, (152, 146, 173))
            self.screen.blit(count_astoroids, (
                SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2 + SCREEN_WIDTH * 0.085,
                0 + SCREEN_HEIGHT * 0.15 + SCREEN_HEIGHT * 0.2 * 2))
            text_count_enemy = pygame.font.SysFont('impact', int(SCREEN_HEIGHT * 0.05)).render(f'???????????????????? ????????????????????',
                                                                                               1, (152, 146, 173))
            self.screen.blit(text_count_enemy, (
                (SCREEN_WIDTH // 2 + 15 * int(SCREEN_HEIGHT * 0.05) // 2) // 2,
                0 + SCREEN_HEIGHT * 0.15 + SCREEN_HEIGHT * 0.2 * 1.5))
            # ???? ???????????? ????????????????????
            spawn_astoroids = pygame.font.SysFont('impact', int(SCREEN_HEIGHT * 0.05)).render(
                f'{self.spawn_asteroids / 10}', 1, (152, 146, 173))
            self.screen.blit(spawn_astoroids, (
                SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2 + SCREEN_WIDTH * 0.085,
                0 + SCREEN_HEIGHT * 0.15 + SCREEN_HEIGHT * 0.2 * 3))

            text_count_enemy = pygame.font.SysFont('impact', int(SCREEN_HEIGHT * 0.05)).render(f'???? ???????????? ????????????????????',
                                                                                               1, (152, 146, 173))
            self.screen.blit(text_count_enemy, (
                (SCREEN_WIDTH // 2 + 16 * int(SCREEN_HEIGHT * 0.05) // 2) // 2,
                0 + SCREEN_HEIGHT * 0.15 + SCREEN_HEIGHT * 0.2 * 2.5))

            flip()
            for e in event.get():
                if e.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
                        False, False, False, False, False, False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.menu()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        self.settings_btn.update(self)

    def pause_menu(self):
        self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
            False, False, False, False, False, True
        while self.run_congame:
            self.screen.fill('black')
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
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        self.congame_btns.update(self)

    def hight_score(self):
        self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame, self.run_hight_score = \
            False, False, False, False, False, False, True
        while self.run_hight_score:
            self.screen.fill('black')
            self.hight_btn.draw(self.screen)
            hight_score_players = sorted(read_score(), key=lambda x: x[1], reverse=True)[:10]
            for i in range(0, len(hight_score_players)):
                name, score = hight_score_players[i][0], hight_score_players[i][1]
                # Top score
                text = pygame.font.SysFont('arial', 100).render(f'Top score', 1, (152, 146, 173))
                self.screen.blit(text, (int(SCREEN_WIDTH // 1.7 - text.get_width()), 100))
                # number
                text = pygame.font.SysFont('arial', 40).render(f'{(i + 1)}', 1, (152, 146, 173))
                self.screen.blit(text,
                                 (int(SCREEN_WIDTH // 3.0), int(SCREEN_HEIGHT // 4 + SCREEN_HEIGHT * 0.05 * (i + 1))))
                # -
                text = pygame.font.SysFont('arial', 40).render(f'-', 1, (152, 146, 173))
                self.screen.blit(text,
                                 (int(SCREEN_WIDTH // 2.8), int(SCREEN_HEIGHT // 4 + SCREEN_HEIGHT * 0.05 * (i + 1))))
                # name
                text = pygame.font.SysFont('arial', 40).render(f'{name}', 1, (152, 146, 173))
                self.screen.blit(text,
                                 (int(SCREEN_WIDTH // 2.6), int(SCREEN_HEIGHT // 4 + SCREEN_HEIGHT * 0.05 * (i + 1))))
                # score
                text = pygame.font.SysFont('arial', 40).render(f'{score}', 1, (152, 146, 173))
                self.screen.blit(text,
                                 (int(SCREEN_WIDTH - SCREEN_WIDTH // 2.55),
                                  int(SCREEN_HEIGHT // 4 + SCREEN_HEIGHT * 0.05 * (i + 1))))

            flip()
            for e in event.get():
                if e.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame, self.run_hight_score = \
                        False, False, False, False, False, False, False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.menu()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        self.hight_btn.update(self)

    def library(self):
        self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame, self.run_hight_score, self.run_info = \
            False, False, False, False, True, False, False, False

        while self.run_library:
            self.screen.fill('black')
            self.info_btn.draw(self.screen)
            flip()

            for e in event.get():
                if e.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame = \
                        False, False, False, False, False, False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.menu()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        self.info_btn.update(self)

    def info_shatle(self, name, info, png):
        self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame, self.run_hight_score, self.run_info = \
            False, False, False, False, False, False, False, True
        shatle_image = pygame.transform.scale(pygame.image.load(png), (int(SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.09),
                                                                       int(SCREEN_HEIGHT * 0.4)))
        shatle_image_rect = shatle_image.get_rect()
        shatle_image_rect.x, shatle_image_rect.y = 750, 300
        info_image = pygame.transform.scale(pygame.image.load(info),
                                            (int(SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.03), int(SCREEN_HEIGHT * 0.5)))
        info_image_rect = info_image.get_rect()
        info_image_rect.x, info_image_rect.y = 150, 300

        while self.run_info:
            self.screen.fill('black')
            self.screen.blit(shatle_image, shatle_image_rect)
            self.screen.blit(info_image, info_image_rect)
            text = pygame.font.SysFont('arial', 100).render(f'{name}', 1, (152, 146, 173))
            self.screen.blit(text, (int(SCREEN_WIDTH // 1.7 - text.get_width()), 100))
            self.info_shatle_btn.draw(self.screen)
            flip()
            for e in event.get():
                if e.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_over, self.run_settings, self.run_library, self.run_congame, self.run_hight_score, self.run_info = \
                        False, False, False, False, False, False, False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        self.menu()
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        self.info_shatle_btn.update(self)
