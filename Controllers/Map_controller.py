from Engine import Cell
from Engine import Wall
from Engine import Mineral
from Engine import Berry


class MapController:

    def fill_map(self, unfilled_map, filled_map_file):
        filled_map_file = filled_map_file.split()
        for i in range(unfilled_map.height):
            for j in range(unfilled_map.width):
                object = None
                if filled_map_file[0] == '0':
                    object = Wall
                unfilled_map.set_cell(object)

    def draw_map(self, map):
        # подаёт команду UI нарисовать карту
        pass
