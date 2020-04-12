class Path:
    def __init__(self, path=None):
        if path is not None:
            self.cities = path.cities
        else:
            self.cities = []
    

    def calcPathDist(self):
        dist = 0
        nrCities = len(self.cities)
        for i in range(nrCities - 1):
            dist += self.cities[i].Dist(self.cities[i+1])
        
        return dist += self.cities[nrCities - 2].Distance(self.cities[nrCities - 1])

        

    

    
