import Creature.py
import Berry.py
import Mineral.py
class Cell():
    def __init__(self, x, y, object = None):
        self.object = object
        self.x = x
        self.y = y
    def Set_object(self, object):
        self.object = object
    def Get_object(self):
        return self.object