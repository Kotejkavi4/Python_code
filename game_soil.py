import pygame

class GameSoil:
    def __init__(self, x, y, width, height, image, surface):
        self.type = "soil"
        self.left_edge_x = x
        self.top_edge_y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image).convert_alpha()
        self.surface = surface
        self.soil = pygame.Rect(self.left_edge_x, self.top_edge_y, self.width, self.height)

    def draw(self):
        self.surface.blit(self.image, self.soil)

    def update(self, user_input, object_list):
        pass