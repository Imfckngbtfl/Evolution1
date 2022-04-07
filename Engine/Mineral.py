import Resource


class Mineral (Resource):

    def __init__(self, resource_energy):
        super().resource_energy = resource_energy
    resource_type = 'Mineral'
    super().collide_type = 'Collide'
