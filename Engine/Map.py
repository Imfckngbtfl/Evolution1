import Cell.py
import numpy as np
class Map():
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def Generate(self):
        self.cells = []
        for i in range(self.h):
            cell_row = []
            for j in range(self.w):
                cell_row.append(Cell(x,y))
            self.cells.append(cell_row)
