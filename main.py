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
                    if self.action == 'settings':
                        pass
                    if self.action == 'library':
                        pygame.time.delay(200)
                    if self.action == 'exit':
                        game.run_menu = False

    def check_click(self):
        pass


var_btn_menu = [
    Button('Images/btns/newgame.png', 'newgame', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 - SCREEN_HEIGHT * 0.08 * 2),
    Button('Images/btns/congame.png', 'congame', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 - SCREEN_HEIGHT * 0.08),
    Button('Images/btns/settings.png', 'settings', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2),
    Button('Images/btns/library.png', 'library', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 + SCREEN_HEIGHT * 0.08),
    Button('Images/btns/exit.png', 'exit', SCREEN_WIDTH * 0.20, SCREEN_HEIGHT * 0.08,
           SCREEN_WIDTH // 2 - SCREEN_WIDTH * 0.2 // 2, SCREEN_HEIGHT // 2 - SCREEN_HEIGHT * 0.08 // 2 + SCREEN_HEIGHT * 0.08 * 2),
                ]


class Game:
    def __init__(self, SIZE, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.fps = 60
        self.run_menu, self.run_over, self.over_over = True, False, False
        self.menu_btn = pygame.sprite.Group()
        for i in var_btn_menu:
            self.menu_btn.add(i)

    def menu(self):
        self.run_menu, self.run_over, self.over_over = True, False, False
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
                    self.run_menu = False

    def game(self):
        pass

    def over(self):
        pass

    def info(self):
        pass


class Button(pygame.sprite.Sprite):
    def __init__(self, filename, action, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.width, self.height = width, height
        self.action = action
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def check_click(self):
        pass


if __name__ == '__main__':
    game = Game(SCREEN_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT)
    game.menu()
