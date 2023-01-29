from classes import *
import pygame
from math import pi, atan

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h))
    size = screen.get_size()
    run = True
    clock = pygame.time.Clock()
    fps = 60
    bullets = list()
    ships = pygame.sprite.Group()
    shells = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid = Asteroid((50, 50), 60, 30, 100)
    ship = Buran((0, 0))
    ships.add(ship)
    ships.add(asteroid)
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
                    bullets.append(ClassicAmmunition(pos, 300, 1, 1))
                    shells.add(bullets[-1])

        if ship.hp <= 0:
            run = False
        for bullet in shells:
            if pygame.sprite.spritecollide(bullet, ships, False):
                for i in pygame.sprite.spritecollide(bullet, ships, False):
                    bullet.give_damage(i)

        shells.update(fps)
        ships.update(keys, fps)
        shells.draw(screen)
        ships.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
