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
        self.bounding_box = pygame.Rect(self.left_edge_x, self.top_edge_y, self.width, self.height)

    def draw(self):
        score_text = self.font.render("Score: " + str(self.score), True, (255, 255, 255))
        self.surface.blit(score_text, self.bounding_box)

    def update(self, user_input, object_list, get_time):
        for i in object_list.object_list:
            if i.type == "rectangle":
                self.score = i.score