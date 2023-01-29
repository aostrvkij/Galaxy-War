from library.config import FPS, MENU_BTN, SETTING_BTN, LIBRARY_BTN
from library.config import SCREEN_WIDTH, SCREEN_HEIGHT
from pygame.display import flip
from pygame.key import get_pressed
from pygame import event
from pygame import transform
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


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, name, pos, hp, speed, info_id, sprite_id, color,
                 weapon=None, armor=None):
        super().__init__()
        self.image = transform.scale(pygame.image.load('Images/buran.png'), (100, 200))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos[0], pos[1]
        self.mask = pygame.mask.from_surface(self.image)
        self.name = name
        self.hp = hp
        self.hp_none = pygame.transform.scale(pygame.image.load('Images/hp_none.png'), (SCREEN_WIDTH * 0.02, SCREEN_WIDTH * 0.02))
        self.hp_half = pygame.image.load('Images/hp_half.png')
        self.hp_full = pygame.image.load('Images/hp_full.png')
        self.speed = speed
        self.info_id = info_id
        self.sprite_id = sprite_id
        self.weapon = weapon
        self.armor = armor

    def get_damage(self, damage, f=False):
        if self.armor is not None:
            damage = self.armor.get_damage(damage, f)
        self.hp -= damage
        if self.hp <= 0:
            return False
        return True

    def move(self, direction, fps):
        if direction == 'left':
            self.rect.x -= self.speed / fps
        if direction == 'right':
            self.rect.x += self.speed / fps
        if direction == 'up':
            self.rect.y -= self.speed / fps
        if direction == 'down':
            self.rect.y += self.speed / fps

    def equip_gun(self, weapon):
        self.weapon = weapon

    def equip_armour(self, armour):
        self.armor = armour

    def draw_hp(self, screen):
        hp_rect = self.hp_none.get_rect()
        hp_rect.width, hp_rect.height = SCREEN_WIDTH * 0.025, SCREEN_WIDTH * 0.025
        hp_rect.x, hp_rect.y = SCREEN_WIDTH // 100 * 0.05, SCREEN_HEIGHT - SCREEN_WIDTH // 100 * 0.05 - hp_rect.height
        pygame.draw.rect(screen, (65, 65, 65), ((SCREEN_WIDTH * 0.03, SCREEN_HEIGHT * 0.96),
                                                (SCREEN_WIDTH * 0.2, SCREEN_HEIGHT * 0.03)))
        pygame.draw.rect(screen, (255, 0, 0), ((SCREEN_WIDTH * 0.03, SCREEN_HEIGHT * 0.96),
                                         (SCREEN_WIDTH * 0.2 / 100 * self.hp, SCREEN_HEIGHT * 0.03)))
        if self.hp < 30:
            hp_image = pygame.transform.scale(self.hp_none, (hp_rect.width, hp_rect.height))
            screen.blit(hp_image, hp_rect)
        elif 30 <= self.hp < 70:
            hp_image = pygame.transform.scale(self.hp_half, (hp_rect.width, hp_rect.height))
            screen.blit(hp_image, hp_rect)
        elif 70 <= self.hp:
            hp_image = pygame.transform.scale(self.hp_full, (hp_rect.width, hp_rect.height))
            screen.blit(hp_image, hp_rect)

    def update(self, keys, fps, group, screen):
        if pygame.sprite.spritecollide(self, group, False):
            for i in pygame.sprite.spritecollide(self, group, True):
                self.get_damage(i.damage)
        if keys[pygame.K_w]:
            self.move('up', fps)
        if keys[pygame.K_s]:
            self.move('down', fps)
        if keys[pygame.K_a]:
            self.move('left', fps)
        if keys[pygame.K_d]:
            self.move('right', fps)
        if keys[pygame.K_c]:
            self.hp -= 1
        self.draw_hp(screen)


class Game:
    def __init__(self, screen):
        self.run_menu, self.run_game, self.run_settings, self.run_library = True, False, False, False

        self.menu_btn = MENU_BTN
        self.settings_btn = SETTING_BTN
        self.libr_btns = LIBRARY_BTN
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.shells = pygame.sprite.Group()
        self.ships = pygame.sprite.Group()
        self.ship = SpaceShip('buran', [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2], 100, 300, 1, 1, 'green')
        self.ships.add(self.ship)

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
            self.ships.update(keys, FPS, self.shells, self.screen)
            bullets.update()
            bullets.draw(self.screen)
            self.shells.draw(self.screen)
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