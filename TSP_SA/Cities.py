import math

class City:
    def __init__(self, x_coord, y_coord, name):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.name = name


    def Distance(self, city):
        distance = math.sqrt(((city.x_coord - self.x_coord) ** 2) + ((city.y_coord - self.y_coord) ** 2))
        return distance
