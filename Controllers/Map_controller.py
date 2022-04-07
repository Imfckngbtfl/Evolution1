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
                filled_map_file.pop(0)
                unfilled_map.set_cell(i, j, object)

    def draw_cell(self, x, y):
        # подаёт команду UI нарисовать (обновить) клетку на данной координате
        pass

    def draw_map(self, game_map):
        for i in range(game_map.height + 1):
            for j in range(game_map.width + 1):
                cell = game_map[i][j]
                if cell.is_update == 1:
                    self.draw_cell(i, j)
                    cell.update()

