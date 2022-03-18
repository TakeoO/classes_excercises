from modules.furniture import furniture

class board(furniture):
    def __init__(self, price, dimensions, material, usage, color, drawing_surface, type, ip=55, ):
        super().__init__(price, dimensions, material, usage, color, ip)
        self.drawing_surface = drawing_surface
        self.type = type

    def isElectrical(self):
        return self.type == 'electrical'

