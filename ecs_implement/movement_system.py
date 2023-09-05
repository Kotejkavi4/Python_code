from ecs import System
from ecs.exceptions import NonexistentComponentTypeForEntity
from position_component import PositionComponent
from movement_component import MovementComponent
import pygame


class MovementSystem(System):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, dt):
        for entity_id, position_component in self.entity_manager.pairs_for_type(PositionComponent):
            try:
                movement_component = self.entity_manager.component_for_entity(entity_id, MovementComponent)
                user_input = pygame.key.get_pressed()
                change_y = position_component.y
                change_x = position_component.x
                if user_input[pygame.K_UP]:
                    if position_component.y > 0:
                        change_y = position_component.y - movement_component.step

                elif user_input[pygame.K_DOWN]:
                    if position_component.y + position_component.height < self.screen_height:
                        change_y = position_component.y + movement_component.step

                elif user_input[pygame.K_LEFT]:
                    if position_component.x > 0:
                        change_x = position_component.x - movement_component.step

                elif user_input[pygame.K_RIGHT]:
                    if position_component.x + position_component.width < self.screen_width:
                        change_x = position_component.x + movement_component.step

                position_component.y = change_y
                position_component.x = change_x
            except NonexistentComponentTypeForEntity:
                continue
