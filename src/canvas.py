import cell as cell
import pygame
import random


class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cell_size = 40
        self.rows = height // self.cell_size
        self.cols = width // self.cell_size
        self.grid = self.create_grid()
        self.running = False
        self.paused = True  # Start paused
        self.frame_count = 0
        self.update_rate = 10

        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Game of Life")
        self.clock = pygame.time.Clock()

    def create_grid(self):
        return [[cell.Cell(x * self.cell_size, y * self.cell_size)
                 for x in range(self.cols)]
                for y in range(self.rows)]

    def randomize_grid(self):
        for row in self.grid:
            for single_cell in row:
                single_cell.set_state(random.choice([0, 1]))

    def get_cell_from_pos(self, pos):
        x, y = pos
        row = y // self.cell_size
        col = x // self.cell_size
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col]
        return None

    def draw(self):
        self.screen.fill((128, 128, 128))  # Gray background
        for row in self.grid:
            for single_cell in row:
                pygame.draw.rect(self.screen, single_cell.color, single_cell)
                # Draw grid lines
                pygame.draw.rect(self.screen, (64, 64, 64), single_cell, 1)
        pygame.display.flip()

    def clear_grid(self):
        for row in self.grid:
            for single_cell in row:
                single_cell.set_state(0)

    def get_neighbors_state(self, row, col):
        neighbors = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        alive_neighbors = 0
        for dx, dy in neighbors:
            new_row, new_col = row + dy, col + dx
            if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                alive_neighbors += self.grid[new_row][new_col].get_state()
        return alive_neighbors

    def get_next_state(self, row, col):
        """Calculate the next state for a cell without changing it"""
        neighbors_state = self.get_neighbors_state(row, col)
        current_state = self.grid[row][col].get_state()

        if current_state == 1:  # Cell is alive
            if neighbors_state < 2 or neighbors_state > 3:
                return 0  # Cell dies
            return 1  # Cell stays alive
        else:  # Cell is dead
            if neighbors_state == 3:
                return 1  # Cell becomes alive
            return 0  # Cell stays dead


    def update_all_cells(self):
        """Update all cells simultaneously at a controlled rate"""
        if not self.paused:
            self.frame_count += 1
            if self.frame_count >= self.update_rate:
                # Calculate all next states first
                next_states = [[self.get_next_state(row, col)
                                for col in range(self.cols)]
                               for row in range(self.rows)]

                # Then update all cells
                for row in range(self.rows):
                    for col in range(self.cols):
                        self.grid[row][col].set_state(next_states[row][col])

                self.frame_count = 0  # Reset frame counter