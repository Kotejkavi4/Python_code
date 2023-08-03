import pygame

class GameRect:
    def __init__(self, x, y, width, height, image, surface, win_widths, win_heights):
        self.type = 2
        self.score = 0
        self.left_edge_x = x
        self.top_edge_y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image).convert_alpha()
        self.surface = surface
        self.step = 3
        self.win_widths = win_widths
        self.win_heights = win_heights
        self.count = 0
        self.rect = pygame.Rect(self.left_edge_x, self.top_edge_y, self.width, self.height)


    def draw(self):
        self.rect = pygame.Rect(self.left_edge_x, self.top_edge_y, self.width, self.height)
        self.surface.blit(self.image, self.rect)

    def update(self, user_input, object_list):
        change_y = self.top_edge_y
        change_x = self.left_edge_x

        if user_input[pygame.K_UP]:
            if self.top_edge_y > 0:
                change_y = self.top_edge_y - self.step

        if user_input[pygame.K_DOWN]:
            if self.top_edge_y + self.height < self.win_heights:
                change_y = self.top_edge_y + self.step

        if user_input[pygame.K_LEFT]:
            if self.left_edge_x > 0:
                change_x = self.left_edge_x - self.step

        if user_input[pygame.K_RIGHT]:
            if self.left_edge_x + self.width < self.win_widths:
                change_x = self.left_edge_x + self.step

        #self.rect = pygame.Rect(change_x, change_y, self.width, self.height)
        #self.rect = pygame.Rect(self.left_edge_x, self.top_edge_y, self.width, self.height)

        collision_x = False
        collision_y = False
        for i in object_list.object_list:

            if i.type == 5 and self.rect.colliderect(i.key):
                object_list.object_list.pop(object_list.object_list.index(i))
                if i.variety == 1:
                    print("Door 1 open now")
                    for ii in object_list.object_list:
                        if ii.type == 4 and ii.variety == 1:
                            ii.is_open = True


                elif i.variety == 2:
                    print("Door 2 open now")
                    for ii in object_list.object_list:
                        if ii.type == 4 and ii.variety == 2:
                            ii.is_open = True

            if i.type == 4:
                if not i.is_open:
                    self.rect = pygame.Rect(change_x, self.top_edge_y, self.width, self.height)
                    if self.rect.colliderect(i.door):
                        collision_x = True
                    self.rect = pygame.Rect(self.left_edge_x, change_y, self.width, self.height)
                    if self.rect.colliderect(i.door):
                        collision_y = True

            if i.type == 1:
                self.rect = pygame.Rect(change_x, self.top_edge_y, self.width, self.height)
                if self.rect.colliderect(i.rock):
                    collision_x = True
                self.rect = pygame.Rect(self.left_edge_x, change_y, self.width, self.height)
                if self.rect.colliderect(i.rock):
                    collision_y = True

            if i.type == 3:
                if self.rect.colliderect(i.ext):
                    print("You WIN!!!")

            if i.type == 6:
                if self.rect.colliderect(i.diamond):
                    object_list.object_list.pop(object_list.object_list.index(i))
                    self.score = self.score + 1
                    #print(self.score)

        if not collision_x:
            if not collision_y:
                self.left_edge_x = change_x
                self.top_edge_y = change_y
            else:
                self.left_edge_x = change_x
        elif not collision_y:
            self.top_edge_y = change_y
