import Resource


class Berry (Resource):
    def __init__(self, resource_energy):
        super().resource_energy = resource_energy
    resource_type = 'Berry'
    super().collide_type = 'Collide'
