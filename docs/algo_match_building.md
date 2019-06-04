## Algorithmus zur Findung der Punktwolke passend zu einem gegebenen Gebäude
```
eingabe(punktwolkenOrder)
eingabe(building)

punktwolken = []
derzeitigePunktwolke = None

eckpunkte = building.coordinates
for katasterPunkt in eckpunkte:
  //Finde Punktwolke, in der der Punkt enthalten ist

  //Performanz: Speichere die Punktewolke, in der der letzte Eckpunkt des Gebäudes lag
  //Überprüfe diese zuerst, bevor nach einer neuen Punktwolke gesucht wird.
  if derzeitigePunktwolke != None:
    maxCoords = derzeitigePunktwolke.getMaxCoords()
    minCoords = derzeitigePunktwolke.getMinCoords()
    eckpunkt1 = (minCoords.x, minCoords.z)
    eckpunkt2 = (minCoords.x, maxCoords.z)
    eckpunkt3 = (maxCoords.x, minCoords.z)
    eckpunkt4 = (maxCoords.x, maxCoords.z)
    polygon = Polygon([eckpunkt1, eckpunkt2, eckpunkt3, eckpunkt4])
    if polygon.contains(katasterPunkt):
      continue
    else:
      derzeitigePunktwolke = None

  //Falls die Punktwolke gefunden werden muss, iterier über alle Punktwolken
  for punktwolke in punktwolkenOrdner:
    maxCoords = punktwolke.getMaxCoords()
    minCoords = punktwolke.getMinCoords()
    eckpunkt1 = (minCoords.x, minCoords.z)
    eckpunkt2 = (minCoords.x, maxCoords.z)
    eckpunkt3 = (maxCoords.x, minCoords.z)
    eckpunkt4 = (maxCoords.x, maxCoords.z)
    polygon = Polygon([eckpunkt1, eckpunkt2, eckpunkt3, eckpunkt4])
    if polygon.contains(katasterPunkt):
      punktwolken.append(punktwolke)
      derzeitigePunktwolke = punktwolke
      break

return punktwolken
```
