import Resource.py
import Genome.py
class Creature(Resource):
    def __init__(self, Genome):
        self.Genome = Genome
        self.Energy = Genome.Start_energy.Get_current()
    self.Resource_type = "Creature"
