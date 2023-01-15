import ships
import pygame


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h))
    size = screen.get_size()
    run = True
    clock = pygame.time.Clock()
    fps = 60
    ship = ships.SpaceShip('baron', [0, 0], 100, 300, 1, 1, 1)
    w = 0
    a = 0
    s = 0
    d = 0
    while run:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_w:
                    w = 1
                if event.key == pygame.K_s:
                    s = 1
                if event.key == pygame.K_a:
                    a = 1
                if event.key == pygame.K_d:
                    d = 1
            if w:
                ship.move('up', fps)
            if s:
                ship.move('down', fps)
            if a:
                ship.move('left', fps)
            if d:
                ship.move('right', fps)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    w = 0
                if event.key == pygame.K_s:
                    s = 0
                if event.key == pygame.K_a:
                    a = 0
                if event.key == pygame.K_d:
                    d = 0

        ship.draw(screen)
        clock.tick(fps)
        pygame.display.flip()

