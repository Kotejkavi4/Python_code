import pygame

class GameRock:
    def __init__(self, x, y, width, height, color, surface):
        self.type = 1
        self.left_edge_x = x
        self.top_edge_y = y
        self.width = width
        self.height = height
        self.color = color
        self.surface = surface
        self.rock = pygame.Rect(self.left_edge_x, self.top_edge_y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rock)

    def update(self, user_input, object_list):
        pass