import pygame

class GameBackground:
    def __init__(self, surface):
        self.type = 0
        self.color = (30, 170, 170)
        self.surface = surface
        pygame.display.set_caption("Proof of concept")

    def draw(self):
        self.surface.fill(self.color)

    def update(self, user_input, object_list):
        pass