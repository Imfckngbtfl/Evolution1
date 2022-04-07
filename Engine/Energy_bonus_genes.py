import Gene


class EnergyGenes:
    def __init__(self, max_berry_bonus, max_mineral_bonus, max_creature_bonus, min_berry_bonus, min_mineral_bonus, min_creature_bonus):
        self.Berry_bonus_gene = Gene.Gene(min_berry_bonus, max_berry_bonus)
        self.Mineral_bonus_gene = Gene.Gene(min_mineral_bonus, max_mineral_bonus)
        self.Creature_bonus_gene = Gene.Gene(min_creature_bonus, max_creature_bonus)

    def generate(self):
        self.Berry_bonus_gene.generate()
        self.Mineral_bonus_gene.generate()
        self.Creature_bonus_gene.generate()

    def mutate(self):
        self.Berry_bonus_gene.mutate()
        self.Mineral_bonus_gene.mutate()
        self.Creature_bonus_gene.mutate()

    def get_energy_bonus_value(self, resource_type):
        if resource_type == 'Berry':
            return self.Berry_bonus_gene.get_value()
        if resource_type == 'Mineral':
            return self.Mineral_bonus_gene.get_value()
        if resource_type == 'Creature':
            return self.Creature_bonus_gene.get_value()
        return None
