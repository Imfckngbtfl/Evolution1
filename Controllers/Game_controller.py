from Engine import Map
import Map_controller
import Action_controller


class GameController:
    def start(self, width, height):
        game_over = False
        map_file = ''
        game_map = Map.Map(width, height)
        map_control = Map_controller.MapController()
        a = Action_controller.ActionController()
        map_control.fill_map(game_map, map_file)
        while not game_over:
            a.action(game_map)
            map_control.draw_map(game_map)
