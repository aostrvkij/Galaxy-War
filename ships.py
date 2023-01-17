import pygame


class Ammunition:
    def __init__(self, pos, type, speed, damage, number, sprite_id, info_id):
        self.pos = pos
        self.type = type
        self.speed = speed
        self.damage = damage
        self.number = number
        self.sprite_id = sprite_id
        self.info_id = info_id

    def move(self, quarter, k, fps):
        if quarter == 1:
            self.pos[0] += self.speed * (1 - k) / fps
            self.pos[1] -= self.speed * k / fps
        if quarter == 2:
            self.pos[0] -= self.speed * (1 - k) / fps
            self.pos[1] -= self.speed * k / fps
        if quarter == 3:
            self.pos[0] -= self.speed * (1 - k) / fps
            self.pos[1] += self.speed * k / fps
        if quarter == 4:
            self.pos[0] += self.speed * (1 - k) / fps
            self.pos[1] += self.speed * k / fps

    def draw(self, screen, side):
        if side > 0:
            color = pygame.color.Color('yellow')
        else:
            color = pygame.color.Color('blue')
        pygame.draw.circle(screen, color, self.pos, 2)


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


class SpaceShip:
    def __init__(self, name, pos, hp, speed, info_id, sprite_id, side,
                 weapon=None, armor=None):
        self.name = name
        self.pos = pos
        self.hp = hp
        self.speed = speed
        self.info_id = info_id
        self.sprite_id = sprite_id
        self.side = side
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
            self.pos[0] -= self.speed / fps
        if direction == 'right':
            self.pos[0] += self.speed / fps
        if direction == 'up':
            self.pos[1] -= self.speed / fps
        if direction == 'down':
            self.pos[1] += self.speed / fps

    def equip_gun(self, weapon):
        self.weapon = weapon

    def equip_armour(self, armour):
        self.armor = armour

    def draw(self, screen):
        if self.side > 0:
            color = pygame.color.Color('green')
        else:
            color = pygame.color.Color('red')
        pygame.draw.rect(screen, color, (self.pos, (25, 25)))

    def update(self, keys, screen, fps):
        if keys[pygame.K_w]:
            self.move('up', fps)
        if keys[pygame.K_s]:
            self.move('down', fps)
        if keys[pygame.K_a]:
            self.move('left', fps)
        if keys[pygame.K_d]:
            self.move('right', fps)
        self.draw(screen)


# drow = Armour('drow', 1, 10, 1)
# shatl = SpaceShip('baron', [0, 0], 100, 30, 1, 1, 1)
# shatl.equip_armour(drow)
# print(shatl.get_damage(110))
# print(shatl.hp)

