import CadasterReader as CadReader

cad = CadReader.Cadaster()
cad.buildings = CadReader.getBuildingsFromCadaster("ExampleData/LoD1_468_5751_1_NW.gml")
building = cad.buildings[0]

for building in cad.buildings:
    print("========================================")
    print("Building: ")
    print("Coord Count: " + str(len(building.coordinates)))
    for coord in building.coordinates:
        print("Coordinates:  x:" + str(coord.x) + " y: " + str(coord.y) + " z: " + str(coord.z))
