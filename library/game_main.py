from library.classes import *
import pygame
import moviepy.editor
from random import randint
import time


def main(FPS, count, data_ship, game):
    pygame.mixer.music.load("Images/data/music.mp3")
    pygame.init()
    # video = moviepy.editor.VideoFileClip("Images/data/Spaceship-start.mp4")
    # video.preview()
    start = time.time()
    pusk = time.time()
    pusk_as = time.time()
    pygame.mixer.pre_init(44100, -32, 100, 1024)
    screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h))
    size = screen.get_size()
    run = True
    clock = pygame.time.Clock()
    fps = FPS
    ships = pygame.sprite.Group()
    shells = pygame.sprite.Group()
    ship = Buran((size[0] // 2, size[1] - 158), *data_ship)
    ships.add(ship)
    # ship.equip_gun(MachineGun())
    pygame.mixer.music.play(loops=-1, start=5)
    pygame.mixer.music.set_volume(0.2)
    count_enemy = 0
    count_asteroids = 0
    while run:
        pygame.mixer.music.unpause()
        keys = pygame.key.get_pressed()
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.pause()
                    pygame.mixer.pause()
                    run = game.pause_menu()

        if count_asteroids < count[0] and (time.time() - pusk_as) >= count[2]:
            # if (time.time() - start) % 1 == 0:
            x = randint(1, 100)
            count_asteroids += 1
            if 1 <= x <= 85:
                ships.add(Asteroid((randint(0, size[0] - 60), randint(-250, -100)), randint(30, 100),
                                   randint(25, 50)))
            elif 86 <= x <= 95:
                ships.add(AsteroidIron((randint(0, size[0] - 60), randint(-250, -100)), randint(30, 100),
                                       randint(15, 35)))
            elif 96 <= x <= 100:
                ships.add(AsteroidGold((randint(0, size[0] - 60), randint(-250, -100)), randint(30, 100),
                                       randint(10, 20)))
            pusk_as = time.time()

        if count_enemy < count[1] and (time.time() - pusk) >= count[3]:
            x = randint(1, 100)
            if 1 <= x <= 20:
                ships.add(Titan34D((randint(int(ship.x) - 20, int(ship.x) + 20), -100)))
                count_enemy += 1
            elif 21 <= x <= 50:
                ships.add(SpaceShuttle((randint(0, size[0] - 60), -10)))
                count_enemy += 1
            elif 51 <= x <= 60:
                ships.add(DreamChaser((randint(0, size[0] - 80), -100)))
                count_enemy += 1
            pusk = time.time()

        if ship.hp <= 0:
            run = False
        for bullet in shells:
            if pygame.sprite.spritecollide(bullet, ships, False):
                for i in pygame.sprite.spritecollide(bullet, ships, False):
                    bullet.give_damage(i)
                    if i.hp is False:
                        if type(i) == library.classes.Asteroid or type(i) == library.classes.AsteroidIron or \
                                type(i) == library.classes.AsteroidGold:
                            i.kill()
                            count_asteroids -= 1
                        else:
                            i.kill()
                            count_enemy -= 1
                        i.death()
                        ships.remove(i)
            if bullet.y > size[1] + 20 or bullet.y < - 20:
                shells.remove(bullet)

        for s in ships:
            if s.rect.y > size[1]:
                if type(s) == library.classes.Asteroid or type(s) == library.classes.AsteroidIron or \
                        type(s) == library.classes.AsteroidGold:
                    count_asteroids -= 1
                else:
                    count_enemy -= 1
                s.death()
                ships.remove(s)
            if pygame.sprite.spritecollide(s, ships, False):
                for i in pygame.sprite.spritecollide(s, ships, False):
                    if s is not i:
                        s.give_damage(i)
                        if s.hp is False:
                            if type(s) == library.classes.Asteroid or type(s) == library.classes.AsteroidIron or \
                                    type(s) == library.classes.AsteroidGold:
                                s.kill()
                                count_asteroids -= 1
                            else:
                                s.kill()
                                count_enemy -= 1
                            s.death()
                            ships.remove(s)

                        if i.hp is False:
                            if type(i) == library.classes.Asteroid or type(i) == library.classes.AsteroidIron or \
                                    type(i) == library.classes.AsteroidGold:
                                i.kill()
                                count_asteroids -= 1
                            else:
                                i.kill()
                                count_enemy -= 1
                            i.death()
                            ships.remove(i)

        shells.draw(screen)
        ships.draw(screen)
        shells.update(fps)
        ships.update(keys, fps, size, screen, ship, shells)
        score_text = pygame.font.SysFont('impact', 30).render(f'{ship.score * int(time.time() - start)}', 1,
                                                              (152, 146, 173))
        game.screen.blit(score_text,
                         score_text.get_rect(center=(size[0] // 2, size[1] * 0.025)))
        clock.tick(fps)
        pygame.display.flip()
    pygame.mixer.music.stop()
    pygame.mixer.pause()
    return ship.score * int(time.time() - start), ship.money
# muhamad ge(ni)y