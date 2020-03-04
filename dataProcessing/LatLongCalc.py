import pandas as pd
import math
import geopy.distance

data = pd.read_csv("AB_NYC_2019.csv");
landmarks = pd.read_csv("lat long of NYC landmarks.csv");

CalculatedDistance = []
currentLandmark = 0
landmarkNames = ["Central Park Zoo", "Times Square", "Wall Street", "Washington Square Park", "World Trade Center",
                 "Statue of Liberty (Battery Park)", "Empire State Building", "Yankee Stadium", "Flatiron Building"]


def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371  # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d


for a, b in zip(landmarks['Lat'], landmarks['Long']):
    for x, y in zip(data['latitude'], data['longitude']):
        CalculatedDistance.append(geopy.distance.vincenty((a, b), (x, y)).miles)
    newColumn = pd.DataFrame(CalculatedDistance)
    data[landmarkNames[currentLandmark]] = newColumn
    CalculatedDistance = []
    currentLandmark = currentLandmark + 1

data.to_csv("AB_NYC_2019_calculated.csv")
