from cmath import exp
from Cities import City
from Path import Path
from random import randrange, random


class SimulatedAnnealing:
    def __init__(self, temperature):
        self.min_temperature = temperature
        self.min_temperature = 0.99
        self.rate_of_cooling = 0.005


    def findRoute(self, temperature, currentRoute):
        shortestRoute = Path(currentRoute)
        CurrentRoute = Path(currentRoute)
        while(temperature > self.min_temperature):
            for city in CurrentRoute.cities:
                print(city.name, end=" ")

            print()
            print(CurrentRoute.calcPathDist())

            if(type(currentRoute) == list):
                adjacentRoute = self.obtainAdjacentRoute(Path(currentRoute))
            else: adjacentRoute = self.obtainAdjacentRoute(Path(currentRoute.cities))
            if(CurrentRoute.calcPathDist() < shortestRoute.calcPathDist()):
                shortestRoute = Path(currentRoute)
            if(self.acceptRoute(CurrentRoute.calcPathDist(), adjacentRoute.calcPathDist(), temperature)):
                CurrentRoute = Path(adjacentRoute.cities)
            temperature = temperature * (1 - self.rate_of_cooling)
        return shortestRoute

    def acceptRoute(self, currentDistance, adjacentDistance, temperature):
        shorterDistance = True
        acceptRouteFlag = False
        acceptanceProbability = 1.0
        if(adjacentDistance >= currentDistance):
            acceptanceProbability = exp(-(adjacentDistance - currentDistance) / temperature)
            shorterDistance = False
        randomNumb = random()
        if(acceptanceProbability.real >= randomNumb):
            acceptRouteFlag = True
        return acceptRouteFlag

    def obtainAdjacentRoute(self, route):
        x1 = 0
        x2 = 0
        while x1 == x2:
            x1 = int(route.cities_size() * random())
            x2 = int(route.cities_size() * random())
        city1 = route.cities[x1]
        city2 = route.cities[x2]
        route.cities[x2] = city1
        route.cities[x1] = city2

        return route


if __name__ == "__main__":
    Cities = []

    Cities.append(City(423, 0, "Marosvasarhely"))
    Cities.append(City(1, 8, "Bukarest"))
    Cities.append(City(11, 15, "Kolozsvar"))
    Cities.append(City(0, 3, "Szeben"))
    Cities.append(City(135, 11, "Csikszereda"))
    Cities.append(City(0, 18, "Katmandu"))
    Cities.append(City(312, 42, "Roma"))
    Cities.append(City(63, 14, "Budapest"))

    Annealing = SimulatedAnnealing(999)

    Annealing.findRoute(999, Cities)
