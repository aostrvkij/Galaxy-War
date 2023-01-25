from library.config import FPS, MENU_BTN, SETTING_BTN, LIBRARY_BTN
from library.config import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame.display import flip
from pygame.key import get_pressed
from pygame import event
import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, move=None):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 20
        self.width, self.height = 2, 10
        self.move = move
        self.move_x = 0
        self.image = pygame.Surface((3, 10))
        self.image.fill('yellow')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y
        self.x, self.y = self.rect.x, self.rect.y

    def update(self):
        if self.move:
            self.move_x += 0.05
            if self.move == 'left':
                self.x -= int(self.move_x) / FPS
                self.y -= self.speed / FPS
            if self.move == 'right':
                self.x += int(self.move_x) / FPS
                self.y -= self.speed / FPS
        else:
            self.y -= self.speed / FPS
        self.rect.x, self.rect.y = self.x, self.y
        if SCREEN_HEIGHT < self.rect.y < 0:
            self.kill()


bullets = pygame.sprite.Group()


class Ship(pygame.sprite.Sprite):
    def __init__(self, pos, speed, number, damage, type_ship, sprite_id, info_id):
        super().__init__()
        self.speed = speed
        self.number = number
        self.damage = damage
        self.bullet_delay = 10
        self.type = type_ship
        self.sprite_id = sprite_id
        self.info_id = info_id
        self.image = pygame.Surface((30, 30))
        self.image.fill('red')
        self.x, self.y = 100, 100
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y

    def update(self, keys):
        if keys[pygame.K_w]:
            if self.rect.y - self.speed > 0:
                self.y -= self.speed / FPS
            else:
                self.rect.y = 0
        if keys[pygame.K_s]:
            if self.rect.y + self.speed < SCREEN_HEIGHT - self.rect.height:
                self.y += self.speed / FPS
            else:
                self.rect.y = SCREEN_HEIGHT - self.rect.height
        if keys[pygame.K_a]:
            if self.rect.x - self.speed > 0:
                self.x -= self.speed / FPS
            else:
                self.rect.x = 0
        if keys[pygame.K_d]:
            if self.rect.x + self.speed < SCREEN_WIDTH - self.rect.width:
                self.x += self.speed / FPS
            else:
                self.rect.x = SCREEN_WIDTH - self.rect.width
        if keys[pygame.K_SPACE]:
            self.attack(keys)
        self.rect.x, self.rect.y = self.x, self.y

    def attack(self, keys):
        if self.bullet_delay >= 10:
            if keys[pygame.K_a] and keys[pygame.K_d] or not(keys[pygame.K_a] and keys[pygame.K_d]):
                bullets.add(Bullet(self.rect.x, self.rect.top))
            else:
                if keys[pygame.K_a]:
                    bullets.add(Bullet(self.rect.x, self.rect.top, 'left'))
                if keys[pygame.K_d]:
                    bullets.add(Bullet(self.rect.x, self.rect.top, 'right'))
            self.bullet_delay = 0
        elif self.bullet_delay < 10:
            self.bullet_delay += 10 / FPS


class Game:
    def __init__(self, screen):
        self.run_menu, self.run_game, self.run_settings, self.run_library = True, False, False, False

        self.menu_btn = MENU_BTN
        self.settings_btn = SETTING_BTN
        self.libr_btns = LIBRARY_BTN
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.ships = pygame.sprite.Group()
        self.ships.add(Ship((100, 100), 10, 1, 1, 1, 1, 1))

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
            bullets.update()
            bullets.draw(self.screen)
            self.ships.draw(self.screen)
            flip()
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
