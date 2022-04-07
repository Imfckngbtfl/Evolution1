from Berry_spawn_controller import BerrySpawnController
from Mineral_spawn_controller import MineralSpawnController


class SpawnResourceController:
    def __init__(self, berry_resource_energy, mineral_resource_energy):
        self.B = BerrySpawnController(berry_resource_energy)
        self.M = MineralSpawnController(mineral_resource_energy)

    def spawn(self, game_map):
        self.B.spawn(game_map)
        self.M.spawn(game_map)


