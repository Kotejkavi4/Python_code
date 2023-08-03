import pygame
import csv
from game_background import GameBackground
from game_rectangle import GameRect
from game_rock import GameRock
from object_list import ObjectList
from game_exit import GameExit
from game_door import GameDoor
from game_key import GameKey
from game_diamond import GameDiamond
#from game_scoreboard import GameScoreboard

class GameWorld:
    def __init__(self):
        self.window_width = 900
        self.window_height = 600
        self.class_object_list = ObjectList()
        self.class_object_list.object_list = []
        self.map_data = []
        self.map_path = "res/map1.csv"

    def setup(self):
        rectangle_width = 30
        rectangle_height = 30
        pygame_display_window = pygame.display.set_mode((self.window_width, self.window_height))
        self.class_object_list.object_list = []
        object_class_game_bkg = GameBackground(pygame_display_window)
        self.class_object_list.object_list.append(object_class_game_bkg)

        with open(self.map_path, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                self.map_data.append([int(tile_id) for tile_id in row])

        for y, row in enumerate(self.map_data):
            for x, tile_value in enumerate(row):
                print(x, y, tile_value)
                if tile_value == 0:
                    object_class_game_rock = GameRock(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, "res/game_rock.png", pygame_display_window)
                    self.class_object_list.object_list.append(object_class_game_rock)
                elif tile_value == 13:
                    object_class_game_key = GameKey(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, "res/game_key_type_2.png", pygame_display_window, 2)
                    self.class_object_list.object_list.append(object_class_game_key)
                elif tile_value == 3:
                    object_class_game_key = GameKey(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, "res/game_key_type_1.png", pygame_display_window, 1)
                    self.class_object_list.object_list.append(object_class_game_key)
                elif tile_value == 1:
                    object_class_game_exit = GameExit(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, "res/game_exit.png", pygame_display_window)
                    self.class_object_list.object_list.append(object_class_game_exit)
                elif tile_value == 12:
                    object_class_game_door = GameDoor(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, "res/game_door_type_2.png", pygame_display_window, 2)
                    self.class_object_list.object_list.append(object_class_game_door)
                elif tile_value == 2:
                    object_class_game_door = GameDoor(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, "res/game_door_type_1.png", pygame_display_window, 1)
                    self.class_object_list.object_list.append(object_class_game_door)
                elif tile_value == 10:
                    object_class_game_rect = GameRect(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, "res/game_rectangle.png", pygame_display_window, self.window_width, self.window_height)
                    self.class_object_list.object_list.append(object_class_game_rect)
                elif tile_value == 11:
                    object_class_game_diamond = GameDiamond(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, "res/game_diamond.png", pygame_display_window)
                    self.class_object_list.object_list.append(object_class_game_diamond)

        #object_class_game_scoreboard = GameScoreboard(self.window_width - (rectangle_width * 2), 0, pygame_display_window)
        #self.class_object_list.object_list.append(object_class_game_scoreboard)

    def draw(self):
        for x in self.class_object_list.object_list:
            x.draw()

    def update(self, user_input):
        for x in self.class_object_list.object_list:
            x.update(user_input, self.class_object_list)