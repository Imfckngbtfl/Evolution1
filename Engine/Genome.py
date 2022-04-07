import Color_genes
import Energy_bonus_genes
import Gene


class Genome:

    Max_Minerals_bonus = 5
    Max_Berries_bonus = 5
    Max_Creature_bonus = 5
    Min_Minerals_bonus = -5
    Min_Berries_bonus = -5
    Min_Creature_bonus = -5
    Max_Strength = 50
    Colors = Color_genes.ColorGene()
    Bonuses = Energy_bonus_genes.EnergyGenes(Max_Berries_bonus, Max_Minerals_bonus, Max_Creature_bonus, Min_Berries_bonus, Min_Minerals_bonus, Min_Creature_bonus)
    Strength = Gene.Gene(0, 50)
    Start_energy = Gene.Gene(10, 25)

    def __init__(self):
        pass

    def generate(self):
        self.Colors.generate()
        self.Bonuses.generate()
        self.Strength.generate()
        self.Start_energy.generate()

    def mutate(self):
        self.Colors.mutate()
        self.Bonuses.mutate()
        self.Strength.mutate()
        self.Start_energy.mutate()
