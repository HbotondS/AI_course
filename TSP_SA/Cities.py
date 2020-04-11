class City:
    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def get_x_coord(self):
        return self.x_coord

    def get_y_coord(self):
        return self.y_coord


class Distance:
    def __init__(self, city1, city2, distance):
        self.city1 = city1
        self.city2 = city2
        self.distance = distance

    def get_city1(self):
        return self.city1

    def get_city2(self):
        return self.city2

    def get_distance(self):
        return self.distance

