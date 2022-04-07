from Engine.Berry import Berry
from random import randint


class BerrySpawnController:
    def __init__(self, bre):
        self.berry_resource_energy = bre

    def spawn(self, game_map):
        for cell_row in game_map:
            for cell in cell_row:
                for object in cell:
                    if cell.is_empty_for_berry():
                        rand = randint(1, 100)
                        if rand <= 8:
                            b = Berry(self.berry_resource_energy)
                            cell.set_object(b)
