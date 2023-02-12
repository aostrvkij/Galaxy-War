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
                if self.action == 'compl+':
                    game.complexity += 1
                if self.action == 'compl-':
                    game.complexity -= 1
                if self.action == 'menu':
                    game.menu()
                if self.action == 'hightscore':
                    game.hight_score()
                if self.action == 'library':
                    game.library()
                if self.action == 'exit':
                    game.run_menu, game.run_game, game.run_over, game.run_settings, game.run_library, game.run_congame, game.run_hight_score = \
                        False, False, False, False, False, False, False
                if self.action == 'exit_2':
                    game.exit = True
                if self.action == 'buran':
                    game.info_shatle('Буран', 'Images/btn_info/img_5.png' , 'Images/btn_info/image_prev_ui.png')
                if self.action == 'uragan':
                    game.info_shatle('Ураган', 'Images/btn_info/image (1).png', 'Images/btn_info/img1.png')
                if self.action == 'dream':
                    game.info_shatle('Dream Chaser', 'Images/btn_info/img_3.png', 'Images/btn_info/img_2.png')
                if self.action == 'shutl':
                    game.info_shatle('Space Shuttle', 'Images/btn_info/img_9.png', 'Images/btn_info/img_1.png')
                if self.action == 'titan':
                    game.info_shatle('Titan 34D', 'Images/btn_info/img_10.png', 'Images/btn_info/img_11.png')
                
