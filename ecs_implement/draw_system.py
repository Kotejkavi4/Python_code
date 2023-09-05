import pygame
from ecs import System
from ecs.exceptions import NonexistentComponentTypeForEntity
from position_component import PositionComponent
from draw_component import DrawComponent

class DrawSystem(System):
    def __init__(self, surface):
        super().__init__()
        self.surface = surface

    def update(self, dt):
        for entity_id, position_component in self.entity_manager.pairs_for_type(PositionComponent):
            try:
                position_component.bounding_box = pygame.Rect(position_component.x, position_component.y, position_component.width, position_component.height)
                draw_component = self.entity_manager.component_for_entity(entity_id, DrawComponent)
                self.surface.blit(draw_component.image, position_component.bounding_box)
            except NonexistentComponentTypeForEntity:
                continue