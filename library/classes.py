import os
import sys
from time import time

import pygame

import library


def load_image(name):
    fullname = os.path.join('Images', 'data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


classic_ammunition_image = load_image("Standart ammo.png")
piercing_ammunition_image = load_image("Piersing ammo.png")
explosive_ammunition_image = load_image("Explosive ammo.png")
buran_images = [[pygame.transform.scale(load_image('buran.png'), (50, 79)),
                 pygame.transform.scale(load_image('buran right.png'), (50, 79)),
                 pygame.transform.scale(load_image('buran left.png'), (50, 79))],
                [pygame.transform.scale(load_image('buran forward.png'), (50, 79)),
                 pygame.transform.scale(load_image('buran right forward.png'), (50, 79)),
                 pygame.transform.scale(load_image('buran left forward.png'), (50, 79))]]
titan34D = pygame.transform.scale(load_image('titan 34D.png'), (100, 152))
asteroid = load_image('Asteroid.png')
asteroid_iron = load_image('Asteroid_Iron.png')
asteroid_gold = load_image('Asteroid_Gold.png')
hp_none = load_image('hp_none.png')
hp_half = load_image('hp_half.png')
hp_full = load_image('hp_full.png')
boom = load_image('boom.png')


class Ammunition(pygame.sprite.Sprite):
    def __init__(self, pos, speed, damage, sprite, info_id, quarter, corner, owner):
        super().__init__()
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos[0], pos[1]
        self.x, self.y = pos[0], pos[1]
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = speed
        self.damage = damage
        self.info_id = info_id
        self.quarter = quarter
        self.corner = corner
        self.owner = owner

    def move(self, fps):
        if self.quarter == 1:
            self.x += self.speed * (1 - self.corner) / fps
            self.y -= self.speed * self.corner / fps
            self.rect.x = self.x
            self.rect.y = self.y
        if self.quarter == 2:
            self.x -= self.speed * (1 - self.corner) / fps
            self.y -= self.speed * self.corner / fps
            self.rect.x = self.x
            self.rect.y = self.y
        if self.quarter == 3:
            self.x -= self.speed * (1 - self.corner) / fps
            self.y += self.speed * self.corner / fps
            self.rect.x = self.x
            self.rect.y = self.y
        if self.quarter == 4:
            self.x += self.speed * (1 - self.corner) / fps
            self.y += self.speed * self.corner / fps
            self.rect.x = self.x
            self.rect.y = self.y

    def give_damage(self, body):
        if pygame.sprite.collide_mask(self, body):
            if (type(body) == library.classes.AsteroidIron or type(body) == library.classes.AsteroidGold) \
                    and type(self.owner) == library.classes.Buran:
                self.owner.money += body.price
            body.get_damage(self.damage)
            self.kill()

    def update(self, fps):
        self.move(fps)
        if self.rect.y < -50:
            self.kill()


class ClassicAmmunition(Ammunition):
    def __init__(self, pos, speed, quarter, corner, owner):
        super().__init__(pos, speed, 3, classic_ammunition_image, 1, quarter, corner, owner)


class PiercingAmmunition(Ammunition):
    def __init__(self, pos, speed, quarter, corner, owner, k):
        super().__init__(pos, speed * 1.25, 5, piercing_ammunition_image, 1, quarter, corner, owner)
        self.ratio = k

    def give_damage(self, body):
        if pygame.sprite.collide_mask(self, body):
            if (type(body) == library.classes.AsteroidIron or type(body) == library.classes.AsteroidGold) \
                    and type(self.owner) == library.classes.Buran:
                self.owner.money += body.price
            body.get_damage(self.damage)
            self.ratio -= 1
            if self.ratio <= 0:
                self.kill()


class ExplosiveAmmunition(Ammunition):
    def __init__(self, pos, speed, quarter, corner, owner, radios):
        super().__init__(pos, speed * 0.75, 10, explosive_ammunition_image, 1, quarter, corner, owner)
        self.radios = radios
        self.start = 0

    def give_damage(self, body):
        if pygame.sprite.collide_mask(self, body):
            if (type(body) == library.classes.AsteroidIron or type(body) == library.classes.AsteroidGold) \
                    and type(self.owner) == library.classes.Buran:
                self.owner.money += body.price
            f = body.speed
            body.get_damage(self.damage)

            if str(self.image) != str(pygame.transform.scale(boom, (self.radios * 2, self.radios * 2))):
                self.quarter = 3
                self.speed = f
                self.start = time()
                self.damage = 3
                self.image = pygame.transform.scale(boom, (self.radios * 2, self.radios * 2))
                self.rect = self.image.get_rect()
                self.x, self.y = body.x + (body.rect.width // 2) - (self.rect.width // 2), \
                                 body.y + (body.rect.height // 2) - (self.rect.width // 2)
                self.rect.x, self.rect.y = self.x, self.y
                self.mask = pygame.mask.from_surface(self.image)

    def update(self, fps):
        self.move(fps)
        if self.rect.y < -self.rect.height - 10:
            self.kill()
        if time() - self.start >= 1 and self.start != 0:
            self.kill()
            self.start = 0


class Weapon:
    def __init__(self, name, recharge, store_size, rate_of_fire, ammunition_type, info_id):
        self.name = name
        self.recharge = recharge
        self.store_size = store_size
        self.rate_of_fire = rate_of_fire
        self.ammunition_type = ammunition_type
        self.info_id = info_id


class Armour:
    def __init__(self, name, armour_type, number, info_id):
        self.name = name
        self.armour_type = armour_type
        self.k = number
        self.info_id = info_id

    def get_damage(self, damage, f=False):
        if self.armour_type == 1:
            self.k -= damage
            if self.k < 0:
                return self.k * -1
            return 0

        elif self.armour_type == 2:
            return damage * (1 - self.k)

        elif self.armour_type == 3:
            if f:
                return 0


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, name, pos, hp, speed, info_id, sprite,
                 weapon=None, armor=None):
        super().__init__()
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos[0], pos[1]
        self.x, self.y = pos[0], pos[1]
        self.mask = pygame.mask.from_surface(self.image)
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.speed = speed
        self.info_id = info_id
        self.weapon = weapon
        self.armor = armor
        self.start = 0

    def get_damage(self, damage, f=False):
        if self.armor is not None:
            damage = self.armor.get_damage(damage, f)
        self.hp -= damage
        if self.hp <= 0:
            self.start = time()
            self.image = pygame.transform.scale(boom, (self.rect.width, self.rect.width))
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = self.x, self.y
            self.mask = pygame.mask.from_surface(self.image)

    def draw_hp(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.rect.x, self.rect.y - self.rect.height * 0.15,
                                               self.rect.width / self.max_hp * self.hp, self.rect.height * 0.1))

    def give_damage(self, body):
        if pygame.sprite.collide_mask(self, body) and self.hp > 0 and body.hp > 0:
            damage = body.hp
            body.get_damage(self.hp)
            self.get_damage(damage)
        elif pygame.sprite.collide_mask(self, body) and body.hp > 0:
            body.get_damage(5)

    def move(self, direction, fps):
        if direction == 'left':
            self.x -= self.speed / fps
            self.rect.x = self.x
        if direction == 'right':
            self.x += self.speed / fps
            self.rect.x = self.x
        if direction == 'up':
            self.y -= self.speed / fps
            self.rect.y = self.y
        if direction == 'down':
            self.y += self.speed / fps
            self.rect.y = self.y

    def equip_gun(self, weapon):
        self.weapon = weapon

    def equip_armour(self, armour):
        self.armor = armour

    def update(self, keys, fps, size, screen):
        pass


class Buran(SpaceShip):
    def __init__(self, pos, hp, speed, money, score, weapon, armour):
        super().__init__('Buran', pos, hp, speed, 1, buran_images[0][0], weapon=weapon, armor=armour)
        self.money = money
        self.score = score
        self.forward = 0
        self.side = 0

    def draw_hp(self, screen, size):
        hp_rect = pygame.transform.scale(hp_none, (int(size[0] * 0.025), int(size[0] * 0.025))).get_rect()
        hp_rect.width, hp_rect.height = int(size[0] * 0.025), int(size[0] * 0.025)
        hp_rect.x, hp_rect.y = int(size[0] // 100 * 0.05), int(size[1] - size[0] // 100 * 0.05 - hp_rect.height)
        pygame.draw.rect(screen, (65, 65, 65), ((int(size[0] * 0.03), int(size[1] * 0.96)),
                                                (int(size[0] * 0.2), int(size[1] * 0.03))))
        pygame.draw.rect(screen, (255, 0, 0), ((int(size[0] * 0.03), int(size[1] * 0.96)),
                                               (int(size[0] * 0.2 * self.hp / self.max_hp), int(size[1] * 0.03))))
        if self.hp < 25:
            hp_image = pygame.transform.scale(hp_none, (hp_rect.width, hp_rect.height))
            screen.blit(hp_image, hp_rect)
        elif 25 <= self.hp < 75:
            hp_image = pygame.transform.scale(hp_half, (hp_rect.width, hp_rect.height))
            screen.blit(hp_image, hp_rect)
        elif 75 <= self.hp:
            hp_image = pygame.transform.scale(hp_full, (hp_rect.width, hp_rect.height))
            screen.blit(hp_image, hp_rect)

    def give_damage(self, body):
        if pygame.sprite.collide_mask(self, body) and self.hp > 0 and body.hp > 0:
            damage = body.hp
            if (type(body) == library.classes.AsteroidIron
                    or type(body) == library.classes.AsteroidGold):
                self.money += body.price * body.hp
            body.get_damage(self.hp)
            self.get_damage(damage)

    def update(self, keys, fps, size, screen):
        if bool(list(filter(lambda x: x != 0, keys))):
            if keys[pygame.K_w] and self.rect.y > 0:
                self.move('up', fps)
                self.forward = 1
                self.side = 0

            elif keys[pygame.K_s] and self.rect.y + self.rect.height < size[1] * 0.96 - 10:
                self.move('down', fps)
                self.forward = 0
                self.side = 0

            else:
                self.forward = 0

            if keys[pygame.K_a] and self.rect.x > 0:
                self.move('left', fps)
                self.side = 2

            if keys[pygame.K_d] and self.rect.x + self.rect.width < size[0]:
                self.move('right', fps)
                self.side = 1

            if keys[pygame.K_d] and keys[pygame.K_a]:
                self.side = 0

        else:
            self.forward = 0
            self.side = 0

        self.image = buran_images[self.forward][self.side]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y
        self.mask = pygame.mask.from_surface(self.image)

        self.draw_hp(screen, size)


class Titan34D(SpaceShip):
    def __init__(self, pos):
        super().__init__('Titan 34D', pos, 75, 200, 1, titan34D, armor=Armour('titanium plating', 2, 0.85, 1))

    def update(self, keys, fps, size, screen):
        self.move('down', fps)
        self.draw_hp(screen)
        if time() - self.start >= 1 and self.start != 0:
            self.kill()
            self.start = 0


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, pos, speeed, radius):
        super().__init__()
        self.image = pygame.transform.scale(asteroid, (2 * radius, 2 * radius))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = pos[0], pos[1]
        self.x, self.y = pos[0], pos[1]
        self.speed = speeed
        self.hp = radius

    def move(self, direction, fps):
        if direction == 'left':
            self.x -= self.speed / fps
            self.rect.x = self.x
        if direction == 'right':
            self.x += self.speed / fps
            self.rect.x = self.x
        if direction == 'up':
            self.y -= self.speed / fps
            self.rect.y = self.y
        if direction == 'down':
            self.y += self.speed / fps
            self.rect.y = self.y

    def get_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()
        if self.hp >= 10:
            self.x, self.y = self.rect.x + ((self.rect.width - 2 * self.hp) // 2), \
                             self.rect.y + ((self.rect.width - 2 * self.hp) // 2)
            self.image = pygame.transform.scale(self.image, (2 * int(self.hp), 2 * int(self.hp)))
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.x, self.rect.y = self.x, self.y
        else:
            self.x, self.y = self.rect.x + ((self.rect.width - 2 * 10) // 2), \
                             self.rect.y + ((self.rect.width - 2 * 10) // 2)
            self.image = pygame.transform.scale(self.image, (2 * 10, 2 * 10))
            self.rect = self.image.get_rect()
            self.mask = pygame.mask.from_surface(self.image)
            self.rect.x, self.rect.y = self.x, self.y

    def give_damage(self, body):
        if pygame.sprite.collide_mask(self, body) and self.hp > 0 and body.hp > 0 \
                and not (type(body) is library.classes.ClassicAmmunition
                         or type(body) is library.classes.PiercingAmmunition
                         or type(body) is library.classes.ExplosiveAmmunition):
            damage = body.hp
            body.get_damage(self.hp)
            self.get_damage(damage)

    def update(self, keys, fps, size, screen):
        self.move('down', fps)


class AsteroidIron(Asteroid):
    def __init__(self, pos, speeed, radius):
        super().__init__(pos, speeed, radius)
        self.image = pygame.transform.scale(asteroid_iron, (2 * radius, 2 * radius))
        self.price = 1


class AsteroidGold(Asteroid):
    def __init__(self, pos, speeed, radius):
        super().__init__(pos, speeed, radius)
        self.image = pygame.transform.scale(asteroid_gold, (2 * radius, 2 * radius))
        self.price = 10
