import Cell.py
class Map():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def Generate(self, map):
        for i in map:
            for j in