class Gene:
    def __init__(self, Max, Min):
        self.Max = Max
        self.Min = Min
    def Generate(self):
        self.Current = rand(self.Min, self.Max)
    def Mutate(self):
        Generate()
    def Get_current(self):
        return self.Current
