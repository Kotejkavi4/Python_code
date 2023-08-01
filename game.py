from game_world import GameWorld
import pygame
class Game:
    def __init__(self):
        self.world = GameWorld()
        self.running = True

    def run(self):
        self.world.setup()
        self.running = True

        while self.running:
            pygame.time.wait(7)

            self.world.draw()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.world.update(pygame.key.get_pressed())
        pygame.quit()