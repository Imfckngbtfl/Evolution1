import Move_controller
import Eat_controller


def check_one(x, lim_x):
    if (x >= 0) and (x <= lim_x):
        return 1
    else:
        return 0


def check(x, lim_x, y, lim_y):
    return check_one(x, lim_x) * check_one(y, lim_y)


places = {'fl': [-1, -1], 'f': [-1, 0], 'fr': [-1, 1], 'r': [0, 1], 'br': [1, 1], 'b': [1, 0], 'bl': [1, -1], 'l': [0, -1]}


class ActionController:
    m = Move_controller.MoveController()
    e = Eat_controller.EatController()

    def action(self, world_map):
        for i in range(world_map.height + 1):
            for j in range(world_map.width + 1):
                cell = world_map.cells[i][j]
                for object in cell:
                    if object.play() is not None:
                        action, place = object.play()
                        action_cell_index = [i + places[place][0], j + places[place][1]]
                        if check(action_cell_index[0], world_map.width, action_cell_index[1], world_map.width) == 1:
                            action_cell = world_map.cells[action_cell_index[0]][action_cell_index[1]]
                            if action == 'Move':
                                self.m.move(cell, object, action_cell)
                            if action == 'Eat':
                                self.e.eat(object, action_cell)
