import pygame

class GameDoor:
    def __init__(self, x, y, width, height, image, surface, variety):
        self.type = "door"
        self.left_edge_x = x
        self.top_edge_y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image).convert_alpha()
        self.surface = surface
        self.variety = variety
        self.is_open = False
        self.door = pygame.Rect(self.left_edge_x, self.top_edge_y, self.width, self.height)

    def draw(self):
        self.surface.blit(self.image, self.door)

    def update(self, user_input, object_list):
        pass