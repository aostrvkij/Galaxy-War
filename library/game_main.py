from library.classes import *
import pygame
from random import randint
import time


def main(FPS, count_asteroid, count_enemy):
    start = time.time()
    pygame.init()
    screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h))
    size = screen.get_size()
    run = True
    clock = pygame.time.Clock()
    fps = FPS
    ships = pygame.sprite.Group()
    shells = pygame.sprite.Group()
    ship = Buran((size[0] // 2, size[1] - 158))
    enemy = EnemyShip((500, 500))
    ships.add(ship)
    ships.add(EnemyShip((500, 500)))
    ships.add(EnemyShip((200, 500)))

    while run:
        keys = pygame.key.get_pressed()
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    pos = [ship.rect.x + ship.rect.width // 2,  ship.rect.y - ship.speed / fps - 7]
                    shells.add(PiercingAmmunition(pos, 500, 1, 1, ship, 5))

        if len(ships) - 1 < count_asteroid:
            # if (time.time() - start) % 1 == 0:
            x = randint(1, 100)
            if 1 <= x <= 85:
                ships.add(Asteroid((randint(0, size[0] - 60), randint(-250, -100)), randint(30, 100),
                                            randint(25, 50)))
            elif 86 <= x <= 95:
                ships.add(AsteroidIron((randint(0, size[0] - 60), randint(-250, -100)), randint(30, 100),
                                            randint(15, 35)))
            elif 96 <= x <= 100:
                ships.add(AsteroidGold((randint(0, size[0] - 60), randint(-250, -100)), randint(30, 100),
                                            randint(10, 20)))

        if ship.hp <= 0:
            run = False
        for bullet in shells:
            if pygame.sprite.spritecollide(bullet, ships, False):
                for i in pygame.sprite.spritecollide(bullet, ships, False):
                    bullet.give_damage(i)

        for s in ships:
            if s.hp <= 0 or s.rect.y > size[1]:
                ships.remove(s)
            if pygame.sprite.spritecollide(s, ships, False):
                for i in pygame.sprite.spritecollide(s, ships, False):
                    if s is not i:
                        s.give_damage(i)

        shells.draw(screen)
        ships.draw(screen)
        # print(ship.money)
        shells.update(fps)
        ships.update(keys, fps, size, screen)
        clock.tick(fps)
        pygame.display.flip()
