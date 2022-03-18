class furniture:
    def __init__(self, price, dimensions, material, usage, color, ip=55):
        self.price = price
        self.dimensions = dimensions
        self.material = material
        self.usage = usage
        self.color = color
        self.ip = ip

    def calculatePriceWithVAT(self):
        return self.price * 1.22

    def isForOutsideUsage(self):
        return self.ip >= 55

    def getDimensions(self):
        width, height = self.dimensions.split("x")
        return float(width), float(height)