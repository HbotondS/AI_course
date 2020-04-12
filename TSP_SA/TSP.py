from cmath import exp

from Cities import City
from Cities import Distance
from random import randrange, random

Cities = []
for i in range(10):
    rand_x = randrange(10)
    rand_y = randrange(10)
    Cities.append(City(rand_x, rand_y))

Distances = []

for i in range(9):
    randDistance = randrange(100)
    Distances.append(Distance(Cities[i], Cities[i+1], randDistance))

# print(Distances[1].city1, Distances[1].city2, Distances[1].distance)


class SimulatedAnnealing:
    def __init__(self, temperature, currentRoute):
        self.temperature = temperature;
        self.currentRoute = currentRoute;

    def findRoute(self, temperature, currentRoute):
        shortestRoute = new Route(currentRoute)
        while(temperature > 0.99):
            adjacentRoute = obtainAdjacentRoute(new Route(currentRoute))
            if(currentRoute.getTotalDistance() < shortestRoute.getTotalDistance()):
                shortestRoute = new Route(currentRoute)
            if(acceptRoute(currentRoute.getTotalDistance(), adjacentRoute.getTotalDistance(), temperature)):
                currentRoute = new Route(adjacentRoute)
            temperature = temperature * 1-0.005
        return shortestRoute

    def acceptRoute(self, currentDistance, adjacentDistance, temperature):
        shorterDistance = True
        acceptRouteFlag = False
        acceptanceProbability = 1.0
        if(adjacentDistance >= currentDistance):
            acceptanceProbability = exp(-(adjacentDistance - currentDistance) / temperature)
            shorterDistance = False
        randomNumb = random()
        if(acceptanceProbability >= randomNumb):
            acceptRouteFlag = True
        if(shorterDistance):
            decision = "proceed"
        elif(acceptRouteFlag):
            decision = "proceed"
        else:
            decision = "stay"
        return acceptRouteFlag

    def obtainAdjacentRoute(self, route):
        x1 = 0
        x2 = 0
        while x1 == x2:
            x1 = route.getCities().size() * random()
            x2 = route.getCities().size() * random()
        city1 = route.getCities().get(x1)
        city2 = route.getCities().get(x2)
        route.getCities().set(x2, city1)
        route.getCities().set(x1, city2)
        return route