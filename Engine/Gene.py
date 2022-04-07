import random


class Gene:

    def __init__(self, max_value, min_value):
        self.max_value = max_value
        self.min_value = min_value
        self.value = None

    def generate(self):
        rand = random.randint(self.min_value, self.max_value)
        self.value = rand

    def mutate(self):
        rand = random.randint(1, 100)
        if rand <= 10:
            self.generate()

    def get_value(self):
        return self.value
