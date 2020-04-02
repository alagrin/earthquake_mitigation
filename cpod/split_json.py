# Splits the Json output from Project Sidewalk API
# Access Attributes API.

import json

fileobj = open("coordinates.json")
data = json.load(fileobj)
resFile = open('res.txt', 'w')
for i in data['features']:
    coordinates = i['geometry'][u'coordinates']
    coordinates = str(coordinates).replace("[", "")
    coordinates = str(coordinates).replace("]", "")
    coordinates = str(coordinates).split(",")
    lon = coordinates[0]
    lat = coordinates[1]
    res = ""
    problem = i['properties'][u'label_type']
    print(problem)
    if (problem == "CurbRamp"):
        res = ",1,0,0,0,0"
    elif (problem == "NoCurbRamp"):
        res = ",0,1,0,0,0"
    elif (problem == "Obstacle"):
        res = ",0,0,1,0,0"
    elif (problem == "SurfaceProblem"):
        res = ",0,0,0,1,0"
    elif (problem == "NoSideWalk"):
        res = ",0,0,0,0,1"

    resFile.write(lon + "," + lat + res)
    resFile.write("\n")

    print(lon + "," + lat + res)
    print("\n")

fileobj.close()
resFile.close()

print("done")
