import pygame

class GameRect:
    def __init__(self, x, y, width, height, image, surface, win_widths, win_heights):
        self.type = "rectangle"
        self.score = 0
        self.left_edge_x = x
        self.top_edge_y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image).convert_alpha()
        self.surface = surface
        self.step = 30
        self.win_widths = win_widths
        self.win_heights = win_heights
        self.count = 0
        self.bounding_box = pygame.Rect(self.left_edge_x, self.top_edge_y, self.width, self.height)
        self.move_freeze = 150
        self.move_freeze_timer = self.move_freeze


    def draw(self):
        self.bounding_box = pygame.Rect(self.left_edge_x, self.top_edge_y, self.width, self.height)
        self.surface.blit(self.image, self.bounding_box)

    def update(self, user_input, object_list, get_time):
        if self.move_freeze_timer <= 0:
            is_move = False
            change_y = self.top_edge_y
            change_x = self.left_edge_x

            if user_input[pygame.K_UP]:
                if self.top_edge_y > 0:
                    change_y = self.top_edge_y - self.step
                is_move = True

            elif user_input[pygame.K_DOWN]:
                if self.top_edge_y + self.height < self.win_heights:
                    change_y = self.top_edge_y + self.step
                is_move = True

            elif user_input[pygame.K_LEFT]:
                if self.left_edge_x > 0:
                    change_x = self.left_edge_x - self.step
                is_move = True

            elif user_input[pygame.K_RIGHT]:
                if self.left_edge_x + self.width < self.win_widths:
                    change_x = self.left_edge_x + self.step
                is_move = True

            collision_x = False
            collision_y = False
            for i in object_list.object_list:

                if i.type == "key" and self.bounding_box.colliderect(i.bounding_box):
                    object_list.object_list.pop(object_list.object_list.index(i))
                    if i.variety == 1:
                        print("Door 1 open now")
                        for ii in object_list.object_list:
                            if ii.type == "door" and ii.variety == 1:
                                ii.is_open = True


                    elif i.variety == 2:
                        print("Door 2 open now")
                        for ii in object_list.object_list:
                            if ii.type == "door" and ii.variety == 2:
                                ii.is_open = True

                if i.type == "door":
                    if not i.is_open:
                        self.bounding_box = pygame.Rect(change_x, self.top_edge_y, self.width, self.height)
                        if self.bounding_box.colliderect(i.bounding_box):
                            collision_x = True
                        self.bounding_box = pygame.Rect(self.left_edge_x, change_y, self.width, self.height)
                        if self.bounding_box.colliderect(i.bounding_box):
                            collision_y = True

                if i.type == "rock":
                    self.bounding_box = pygame.Rect(change_x, self.top_edge_y, self.width, self.height)
                    if self.bounding_box.colliderect(i.bounding_box):
                        collision_x = True
                    self.bounding_box = pygame.Rect(self.left_edge_x, change_y, self.width, self.height)
                    if self.bounding_box.colliderect(i.bounding_box):
                        collision_y = True

                if i.type == "exit":
                    if self.bounding_box.colliderect(i.bounding_box):
                        print("You WIN!!!")

                if i.type == "diamond":
                    if self.bounding_box.colliderect(i.bounding_box):
                        object_list.object_list.pop(object_list.object_list.index(i))
                        self.score = self.score + 1
                        #print(self.score)

                if i.type == "soil":
                    if self.bounding_box.colliderect(i.bounding_box):
                        object_list.object_list.pop(object_list.object_list.index(i))

            if not collision_x:
                if not collision_y:
                    self.left_edge_x = change_x
                    self.top_edge_y = change_y
                else:
                    self.left_edge_x = change_x
            elif not collision_y:
                self.top_edge_y = change_y

            if is_move:
                self.move_freeze_timer = self.move_freeze

        else:
            self.move_freeze_timer -= get_time