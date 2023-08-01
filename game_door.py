import pygame

class GameDoor:
    def __init__(self, x, y, width, height, color, surface, variety):
        self.type = 4
        self.left_edge_x = x
        self.top_edge_y = y
        self.width = width
        self.height = height
        self.color = color
        self.surface = surface
        self.variety = variety
        self.is_open = False
        self.door = pygame.Rect(self.left_edge_x, self.top_edge_y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.door)

    def update(self, user_input, object_list):
        pass