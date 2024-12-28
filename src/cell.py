import pygame

class Cell(pygame.Rect):
    def __init__(self, x, y, state=0):
        super().__init__(x, y, 40, 40)
        self.state = state
        self.update_color()

    def update_color(self):
        self.color = (255, 255, 255) if self.state else (0, 0, 0)

    def set_state(self, state):
        self.state = state
        self.update_color()

    def get_state(self):
        return self.state