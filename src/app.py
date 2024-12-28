import pygame
import sys
from canvas import Canvas

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

        # Create canvas
        self.canvas = Canvas(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

        pygame.display.set_caption("Game of Life")

    def run(self):
        running = True
        while running:
            self.draw()
            self.handle_events()
            self.canvas.update_all_cells()  # Update cells each frame
            self.clock.tick(60)

    def draw(self):
        self.canvas.draw()

    def handle_events(self):
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
            # Toggle pause/play
            self.canvas.paused = not self.canvas.paused
        elif key == pygame.K_r:
            # Randomize grid
            self.canvas.randomize_grid()
        elif key == pygame.K_c:
            # Clear grid
            self.canvas.clear_grid()

