from Engine import Resource
from Engine import Creature


class EatController:

    def get_food(self, creature, cell):
        for food in cell:
            if type(food) == Resource:
                if type(food) == Creature:
                    if food.stength <= creature.strength:
                        return food
                else:
                    return food
        return None

    def eat(self, creature, food_cell):
        food = self.get_food(creature, food_cell)
        if food is not None:
            creature.energy += food.resource_energy + creature.EnergyGene.get_energy_bonus_value(food.resource_type)
            food_cell.remove_object(food)

