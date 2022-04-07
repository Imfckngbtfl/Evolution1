from Engine.Mineral import Mineral
from random import randint


class MineralSpawnController:
    def __init__(self, mre):
        self.mineral_resource_energy = mre

    def spawn(self, game_map):
        for cell_row in game_map:
            for cell in cell_row:
                for object in cell:
                    if cell.is_empty_for_mineral():
                        rand = randint(1, 100)
                        if rand <= 15:
                            m = Mineral(self.mineral_resource_energy)
                            cell.set_object(m)
