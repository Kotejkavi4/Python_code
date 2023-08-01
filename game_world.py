import pygame
#import pytmx
import csv
from game_background import GameBackground
from game_rectangle import GameRect
from game_rock import GameRock
from object_list import ObjectList
from game_exit import GameExit
from game_door import GameDoor
from game_key import GameKey

class GameWorld:
    def __init__(self):
        self.window_width = 900
        self.window_height = 600
        self.class_object_list = ObjectList()
        self.class_object_list.object_list = []
        self.map_data = []

    def setup(self):
        rectangle_width = 30
        rectangle_height = 30
        pygame_display_window = pygame.display.set_mode((self.window_width, self.window_height))
        self.class_object_list.object_list = []
        object_class_game_bkg = GameBackground(pygame_display_window)
        self.class_object_list.object_list.append(object_class_game_bkg)
        #layer = self.tmx_data.get_layer_by_name("main")
        #layer_index = 0

        # Because now I'm using "Only one layer" system, the only index of it can be 0
        # If in the future I will be using more than one layer, I need to add this code, to find layer index:
        #
        # for layer in tmx_data.layers:
        #     if layer.name == /layer_name/:  #insert correct layer's correct name
        #         layer_index = layer.index
        #         break

        with open("map1.csv", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                self.map_data.append([int(tile_id) for tile_id in row])

        for y, row in enumerate(self.map_data):
            for x, tile_value in enumerate(row):
                print(x, y, tile_value)
                if tile_value == 0:
                    object_class_game_rock = GameRock(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, "game_rock.png", pygame_display_window)
                    self.class_object_list.object_list.append(object_class_game_rock)
                elif tile_value == 13:
                    object_class_game_key = GameKey(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, "game_key_type_2.png", pygame_display_window, 2)
                    self.class_object_list.object_list.append(object_class_game_key)
                elif tile_value == 3:
                    object_class_game_key = GameKey(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, "game_key_type_1.png", pygame_display_window, 1)
                    self.class_object_list.object_list.append(object_class_game_key)
                elif tile_value == 1:
                    object_class_game_exit = GameExit(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, "game_exit.png", pygame_display_window)
                    self.class_object_list.object_list.append(object_class_game_exit)
                elif tile_value == 12:
                    object_class_game_door = GameDoor(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, "game_door_type_2.png", pygame_display_window, 2)
                    self.class_object_list.object_list.append(object_class_game_door)
                elif tile_value == 2:
                    object_class_game_door = GameDoor(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, "game_door_type_1.png", pygame_display_window, 1)
                    self.class_object_list.object_list.append(object_class_game_door)
                elif tile_value == 4:
                    object_class_game_rect = GameRect(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, "game_rectangle.png", pygame_display_window, self.window_width, self.window_height)
                    self.class_object_list.object_list.append(object_class_game_rect)
        #object_class_game_bkg = GameBackground(pygame_display_window)
        #self.class_object_list.object_list.append(object_class_game_bkg)

        # Info about GID:
        # GID 0 ---> Empty            //ok
        # GID 1 ---> Player           //ok
        # GID 2 ---> Wall             //ok
        # GID 3 ---> Key (type 2)     //4
        # GID 4 ---> Key (type 1)     //3
        # GID 5 ---> Exit             //6
        # GID 6 ---> Door (type 2)    //7
        # GID 7 ---> Door (type 1)    //5

        '''''
        for y in range(layer.height):
            for x in range(layer.width):
                gid = layer.data[y][x]
                print(gid, end=' ')

                if gid == 1:
                    object_class_game_rect = GameRect(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, (255, 255, 255), pygame_display_window, self.window_width, self.window_height)
                    self.class_object_list.object_list.append(object_class_game_rect)
                elif gid == 2:
                    object_class_game_rock = GameRock(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, (255, 0, 0), pygame_display_window)
                    self.class_object_list.object_list.append(object_class_game_rock)
                elif gid == 4:
                    object_class_game_key = GameKey(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, (255, 51, 153), pygame_display_window, 2)
                    self.class_object_list.object_list.append(object_class_game_key)
                elif gid == 3:
                    object_class_game_key = GameKey(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, (102, 102, 255), pygame_display_window, 1)
                    self.class_object_list.object_list.append(object_class_game_key)
                elif gid == 6:
                    object_class_game_exit = GameExit(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, (255, 255, 0), pygame_display_window)
                    self.class_object_list.object_list.append(object_class_game_exit)
                elif gid == 7:
                    object_class_game_door = GameDoor(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, (255, 51, 153), pygame_display_window, 2)
                    self.class_object_list.object_list.append(object_class_game_door)
                elif gid == 5:
                    object_class_game_door = GameDoor(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, (102, 102, 255), pygame_display_window, 1)
                    self.class_object_list.object_list.append(object_class_game_door)
            print("|")
                #z = self.tmx_data.get_tile_gid(x, y, layer_index)
                #print(x, y, z, z % 10, z / 10)
        #        print(x, y, self.tmx_data.get_tile_properties(x, y, layer_index))
            #print(self.tmx_data.get_tile_locations_by_gid(self.tmx_data.get_tile_gid(x, y, layer_index)))
        #    self.class_object_list.object_list.append(GameRock(x * rectangle_height, y * rectangle_width, rectangle_width, rectangle_height, (255, 0, 0), pygame_display_window))
        '''''
    def draw(self):
        for x in self.class_object_list.object_list:
            x.draw()

    def update(self, user_input):
        for x in self.class_object_list.object_list:
            x.update(user_input, self.class_object_list)