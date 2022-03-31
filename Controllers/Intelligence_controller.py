class Intelligence_controller(Intelligence):
    def __init__(self):
        self.Intelligenece = Intelligence
        self.Current = 0
    self.Dict = {0:"f",1:"fr",2:"r",3:"b"}
    def Do(self):
        if self.Intelligenece[self.Current] <=8:
            Move_controller()
