import Cell
import numpy as np


class Map:

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.cells = []

    def generate(self):
        for i in range(self.height + 1):
            cell_row = []
            for j in range(self.width + 1):
                k = Cell.Cell([])
                cell_row.append(k)
            self.cells.append(cell_row)

    def set_cell(self, x, y, object):
        self.cells[x][y].set_object(object)
