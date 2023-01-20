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
    ship = SpaceShip('baron', [0, 0], 100, 300, 1, 1, 'green')
    a = 0
    s = 0
    d = 0
    b = 0
    mouse_pos = (0, 0)
    bullets = list()
    sprite = pygame.sprite.Group()
    sprite.add(ship)
    while run:
        keys = pygame.key.get_pressed()
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEMOTION:
                mouse_pos = (event.pos[0] - ship.rect.x, event.pos[1] - ship.rect.y)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_SPACE:
                    pos = [ship.rect.x, ship.rect.y]
                    if mouse_pos[0] > 0:
                        if mouse_pos[1] > 0:
                            q = 4
                        else:
                            q = 1
                    else:
                        if mouse_pos[1] > 0:
                            q = 3
                        else:
                            q = 2
                    try:
                        bullets.append(Ammunition(pos, 1, 600, 1, 1, 1, 1, q,
                                                  atan(abs(mouse_pos[1]) / abs(mouse_pos[0])) * 180 / pi / 90))
                    except ZeroDivisionError:
                        bullets.append(Ammunition(pos, 1, 600, 1, 1, 1, 1, q, 1))
                    sprite.add(bullets[-1])
                    b = 1

        if b:
            for bullet in bullets:
                bullet.move(fps)
        sprite.update(keys, fps)
        sprite.draw(screen)
        clock.tick(fps)
        pygame.display.flip()

