import os
import sys

import pygame


def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


classic_ammunition_image = load_image("Standart ammo.png")
piercing_ammunition_image = load_image("Piersing ammo.png")
explosive_ammunition_image = load_image("Explosive ammo.png")
buran_image = pygame.transform.scale(load_image('buran.png'), (100, 100 * 1.5862))
asteroid = load_image('Asteroid.png')


class Ammunition(pygame.sprite.Sprite):
    def __init__(self, pos, speed, damage, sprite, info_id, quarter, corner):
        super().__init__()
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos[0], pos[1]
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = speed
        self.damage = damage
        self.info_id = info_id
        self.quarter = quarter
        self.corner = corner

    def move(self, fps):
        if self.quarter == 1:
            self.rect.x += self.speed * (1 - self.corner) / fps
            self.rect.y -= self.speed * self.corner / fps
        if self.quarter == 2:
            self.rect.x -= self.speed * (1 - self.corner) / fps
            self.rect.y -= self.speed * self.corner / fps
        if self.quarter == 3:
            self.rect.x -= self.speed * (1 - self.corner) / fps
            self.rect.y += self.speed * self.corner / fps
        if self.quarter == 4:
            self.rect.x += self.speed * (1 - self.corner) / fps
            self.rect.y += self.speed * self.corner / fps

    def give_damage(self, body):
        if pygame.sprite.collide_mask(self, body):
            body.get_damage(self.damage)
            self.kill()

    def update(self, fps):
        self.move(fps)
        if self.rect.y < -50:
            self.kill()


class ClassicAmmunition(Ammunition):
    def __init__(self, pos, speed, quarter, corner):
        super().__init__(pos, speed, 3, classic_ammunition_image, 1, quarter, corner)


class Weapon:
    def __init__(self, name, recharge, store_size, rate_of_fire, ammunition_type, info_id, sprite_id):
        self.name = name
        self.recharge = recharge
        self.store_size = store_size
        self.rate_of_fire = rate_of_fire
        self.ammunition_type = ammunition_type
        self.info_id = info_id
        self.sprite_id = sprite_id


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
        self.mask = pygame.mask.from_surface(self.image)
        self.name = name
        self.hp = hp
        self.speed = speed
        self.info_id = info_id
        self.weapon = weapon
        self.armor = armor

    def get_damage(self, damage, f=False):
        if self.armor is not None:
            damage = self.armor.get_damage(damage, f)
        self.hp -= damage
        if self.hp <= 0:
            self.kill()
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

    def update(self, keys, fps):
        if keys[pygame.K_w]:
            self.move('up', fps)
        if keys[pygame.K_s]:
            self.move('down', fps)
        if keys[pygame.K_a]:
            self.move('left', fps)
        if keys[pygame.K_d]:
            self.move('right', fps)


class Buran(SpaceShip):
    def __init__(self, pos):
        super().__init__('Buran', pos, 100, 120, 1, buran_image)


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, pos, speeed, radius, hp):
        super().__init__()
        self.image = asteroid
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos[0], pos[1]
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = speeed
        self.hp = hp

    def move(self, direction, fps):
        if direction == 'left':
            self.rect.x -= self.speed / fps
        if direction == 'right':
            self.rect.x += self.speed / fps
        if direction == 'up':
            self.rect.y -= self.speed / fps
        if direction == 'down':
            self.rect.y += self.speed / fps

    def get_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()

    def update(self, keys, fps):
        self.move('down', fps)



