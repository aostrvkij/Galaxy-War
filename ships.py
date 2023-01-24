import pygame


class Ammunition(pygame.sprite.Sprite):
    def __init__(self, pos, type_ammunition, speed, damage, number, sprite_id, info_id, quarter, corner):
        super().__init__()
        self.image = pygame.Surface((3, 3))
        self.image.fill('yellow')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos[0], pos[1]
        self.mask = pygame.mask.from_surface(self.image)
        self.type = type_ammunition
        self.speed = speed
        self.damage = damage
        self.number = number
        self.sprite_id = sprite_id
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
    def __init__(self, name, pos, hp, speed, info_id, sprite_id, color,
                 weapon=None, armor=None):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos[0], pos[1]
        self.mask = pygame.mask.from_surface(self.image)
        self.name = name
        self.hp = hp
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

    def update(self, keys, fps, group):
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


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, pos, speeed, radius, hp):
        super().__init__()
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("grey"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(pos[0], pos[1], 2 * radius, 2 * radius)
        self.rect.x, self.rect.y = pos[0], pos[1]
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

    def update(self, group):
        if pygame.sprite.spritecollide(self, group, False):
            for i in pygame.sprite.spritecollide(self, group, True):
                self.get_damage(i.damage)
