from Cities import City
from Cities import Distance
from random import randrange

Cities = []
for i in range(10):
    rand_x = randrange(10)
    rand_y = randrange(10)
    Cities.append(City(rand_x, rand_y))

Distances = []

for i in range(9):
    randDistance = randrange(100)
    Distances.append(Distance(Cities[i], Cities[i+1], randDistance))

#print(Distances[1].city1, Distances[1].city2, Distances[1].distance)

def TSP(Cities, Distances, temp):
