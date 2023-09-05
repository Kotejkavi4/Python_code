from game_world import GameWorld
import pygame
class Game:
    def __init__(self):
        self.world = GameWorld()
        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):
        self.world.setup()
        self.running = True

        while self.running:

            self.world.draw()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.world.update(pygame.key.get_pressed(), self.clock.get_time())
            self.clock.tick_busy_loop(55)

        pygame.quit()