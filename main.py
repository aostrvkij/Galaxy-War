from ships import *
import pygame
from math import pi, atan

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h))
    size = screen.get_size()
    run = True
    clock = pygame.time.Clock()
    fps = 60
    ship = SpaceShip('buran', [0, 0], 100, 300, 1, 1, 'green')
    a = 0
    s = 0
    d = 0
    b = 0
    mouse_pos = (0, 0)
    bullets = list()
    ships = pygame.sprite.Group()
    shells = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    ships.add(ship)
    asteroid = Asteroid((50, 50), 60, 30, 100)
    asteroids.add(asteroid)
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
                    pos = [ship.rect.x, ship.rect.y]
                    try:
                        bullets.append(ClassicAmmunition(pos, 240, 1, 1))
                    except ZeroDivisionError:
                        bullets.append(ClassicAmmunition(pos, 240, 1, 1))
                    shells.add(bullets[-1])
                    b = 1

        if b:
            for bullet in bullets:
                bullet.move(fps)
        if ship.hp <= 0:
            run = False
        ships.update(keys, fps, shells)
        asteroids.update(shells)
        ships.draw(screen)
        shells.draw(screen)
        asteroids.draw(screen)
        clock.tick(fps)
        pygame.display.flip()

