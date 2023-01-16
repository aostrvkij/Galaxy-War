import pygame

pygame.init()
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((pygame.display.Info().current_w, pygame.display.Info().current_h))
clock = pygame.time.Clock()


class Button(pygame.sprite.Sprite):
    def __init__(self, filename, action, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.width, self.height = width, height
        self.action = action
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.rect.x < mouse[0] < self.rect.x + self.rect.width:
            if self.rect.y < mouse[1] < self.rect.y + self.rect.height:
                if click[0] == 1:
                    if self.action == 'newgame':
                        pass
                    if self.action == 'congame':
                        pass
                    if self.action == 'settgame':
                        game.settings()
                    if self.action == 'menu':
                        game.menu()
                    if self.action == 'library':
                        game.library()
                    if self.action == 'exit':
                        game.run_menu, game.run_game, game.run_settings, game.run_library = False, False, False, False


menu_btns = pygame.sprite.Group()
sett_btns = pygame.sprite.Group()
libr_btns = pygame.sprite.Group()


var_menu = [
    Button('Images/btns/newgame.png', 'newgame', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 - SCREEN_HEIGHT * 0.08 * 2),
    Button('Images/btns/congame.png', 'congame', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 - SCREEN_HEIGHT * 0.08),
    Button('Images/btns/settings.png', 'settgame', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2),
    Button('Images/btns/library.png', 'library', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 + SCREEN_HEIGHT * 0.08),
    Button('Images/btns/exit.png', 'exit', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 + SCREEN_HEIGHT * 0.08 * 2),]
var_sett = [
    Button('Images/btns/newgame.png', 'newgame', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 - SCREEN_HEIGHT * 0.08 * 2),
    Button('Images/btns/exit.png', 'menu', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 - SCREEN_HEIGHT * 0.08)]
var_libr = [
    Button('Images/btns/newgame.png', 'newgame', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 - SCREEN_HEIGHT * 0.08 * 2),
    Button('Images/btns/exit.png', 'menu', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 - SCREEN_HEIGHT * 0.08)]


for i in var_menu:
    menu_btns.add(i)
for i in var_sett:
    sett_btns.add(i)
for i in var_libr:
    libr_btns.add(i)


class Game:
    def __init__(self, SIZE, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.fps = 60
        self.run_menu, self.run_game, self.run_settings, self.run_library = True, False, False, False
        self.menu_btn = menu_btns
        self.settings_btn = sett_btns
        self.libr_btns = libr_btns

    def menu(self):
        self.run_menu, self.run_game, self.run_settings, self.run_library = True, False, False, False
        while self.run_menu:
            screen.fill('black')
            self.menu_btn.update()
            self.menu_btn.draw(screen)
            pygame.display.flip()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.run_menu = False
                quit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_settings, self.run_library = False, False, False, False

    def game(self):
        pass

    def settings(self):
        self.run_menu, self.run_game, self.run_settings, self.run_library = False, False, True, False
        while self.run_settings:
            screen.fill('black')
            self.settings_btn.update()
            self.settings_btn.draw(screen)
            pygame.display.flip()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.run_menu = False
                quit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_settings, self.run_library = False, False, False, False

    def over_menu(self):
        pass

    def library(self):
        self.run_menu, self.run_game, self.run_settings, self.run_library = False, False, False, True
        while self.run_library:
            screen.fill('black')
            self.libr_btns.update()
            self.libr_btns.draw(screen)
            pygame.display.flip()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                self.run_menu = False
                quit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_menu, self.run_game, self.run_settings, self.run_library = False, False, False, False


if __name__ == '__main__':
    game = Game(SCREEN_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT)
    game.menu()
