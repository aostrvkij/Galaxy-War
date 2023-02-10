import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, filename, action, width, height, x, y):
        super().__init__()
        self.width, self.height = width, height
        self.action = action
        self.image = pygame.transform.scale(pygame.image.load(filename), (int(width), int(height)))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def update(self, game):

        mouse = pygame.mouse.get_pos()
        if self.rect.x < mouse[0] < self.rect.x + self.rect.width:
            if self.rect.y < mouse[1] < self.rect.y + self.rect.height:
                if self.action == 'newgame' or self.action == 'restart':
                    game.game()
                if self.action == 'congame':
                    game.run_pause = True
                if self.action == 'settgame':
                    game.settings()
                if self.action == 'menu':
                    game.menu()
                if self.action == 'library':
                    game.library()
                if self.action == 'exit':
                    game.run_menu, game.run_game, game.run_over, game.run_settings, game.run_library, game.run_congame = \
                        False, False, False, False, False, False
                if self.action == 'exit_2':
                    game.exit = True
