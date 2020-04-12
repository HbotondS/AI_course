class Path:
    def __init__(self, path):
        #print(path)
        self.cities = path[:]


    def calcPathDist(self):
        dist = 0
        nrCities = len(self.cities)
        for i in range(nrCities - 1):
            dist += self.cities[i].Distance(self.cities[i+1])

        dist += self.cities[nrCities - 2].Distance(self.cities[nrCities - 1])

        return dist

        
    def cities_size(self):
        return len(self.cities)
