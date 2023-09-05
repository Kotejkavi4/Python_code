from draw_component import DrawComponent
from movement_component import MovementComponent
from movement_system import MovementSystem
from managers import entity_manager_object, system_manager_object
from draw_system import DrawSystem
import pygame
from position_component import PositionComponent

screen_width = 900
screen_height = 600
pygame_display_window = pygame.display.set_mode((screen_width, screen_height))
run = True

player_entity = entity_manager_object.create_entity()
#rock = entity_manager_object.create_entity()

entity_manager_object.add_component(player_entity, PositionComponent(0, 0, 30, 30))
entity_manager_object.add_component(player_entity, MovementComponent(5))
entity_manager_object.add_component(player_entity, DrawComponent("C:/Users/user/src/Python_code/ecs_implement/res/game_rectangle.png"))

draw_system = DrawSystem(pygame_display_window)
movement_system = MovementSystem(screen_width, screen_height)

system_manager_object.add_system(draw_system)
system_manager_object.add_system(movement_system)

clock = pygame.time.Clock()

while run:
    pygame_display_window.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    dt = clock.tick(60) / 1000

    system_manager_object.update(dt)
    pygame.display.update()