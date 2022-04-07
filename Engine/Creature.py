import Resource


class Creature(Resource):

    def __init__(self, genome):
        self.genome = genome
        self.energy = genome.Start_energy.get_value()
    super().collide_type = 'Collide'
    resource_type = "Creature"

    def play(self):
        action, place = "Move", "f"  # затычка, чтобы работало
        # обращается к нейронке и возвращает действие и клетку, к которой это действие применяется
        return action, place


        
