import Creature.py
import Berry.py
import Mineral.py
class Cell():
    def __init__(self, object = NULL):
        self.object = object
    def Set_object(self, object):
        self.object = object
    def Get_object(self):
        return self.object