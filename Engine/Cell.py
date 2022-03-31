import Creature.py
import Berry.py
import Mineral.py
class Cell():
    def __init__(self, object = NULL, x, y):
        self.object = object
        self.x = x
        self.y = y
    def Set_object(self, object):
        self.object = object
    def Get_object(self):
        return self.object