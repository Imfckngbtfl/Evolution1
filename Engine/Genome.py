import Color_genes.py
import Energy_gene.py
class Genome():
    self.Max_Minerals_bonus = 5
    self.Max_Berries_bonus = 5
    self.Min_Minerals_bonus = -5
    self.Min_Berries_bonus = -5
    self.Max_Strength = 50
    self.Red = Color_gene("Red"),
    self.Green = Color_gene("Green"),
    self.Blue = Color_gene("Blue"),
    self.Minerals_bonus = Energy_gene(Min_Minerals_bonus, Max_Minerals_bonus, "Minerals"),
    self.Berries_bonus = Energy_gene(Min_Berries_bonus, Max_Berries_bonus, "Berries"),
    self.Strength = Gene(0, 50)
    self.Start_energy = Gene (10,25)
    self.Genes = [self.Red, self.Green, self.Blue, self.Mine, self.Minerals_bonus, self.Berries_bonus, self.Strength, self.Start_energy]
    def __init__(self):
        pass
    def generate(self):
        for i in Genes:
            i.Generate()
        return self
    def mutate(self):
        for i in Genes:
            k = random(1,100)
            if k <=10:
                i.mutate()