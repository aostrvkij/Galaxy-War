from library.config import FPS, MENU_BTN, SETTING_BTN, LIBRARY_BTN
from pygame.display import flip
from pygame.key import get_pressed
from pygame import event
import pygame


class Ship(pygame.sprite.Sprite):
    def __init__(self, pos, speed, number, damage, type, sprite_id, info_id):
        super().__init__()
        self.speed = speed
        self.number = number
        self.damage = damage
        self.type = type
        self.sprite_id = sprite_id
        self.info_id = info_id
        self.image = pygame.Surface((30, 30))
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = pos[0], pos[1]

    def update(self, keys):
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_SPACE]:
            self.attack()

    def attack(self):
        pass


class Game:
    def __init__(self, screen, size, screen_width, screen_height):
        self.run_menu, self.run_game, self.run_settings, self.run_library = True, False, False, False

        self.menu_btn = MENU_BTN
        self.settings_btn = SETTING_BTN
        self.libr_btns = LIBRARY_BTN
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.ships = pygame.sprite.Group()
        self.ships.add(Ship((100, 100), 4, 1, 1, 1, 1, 1))

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
        self.run_menu, self.run_game, self.run_settings, self.run_library = False, True, False, False
        while self.run_game:
            self.screen.fill('black')
            keys = get_pressed()
            self.ships.update(keys)
            self.ships.draw(self.screen)
            flip()
            self.clock.tick(60)
            if keys[pygame.K_ESCAPE]:
                self.run_game = False
                quit()
            for e in event.get():
                if e.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_settings, self.run_library = False, False, False, False

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
