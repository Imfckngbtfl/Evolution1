import Gene


class ColorGene:
    Red = Gene.Gene(0, 255)
    Green = Gene.Gene(0, 255)
    Blue = Gene.Gene(0, 255)

    def generate(self):
        self.Red.generate()
        self.Green.generate()
        self.Blue.generate()

    def mutate(self):
        self.Red.mutate()
        self.Green.mutate()
        self.Blue.mutate()

    def get_color_value (self, color):
        if color == 'Red':
            return self.Red.get_value()
        if color == 'Green':
            return self.Green.get_value()
        if color == 'Blue':
            return self.Blue.get_value()
