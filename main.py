from modules.board import board
from modules.lights import lights


whiteBoard = board(100, "120x60", "wood", "inside", "black", "green", "whiteboard", 44)
ledLightsBatteries = lights(120, "100x20", "steel", "inside", "white", "batteries", 7000, 1, 44)
ledLightsElectric = lights(90, "100x20", "steel", "inside", "white", "electric", 6000, 3, 55)

furniture = [whiteBoard, ledLightsBatteries, ledLightsElectric]

cheapest = sorted(furniture, key=lambda i: i.price)

for part in cheapest:
    print(part.getDimensions())

