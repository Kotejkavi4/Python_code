import pygame

class GameKey:
    def __init__(self, x, y, width, height, color, surface, variety):
        self.type = 5
        self.left_edge_x = x
        self.top_edge_y = y
        self.width = width
        self.height = height
        self.color = color
        self.surface = surface
        self.variety = variety
        self.active = True
        self.key = pygame.Rect(self.left_edge_x, self.top_edge_y, self.width, self.height)

    def draw(self):
        if self.active:
            pygame.draw.rect(self.surface, self.color, self.key)

    def update(self, user_input, object_list):
        pass