from modules.furniture import furniture


class lights(furniture):
    def __init__(self, price, dimensions, material, usage, color, energy_source, lumen, number_of_bulbs, ip=55):
        super().__init__(price, dimensions, material, usage, color, ip)
        self.number_of_bulbs = number_of_bulbs
        self.lumen = lumen
        self.energy_source = energy_source

    def isWormLight(self):
        return self.lumen < 6500

    def needsBateries(self):
        return self.energy_source == 'batteries'

