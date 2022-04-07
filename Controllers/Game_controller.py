from Engine.Map import Map
from Map_controller import MapController
from Action_controller import ActionController


class GameController:
    def __init__(self, width, height):
        self.game_over = False
        self.map_control = MapController()
        self.game_map = Map(width, height)
        self.a = ActionController()

    def start(self, map_file):
        game_over = False
        self.map_control.fill_map(self.game_map, map_file)
        while not game_over:
            self.a.action(self.game_map)
            self.map_control.draw_map(self.game_map)
