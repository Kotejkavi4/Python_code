import pygame
pygame.font.init()

class GameScoreboard:
    def __init__(self, x, y, width, height, surface):
        self.type = "scoreboard"
        self.surface = surface
        self.score = 0
        self.left_edge_x = x
        self.top_edge_y = y
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 36)
        self.scoreboard = pygame.Rect(self.left_edge_x, self.top_edge_y, self.width, self.height)

    def update(self, user_input, object_list):
        for i in object_list.object_list:
            if i.type == 2:
                self.score = i.score



    def draw(self):
        score_text = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.surface.blit(score_text, self.scoreboard)
