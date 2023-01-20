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
        click = pygame.mouse.get_pressed()
        if self.rect.x < mouse[0] < self.rect.x + self.rect.width:
            if self.rect.y < mouse[1] < self.rect.y + self.rect.height:
                if click[0] == 1:
                    if self.action == 'newgame':
                        game.game()
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



