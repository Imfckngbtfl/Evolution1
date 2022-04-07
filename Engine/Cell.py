from Resource import Resource
from Plane import Plane
from Mineral_cell import MineralCell


class Cell:
    def __init__(self, objects):
        self.objects = objects
        self.is_update = 1

    def set_object(self, object):
        self.objects.append(object)
        self.is_update = 1

    def get_object(self):
        return self.objects

    def remove_object(self, object):
        self.objects.pop(object)
        self.is_update = 1

    def update(self):
        self.is_update = 0

    def is_empty_for_berry(self):
        is_plane_in_cell = False
        for object in self:
            if type(object) == Resource:
                return False
            if type(object) == Plane:
                is_plane_in_cell = True
        return is_plane_in_cell

    def is_empty_for_mineral(self):
        is_mineral_cell_in_cell = False
        for object in self:
            if type(object) == Resource:
                return False
            if type(object) == MineralCell:
                is_mineral_cell_in_cell = True
        return is_mineral_cell_in_cell
