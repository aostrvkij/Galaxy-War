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


classic_ammunition_image = pygame.transform.scale(load_image("Standart ammo.png"), (2, 5))
piercing_ammunition_image = pygame.transform.scale(load_image("Piersing ammo.png"), (2, 5))
explosive_ammunition_image = pygame.transform.scale(load_image("Explosive ammo.png"), (2, 5))
buran_images = [[[pygame.transform.scale(load_image('buran.png'), (50, 79)),
                  pygame.transform.scale(load_image('buran right.png'), (50, 79)),
                  pygame.transform.scale(load_image('buran left.png'), (50, 79))],
                 [pygame.transform.scale(load_image('buran forward.png'), (50, 79)),
                  pygame.transform.scale(load_image('buran right forward.png'), (50, 79)),
                  pygame.transform.scale(load_image('buran left forward.png'), (50, 79))]],
                [[pygame.transform.scale(load_image('buran gun1.png'), (50, 79)),
                  pygame.transform.scale(load_image('buran right gun1.png'), (50, 79)),
                  pygame.transform.scale(load_image('buran left gun1.png'), (50, 79))],
                 [pygame.transform.scale(load_image('buran forward gun1.png'), (50, 79)),
                  pygame.transform.scale(load_image('buran right forward gun1.png'), (50, 79)),
                  pygame.transform.scale(load_image('buran left forward gun1.png'), (50, 79))]]
                ]
space_shuttle = [pygame.transform.scale(load_image('space shuttle.png'), (50, 79)),
                 pygame.transform.scale(load_image('space shuttle right.png'), (50, 79)),
                 pygame.transform.scale(load_image('space shuttle left.png'), (50, 79))]
dream_chaser = pygame.transform.scale(load_image('dream chaser.png'), (70, 104))
titan34D = pygame.transform.scale(load_image('titan 34D.png'), (100, 152))
asteroid = load_image('Asteroid.png')
asteroid_iron = load_image('Asteroid_Iron.png')
asteroid_gold = load_image('Asteroid_Gold.png')
hp_none = load_image('hp_none.png')
hp_half = load_image('hp_half.png')
hp_full = load_image('hp_full.png')
boom = load_image('boom.png')



class Ammunition(pygame.sprite.Sprite):
    def __init__(self, pos, speed, damage, sprite, quarter, corner, owner):
        super().__init__()
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos[0], pos[1]
        self.x, self.y = pos[0], pos[1]
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = speed
        self.damage = damage
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
            if (type(body) is library.classes.AsteroidIron or type(body) is library.classes.AsteroidGold) \
                    and type(self.owner) is library.classes.Buran:
                self.owner.money += body.price
            body.get_damage(self.damage)
            self.kill()

    def update(self, fps):
        self.move(fps)
        if self.rect.y < -50:
            self.kill()


class ClassicAmmunition(Ammunition):
    def __init__(self, pos, speed, quarter, corner, owner):
        super().__init__(pos, speed, 3, classic_ammunition_image, quarter, corner, owner)


class PiercingAmmunition(Ammunition):
    def __init__(self, pos, speed, quarter, corner, owner, k):
        super().__init__(pos, speed * 1.25, 5, piercing_ammunition_image, quarter, corner, owner)
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
        super().__init__(pos, speed * 0.75, 10, explosive_ammunition_image, quarter, corner, owner)
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
    def __init__(self, name, recharge, store_size, rate_of_fire, ammunition_type, pos, sprite_id, baf_speed,
                 ammunition_cof):
        self.name = name
        self.recharge = recharge
        self.store_size = store_size
        self.rate_of_fire = rate_of_fire
        self.ammunition_type = ammunition_type
        self.ammunition_cof = ammunition_cof
        self.pos = pos
        self.sprite_id = sprite_id
        self.baf_speed = baf_speed
        self.star_fire = time()

    def fire(self, group, ship, quarter):
        if time() - self.star_fire >= self.rate_of_fire:
            self.star_fire = time()
            if quarter == 1:
                if self.ammunition_type == 2:
                    group.add(PiercingAmmunition((ship.rect.x + self.pos[0], ship.rect.y - self.pos[1]),
                                                 500 * self.baf_speed, quarter, 1, ship, self.ammunition_cof))

                elif self.ammunition_type == 3:
                    group.add(ExplosiveAmmunition((ship.rect.x + self.pos[0], ship.rect.y - self.pos[1]),
                                                  500 * self.baf_speed, quarter, 1, ship, self.ammunition_cof))
            if quarter == 4:
                if self.ammunition_type == 2:
                    group.add(PiercingAmmunition((ship.rect.x + self.pos[0], ship.rect.y + self.pos[1] + ship.rect.height),
                                                 500 * self.baf_speed, quarter, 1, ship, self.ammunition_cof))

                elif self.ammunition_type == 3:
                    group.add(ExplosiveAmmunition((ship.rect.x + self.pos[0], ship.rect.y + self.pos[1] + ship.rect.height),
                                                  500 * self.baf_speed, quarter, 1, ship, self.ammunition_cof))


class MachineGun(Weapon):
    def __init__(self):
        super().__init__('пулемёт', 3, 100, 0.05, 1, [35, 6], 1, 1.1, 0)
        self.pos2 = [15, 6]
        self.sound = pygame.mixer.Sound('Images/data/fire_sound_1.wav')
        self.sound.set_volume(0.05)
        self.chanel = self.sound.play(loops=-1)
        self.chanel.pause()

    def fire(self, group, ship, quarter):
        if time() - self.star_fire >= self.rate_of_fire:
            self.star_fire = time()

            if self.ammunition_type == 1:
                if quarter == 1:
                    group.add(ClassicAmmunition((ship.rect.x + self.pos[0], ship.rect.y - self.pos[1]),
                                                500 * self.baf_speed, quarter, 1, ship))
                    group.add(ClassicAmmunition((ship.rect.x + self.pos2[0], ship.rect.y - self.pos[1]),
                                                500 * self.baf_speed, quarter, 1, ship))
                if quarter == 4:
                    group.add(ClassicAmmunition((ship.rect.x + self.pos[0], ship.rect.y + ship.rect.height + self.pos[1]),
                                                500 * self.baf_speed, quarter, 1, ship))
                    group.add(ClassicAmmunition((ship.rect.x + self.pos2[0], ship.rect.y + ship.rect.height + self.pos[1]),
                                                500 * self.baf_speed, quarter, 1, ship))


class PiercingRifle(Weapon):
    def __init__(self):
        super().__init__('бронебойная винтовка', 5, 50, 0.25, 2, [35, 6], 2, 1.5, 5)
        self.sound = pygame.mixer.Sound('Images/data/fire_sound_2.wav')
        self.sound.set_volume(0.08)
        self.chanel = self.sound.play(loops=-1)
        self.chanel.pause()


class Armour:
    def __init__(self, name, armour_type, number, owner):
        self.name = name
        self.armour_type = armour_type
        self.k = number
        self.owner = owner
        self.max_k = number

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

    def draw_ammo(self, screen):
        pygame.draw.rect(screen, (155, 155, 155), (self.owner.rect.x, self.owner.rect.y - self.owner.rect.height * 0.30,
                                                   self.owner.rect.width / self.max_k * self.k,
                                                   self.owner.rect.height * 0.1))


class SpaceShip(pygame.sprite.Sprite):
    def __init__(self, name, pos, hp, speed, sprite,
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
        self.weapon = weapon
        self.armor = armor
        self.start = 0
        self.gun_id = 0

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

    def death(self):
        try:
            self.weapon.chanel.stop()
        except AttributeError:
            pass

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
        self.gun_id = weapon.sprite_id

    def equip_armour(self, armour):
        self.armor = armour

    def update(self, keys, fps, size, screen, body):
        pass


class Buran(SpaceShip):
    def __init__(self, pos, hp, speed, money, score, weapon, armour):
        super().__init__('Buran', pos, hp, speed, buran_images[0][0][0],
                         weapon=weapon, armor=armour)
        self.money = money
        self.score = score
        self.forward = 0
        self.side = 0
        if weapon is None:
            self.gun_id = 0
        else:
            self.gun_id = weapon.sprite_id

    def draw_info(self, screen, size):
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

    def update(self, keys, fps, size, screen, body, shells):
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

        if not (keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_s] or keys[pygame.K_d]):
            self.forward = 0
            self.side = 0

        self.image = buran_images[self.gun_id][self.forward][self.side]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y
        self.mask = pygame.mask.from_surface(self.image)
        if self.weapon is not None:
            if keys[pygame.K_SPACE]:
                try:
                    self.weapon.chanel.unpause()
                except AttributeError:
                    pass
                self.weapon.fire(shells, self, 1)
            else:
                try:
                    self.weapon.chanel.pause()
                except AttributeError:
                    pass
        self.draw_info(screen, size)


class SpaceShuttle(SpaceShip):
    def __init__(self, pos):
        super().__init__('Space Shuttle', pos, 150, 150, space_shuttle[0],
                         weapon=MachineGun(), armor=Armour('steel plate', 1, 100, self))
        self.time_update = time()
        self.side = 0

    def update(self, keys, fps, size, screen, body, shells):
        if self.y < 100:
            self.move('down', fps)
        if self.hp > 0:
            self.draw_hp(screen)
            self.armor.draw_ammo(screen)
            if 0 <= (time() - self.time_update) <= 5:
                if body.x - body.rect.width // 3 <= self.x <= body.x:
                    try:
                        self.weapon.chanel.unpause()
                    except AttributeError:
                        pass
                    self.weapon.fire(group=shells, ship=self, quarter=4)
                    self.side = 0
                else:
                    try:
                        self.weapon.chanel.pause()
                    except AttributeError:
                        pass
                    if body.x > self.x and self.hp > 0:
                        self.move('right', fps)
                        self.side = 1
                    elif body.x < self.x and self.hp > 0:
                        self.move('left', fps)
                        self.side = 2
                    else:
                        self.side = 0
            elif 5 <= (time() - self.time_update) <= 8:
                try:
                    self.weapon.chanel.unpause()
                except AttributeError:
                    pass
                self.weapon.fire(group=shells, ship=self, quarter=4)
                self.side = 0
            elif (time() - self.time_update) >= 8:
                try:
                    self.weapon.chanel.pause()
                except AttributeError:
                    pass
                self.time_update = time()

            self.image = space_shuttle[self.side]
            self.rect = self.image.get_rect()
            self.rect.x, self.rect.y = self.x, self.y
            self.mask = pygame.mask.from_surface(self.image)

        else:
            try:
                self.weapon.chanel.pause()
            except AttributeError:
                pass

        if self.armor.k <= 0:
            self.move('down', fps)

        if time() - self.start >= 1 and self.start != 0:
            self.kill()
            self.start = 0


class DreamChaser(SpaceShip):
    def __init__(self, pos):
        super().__init__('Dream Chaser', pos, 300, 225, dream_chaser,
                         weapon=PiercingRifle(), armor=Armour('steel plate', 2, 0.5, self))
        self.time_update = time()
        self.side = 1

    def update(self, keys, fps, size, screen, body, shells):
        # self.move('down', fps)
        self.draw_hp(screen)
        if self.hp >= self.max_hp * 0.75:
            if self.y < 100:
                self.move('down', fps)
            if self.x + self.rect.width + 10 >= size[0]:
                self.side = 2
            if self.x - 10 <= 0:
                self.side = 1
            if self.x < size[0] and self.side == 1:
                self.move('right', fps)
            if self.x > 0 and self.side == 2:
                self.move('left', fps)
            try:
                self.weapon.chanel.unpause()
            except AttributeError:
                pass
            self.weapon.fire(group=shells, ship=self, quarter=4)
        elif self.max_hp * 0.5 <= self.hp <= self.max_hp * 0.75:
            if self.y < 250:
                self.move('down', fps)
                self.equip_armour(Armour('steel plate', 2, 0.4, self))
            if body.x - body.rect.width // 3 <= self.x <= body.x:
                pass
            else:
                if self.x + self.rect.width + 10 >= size[0]:
                    self.side = 2
                if self.x - 10 <= 0:
                    self.side = 1
                if self.x < size[0] and self.side == 1:
                    self.move('right', fps)
                if self.x > 0 and self.side == 2:
                    self.move('left', fps)
            try:
                self.weapon.chanel.unpause()
            except AttributeError:
                pass
            self.weapon.fire(group=shells, ship=self, quarter=4)
        elif self.max_hp * 0.25 <= self.hp <= self.max_hp * 0.5:
            if self.y < 400:
                self.move('down', fps)
                self.equip_armour(Armour('steel plate', 2, 0.3, self))
            if 0 <= (time() - self.time_update) <= 3:
                if body.x - body.rect.width // 3 <= self.x <= body.x:
                    pass
                else:
                    if body.x > self.x and self.hp > 0:
                        self.move('right', fps)

                    elif body.x < self.x and self.hp > 0:
                        self.move('left', fps)
            elif (time() - self.time_update) >= 5:
                self.time_update = time()
            try:
                self.weapon.chanel.unpause()
            except AttributeError:
                pass
            self.weapon.fire(group=shells, ship=self, quarter=4)
        elif 0 < self.hp <= self.max_hp * 0.25:
            self.move('down', fps)
            self.equip_armour(Armour('steel plate', 2, 0.2, self))
            if body.x <= self.x <= body.x + body.rect.width // 2:
                pass
            else:
                if body.x > self.x and self.hp > 0:
                    self.move('right', fps)
                elif body.x < self.x and self.hp > 0:
                    self.move('left', fps)
        else:
            try:
                self.weapon.chanel.pause()
            except AttributeError:
                pass
        if time() - self.start >= 1 and self.start != 0:
            self.kill()
            self.start = 0
        # self.weapon.fire(group=shells, ship=self, quarter=4)


class Titan34D(SpaceShip):
    def __init__(self, pos):
        super().__init__('Titan 34D', pos, 100, 600, titan34D,
                         armor=Armour('titanium plating', 2, 0.9, self))

    def update(self, keys, fps, size, screen, body, shells):
        self.move('down', fps)
        self.draw_hp(screen)
        if time() - self.start >= 1 and self.start != 0:
            self.kill()
            self.start = 0

    def death(self):
        pass


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

    def death(self):
        pass

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

    def update(self, keys, fps, size, screen, body, shells):
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
