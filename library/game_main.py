from library.classes import *
import pygame
from random import randint
import time


def main():
    start = time.time()
    pygame.init()
    screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h))
    size = screen.get_size()
    run = True
    clock = pygame.time.Clock()
    fps = 60
    bullets = list()
    asteroids = list()
    ships = pygame.sprite.Group()
    shells = pygame.sprite.Group()
    ship = Buran((size[0] // 2, size[1] - 158))
    ships.add(ship)
    while run:
        keys = pygame.key.get_pressed()
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                # if event.key == pygame.K_SPACE:
                #     pos = [ship.rect.x + ship.rect.width // 2,  ship.rect.y - ship.speed / fps - 7]
                #     bullets.append(ClassicAmmunition(pos, 500, 1, 1))
                #     shells.add(bullets[-1])

        if len(ships) - 1 < 70:
            # if (time.time() - start) % 1 == 0:
            asteroids.append(Asteroid((randint(0, size[0] - 60), randint(-250, -100)), randint(30, 100),
                                      randint(10, 30)))
            asteroids.append(Asteroid((randint(0, size[0] - 60), randint(-250, -100)), randint(30, 100),
                                      randint(10, 30)))
            asteroids.append(Asteroid((randint(0, size[0] - 60), randint(-250, -100)), randint(30, 100),
                                      randint(10, 30)))
            asteroids.append(Asteroid((randint(0, size[0] - 60), randint(-250, -100)), randint(30, 100),
                                      randint(10, 30)))
            asteroids.append(AsteroidIron((randint(0, size[0] - 60), randint(-250, -100)), randint(30, 100),
                                          randint(10, 30)))
            ships.add(asteroids)

        if ship.hp <= 0:
            run = False
        for bullet in shells:
            if pygame.sprite.spritecollide(bullet, ships, False):
                for i in pygame.sprite.spritecollide(bullet, ships, False):
                    bullet.give_damage(i)

        for s in ships:
            if s.hp <= 0 or s.rect.y > size[1]:
                ships.remove(s)
                asteroids.remove(s)
            if pygame.sprite.spritecollide(s, ships, False):
                for i in pygame.sprite.spritecollide(s, ships, False):
                    if s is not i:
                        s.give_damage(i)

        shells.draw(screen)
        ships.draw(screen)
        shells.update(fps)
        ships.update(keys, fps, size, screen)
        clock.tick(fps)
        pygame.display.flip()