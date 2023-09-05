import pygame
from ecs import Component

class DrawComponent(Component):
    def __init__(self, image):
        self.image = pygame.image.load(image).convert_alpha()