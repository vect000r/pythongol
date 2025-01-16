import pygame
class Menu:
    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height

        pygame.font.init()
        self.font = pygame.font.SysFont('Consolas', 36)
        self.small_font = pygame.font.SysFont('Consolas', 24)
        self.WHITE = (255, 255, 255)
        self.GREEN = (0, 255, 0)

        # Menu items
        self.title = self.font.render('Game Of Life', True, self.WHITE)
        self.play = self.font.render('Play', True, self.WHITE)
        self.instructions = self.small_font.render('Space -> Pause, R -> Reset, C -> Clear', True, self.WHITE)
        self.exit = self.font.render('Exit', True, self.WHITE)

        self.items = [
            (self.title, 'title'),
            (self.play, 'play'),
            (self.instructions, 'instructions'),
            (self.exit, 'exit')
        ]

        self.selected = None
        self.normal_color = self.WHITE
        self.selected_color = self.GREEN

    def draw(self, screen):
        screen.fill((0, 0, 0))

        spacing = 70
        total_height = spacing * len(self.items)
        start_y = (self.height - total_height) // 2

        for i, (item, item_id) in enumerate(self.items):
            item_rect = item.get_rect()
            x = (self.width - item_rect.width) // 2
            y = start_y + (spacing * i)

            screen.blit(item, (x, y))

            if self.selected == item_id and item_id not in ['title', 'instructions']:
                pygame.draw.rect(screen, self.selected_color,
                                 (x - 10, y - 5, item_rect.width + 20, item_rect.height + 10), 2)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            spacing = 70
            total_height = spacing * len(self.items)
            start_y = (self.height - total_height) // 2

            for i, (item, item_id) in enumerate(self.items):
                if item_id in ['title', 'instructions']:
                    continue

                item_rect = item.get_rect()
                x = (self.width - item_rect.width) // 2
                y = start_y + (spacing * i)

                check_rect = pygame.Rect(x, y, item_rect.width, item_rect.height)

                if check_rect.collidepoint(mouse_pos):
                    self.selected = item_id
                    return

            self.selected = None

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.selected