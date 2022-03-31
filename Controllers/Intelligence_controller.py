import Cell
class Intelligence_controller():
    def __init__(self, Cell):
        self.Intelligenece = Cell.Get_object().Intelligence
        self.Current = 0
    self.Dict = {0:"f",1:"fr",2:"r",3:"b",4:""}
    def Do(self):
        if self.Intelligenece[self.Current] <=8:
            Move_controller()
