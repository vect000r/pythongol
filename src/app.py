import pygame
import sys
from canvas import Canvas
from menu import Menu


class App:
    def __init__(self):
        pygame.init()

        # Set window dimensions
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 600
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.cell_width = 40
        self.cell_height = 40
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        # Create canvas and menu
        self.canvas = Canvas(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.menu = Menu(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

        # Game state
        self.game_state = 'menu'  # Can be 'menu' or 'game'

        pygame.display.set_caption("Game of Life")

    def run(self):
        running = True
        while running:
            if self.game_state == 'menu':
                self.run_menu()
            else:
                self.run_game()

            self.clock.tick(60)

    def run_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            selected_option = self.menu.handle_event(event)
            if selected_option:
                if selected_option == 'play':
                    self.game_state = 'game'
                elif selected_option == 'exit':
                    pygame.quit()
                    sys.exit()

        self.menu.draw(self.screen)
        pygame.display.flip()

    def run_game(self):
        self.draw()
        self.handle_game_events()
        self.canvas.update_all_cells()

    def draw(self):
        self.screen.fill(self.BLACK)
        self.canvas.draw()
        pygame.display.flip()

    def handle_game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse()
            elif event.type == pygame.KEYDOWN:
                self.handle_keyboard(event.key)

    def handle_mouse(self):
        mouse_pos = pygame.mouse.get_pos()
        cell = self.canvas.get_cell_from_pos(mouse_pos)
        if cell:
            cell.set_state(1 if cell.get_state() == 0 else 0)

    def handle_keyboard(self, key):
        if key == pygame.K_SPACE:
            self.canvas.paused = not self.canvas.paused
        elif key == pygame.K_r:
            self.canvas.randomize_grid()
        elif key == pygame.K_c:
            self.canvas.clear_grid()
        elif key == pygame.K_ESCAPE:
            self.game_state = 'menu'
