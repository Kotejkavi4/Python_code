import pygame
from ecs import Component

class PositionComponent(Component):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bounding_box = pygame.Rect(self.x, self.y, self.width, self.height)
