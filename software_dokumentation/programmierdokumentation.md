# Programmierdokumentation

Die Schnittstellen zur Ein- und Ausgabe von GeoLeo, sowie die verwendeten Dateitypen, wurden bereits [in der Datendokumentation](datendokumentation) beschrieben.
Nun soll im Folgenden ein genauer Blick auf die Programmlogik geworfen werden, indem der Quellcode genauer betrachtet und erläutert wird.

# Kommandozeilenparameter

Die Klasse zur Umsetzung der Kommandozeilenparameter greift zu Beginn, gleich nach dem Starten des Programms.

[An dieser Stelle](benutzerhandbuch?id=auflistung-der-parameter) wurden bereits die verwendeten Parameter und deren Nutzung erklärt. Diese Parameter stellen teilweise auch die in der Klasse verwendeten Variablen dar. Für Hilfe und Version ist es nicht nötig eigene Variablen anzulegen.
```python
def __init__(self):
    self.cadasterPath = None
    self.pointCloudPath = None
    self.outputPath = None
    self.xoffset = 0.0
    self.yoffset = 0.0
```

Danach sollen die in der Kommandozeile eingegebenen Argumente geparsed, also eingelesen und auf Plausibilität überprüft werden. Dazu werden die Argumente registriert, wie hier am Beispiel des Kataster-Arguments:
```python
def parseArguments(self, args):
    parser = argparse.ArgumentParser(prog='Geodatenverarbeitung')
    filehandling = parser.add_argument_group('file handling')
    filehandling.add_argument("-c", "--cadaster", type=self.dir_path, help="path to cadaster directory")
```

Anschließend werden die verarbeiteten Daten in die dafür angelegten  Variablen geschrieben. Wurde für einen Parameter keine Eingabe getätigt, bleibt der Wert auf ``None``. Dieser Vorgang ist hier einmal beispielhaft für das Kataster-Argument dargestellt:
```python
def writeArgs(self):
    args = self.parseArguments(sys.argv[:1])
    if args.cadaster:
        self.cadasterPath = args.cadaster
```

Neben den für die Klasse notwendigen Getter- und Setter-Methoden, auf die hier nicht weiter eingegangen wird, gibt es noch 2 Methoden, die geschrieben wurden, um nicht primitive Eingaben überprüfen zu können. Zum Einen ist das die Methode "dir_path", die überprüft, ob eine Eingabe ein gültiger Pfad ist. 
```python
if os.path.isdir(path):
    return path
else:
    # Kein gültiger Pfad - Error
```
Die anderen Methode ist eine Verfeinerung von "dir_path", weil sie neben der Gültigkeit eines Pfades auch noch prüft, ob dieser beschrieben werden darf. Die Überprüfung wird nun auf den Ausgabepfad angewandt.
```python
if os.path.isdir(path):
    if os.access(path, os.W_OK):
        return path
    else: # Keine Schreibrechte - Error
else: # Kein gültiger Pfad - Error
```

# Front-End

Das Front-End in GeoLeo übernimmt Funktionen in Form von GUI sowie Useranpassungen und die Darstellung der vom Back-End berechneten und gelieferten Daten. Im Folgenden werden die wichtigsten Funktionen im Front-End mit Hilfe von Beschreibungen sowie Code-Snippets genauer erläutert.

## Darstellung

**Koordinaten:**  
Zum Darstellen der Katasterdaten und der Punktwolken wird OpenGL verwendet. OpenGL gibt es auch für Python und wird mit unserem GUI-Toolkit Tkinter [kombiniert](https://github.com/jonwright/pyopengltk).

Um die Punktwolke schön Darzustellen, soll diese etwas skaliert werden. Dafür wird für alle y-Werte die kleinste y-Koordinate abgezogen und anschließend mit dem ``Faktor 1000`` multipliziert. Auf diese Weise fängt die Punktwolke beim y-Wert ``0`` an und kann sinnvoll dargestellt werden.
```python
for y in range(0, 3):
    curr = list[x][y]
    curr -= self.min[y]
    curr = int(curr * 1000)
    inner.append(curr)
```
Weiterhin hat man sich gegen die Verwendung der bereits vorhandenen Koordianten aus einer Punktwolke entschieden, weil es sonst zu Rundungsfehlern kommen kann und eine exakte Darstellung gewährleistet sein soll. Deshalb wurden diese Koordinaten an das Koordinatensystem der Katasterdaten angepasst, um beide Darstellungen im gleichen Format vorliegen zu haben.

**Farbdarstellung:**  
Um die gegebenen Farbwerte aus den Punktwolken in OpenGL korrekt anzeigen zu können, musste eine Umrechnung der Farbwerte vorgenommen werden. Die gegebenen Farbwerte wurden dabei mit dem ``Faktor 1000`` multipliziert, um Zahlen zwischen ``0 und 65536`` zu erhalten. Anschließend konnten diese Farbwerte durch ``65536`` geteilt werden, um in OpenGL die RGB-Werte gemäß nach Spezifikation korrekt setzen zu können.
```python
for y in range(3, 6):
    curr = list[x][y]
    curr += 1000
    curr = int(curr)
    inner.append(curr)
glColor3d(point[3] / 65536, point[4] / 65536, point[5] / 65536)
```

**Anzeige:**  
Um nun die Punktwolken bzw. die Katasterdaten endgültig anzeigen zu können, werden bei der Initialisierung die einzelnen Punkte in eine Displayliste gespeichert. Diese Liste sorgt dafür, dass bei ständigem Wiederholen des Zeichnens eine ausreichende Performanz gegeben ist und hohe FPS-Zahlen erreicht werden. Ohne diese Vorgehensweise würden die FPS auf ``1/20`` der aktuellen zurückgehen.  
Dieses Vorgehen ist hier einmal exemplarisch für die Katasterdaten als Code-Snippet dargestellt:
```python
self.cadlist = glGenLists(1)
glNewList(self.cadlist, GL_COMPILE)
glColor3d(1, 0, 0)
vertices = []

glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    for building in cad.buildings:
        glBegin(GL_POLYGON)
            for coord in building.coordinates:
                x = self.parser.parse_coords(coord._x, coord._y, coord._z)
                glVertex3d(x[0], x[2], x[1])
                vertices.append((x[0], x[2], x[1]))
            glEnd()
        glEndList()
```

# Back-End

Bei der Dokumentation von GeoLeo ist es auch ganz besonders wichtig, dass man sich die implementierten Methoden im Back-End genauer anschaut. Hier findet die tiefere Programmlogik ihren Platz. Daher werden im Folgenden die wichtigsten Abläufe in GeoLeo zur Verarbeitung der [in der Datendokumentation](datendokumentation) vorgestellten Dateien erläutert.

## getLasFilesForBuildings

Vor dem eigentlichen Durchsuchen der Katasterdaten, sollen die Dateien ermittelt werden, die überhaupt im Bereich der Punktwolke liegen. Auf diese Weise wird eine Vorfilterung vorgenommen, um die Effizienz von GeoLeo zu erhöhen. Es werden als Gebäude, die nicht im globalen Bereich liegen, herausgefiltert.
```python
for building in buildings:
    if(maxBounds != None and building.coordinates[0].x <= maxBounds[0] or building.coordinates[0].x >= maxBounds[2] or building.coordinates[0].y <= maxBounds[1] or building.coordinates[0].y >= maxBounds[3]):
        continue
    else: #Füge Gebäude zu buildingsFound hinzu
```

Nun soll über allen Gebäuden alle Punktwolken durchgegangen werden. Dabei werden für jede Punktwolke alle Gebäudepunkte abgefragt, [ob diese innerhalb der Grenzen liegen](methodendokumentation?id=punkt-in-einem-gebäude). Wenn diese Punkte in den Grenzen liegen, dann soll sich das Programm die .las-Datei merken, um sie später verwenden zu können. Hier ist noch einmal wichtig zu erwähnen, dass diese Filterung essentiell ist, um das Programm überhaupt lauffähig zu halten und nicht zu lange auf das Finden von Gebäuden gewartet werden muss.
```python
for lasFile in filePathList:
    ...
    for building in buildingsFound.keys():
        for buildingPoint in building.coordinates:
            if(#Punkt in Punktwolke):
                buildingsFound[building][0][i] = True
                if(#Las Datei noch nicht hinzugefügt):
                    buildingsFound[building][1].append(lasFile)
```

## getLasFilesForFirstBuilding

Weil es für das Front-End nicht zumutbar ist alle Gebäude in Form von Katasterdaten und Punktwolken darzustellen (auch hier vor allem auf Grund von Performanzgründen), wird nun noch eine Methode benötigt, die dem Front-End nicht alle Gebäude zur Verfügung stellt. Dafür wurde die Methode "getLasFilesForFirstBuilding" impklementiert, die das Front-End mit einem exemplarischem Gebäude aus der Punktwolke versorgt, damit dieses dargestellt werden und somit vom Nutzer ggf. der Offset angepasst werden kann.
```python
for building in buildingsFound.keys():
    for lasFile in filePathList:
        ...
        for buildingPoint in building.coordinates:
            ...
    if(#Ganzes Gebäude war wurde in Punktwolken gefunden):
        return {building: buildingsFound[building][1]}
return None
```
Diese Methode macht das gleiche wie ["getLasFilesForBuildings"](programmierdokumentation?id=getlasfilesforbuildings) nur eben mit dem Unterschied, dass nach dem Ersten, komplett gefundenen Gebäude abgebrochen wird, weil ja nur eines benötigt wird.

## preProcessLasFiles

Damit später schnell auf Informationen zugegriffen werden kann, ohne eine Datei immer wieder öffnen zu müssen, wurde die Methode "preProcessLasFiles" geschrieben. Sie speichert für jede Punktwolke die Grenzen der Koordinaten, aber auch global, also für alle Punktwolken, die höchsten bzw. tiefsten Grenzen (Punkte).
```python
for lasFile in filePathList:
    lasFileReader = PointCloudFileIO(util.getPathToFile(lasFile))
    lowestCoords = lasFileReader.getLowestCoords()
    highestCoords = lasFileReader.getHighestCoords()
    ... # Merke global höchste/tiefste Werte
    coordsForPaths[lasFile] = (lowestCoords, highestCoords)
return [globalLowestX, globalLowestY, globalHighestX, globalHighestY, coordsForPaths]
```
## preProcessBuildingList

Für die weitere Verarbeitung wird im Laufe der Gebäudebetrachtungen eine Methode benötigt, die nahe aneinander liegende Punkte zusammenfügt. Denn in den Katasterdaten kann es vorkommen, dass einzelne Gebäudeeinheiten getrennt voneinander dargestellt sind (z.B. Wohnungen), obwohl sie zum gleichen Gebäude gehören. Hier wurde ein Algorithmus entwickelt (["hier erklärt"](methodendokumentation?id=point-close-to-anchor)), der über die gesamte Gebäudeliste geht und nach nahestehenden Punkten sucht. Diese Punkte werden dann zusammengefügt, sodass später mehrere Gebäude mit Hilfe geometrischer Operationen kombiniert werden können. Erwähnenswert ist hier auch eine berücksichtigte Erweiterungsmöglichkeit: der Grenzwert, also ab wann Punkte zusammengefügt werden ("pointLeeway" genannt), kann dynamisch geändert werden.
```python
for building in buildingList:
    for point in building.coordinates:
        ...
        for uniquePoint in uniquePoints:
            if(#Punkt is nahe eines anderen Punkts):
                ... # Erstelle vergleichbare Punkte
                if(shapelyPoint != shapelyUniquePoint and shapelyPoint.distance(shapelyUniquePoint) < pointLeeway):
                    ... # Überschreibe Koordinaten von point mit denen von uniquePoint
        if(#Punkt war nah/gleich eines anderen Punktes):
            ... # Gruppiere Gebäude, die gemeinsame Punkte haben
        else:
            uniquePoints[point] = i # i ist das i-te Gebäude in der Liste
    i += 1
```

## combineBuildingsToGroups

In der Methodendokumentation wurde bereits auf den Algorithmus eingegangen, [der Gebäude zu Gruppen zusammenfasst](methodendokumentation?id=gebäudegruppe-ermitteln).

```python
for building in buildings:
    hadMatchingPoint = False
    foundGroup = False

    for point in building.coordinates:
        if(#Punkt gab es schon in anderem Gebäude):
            ...
            hadMatchingPoint = True
            if(#Gruppe des anderen Gebäudes beinhaltet 'building' noch nicht):
                buildingGroups[otherBuildingIndex].add(building)
                foundGroup = True

        else:
            uniquePoints[point] = i
    if(not hadMatchingPoint):
        buildingGroups[i] = {building}
```
In diesem Schritt werden zunächst alle Gebäude mit gemeinsamen Punkten gruppiert. Dabei stehen Gebäude, die keinen Punkt mit anderen Gebäuden teilen, in einzelnen Gruppen.  
Im nächsten Schritt sollen dann alle gefundenen Gebäude zu einem großen Gebäude zusammengefasst werden. Diese werden dann alle in einer Liste gespeichert und zurückgegeben.
```python
for buildingGroup in buildingGroups:
    if(len(buildingGroup) > 1): #Wenn mehrere Gebäude gemerged werden müssen
        result = combineBuildingGroup(buildingGroup) #Anderer Algorithmus, s.u.
        ... #Abfrage, ob merge funktioniert hat
        combinedBuildings.append(result)
    else:
        combinedBuildings.append(buildingGroup.pop())
return
```

## combineBuildingGroup

Wie in [combineBuildingsToGroups](programmierdokumentation?id=combinebuildingstogroups) bereits zu sehen wird ein Algorithmus genutzt, der alle gefundenen Gruppen zu einzelnen großen Gebäuden zusammenfügt. Dieser Algorithmus soll im Folgenden mit einem Codebeispiel genauer erläutert werden.  
Zuerst werden Polygonen aus allen Gebäuden einer Gebäudegruppe erstellt. Mittels einer geometrischen Operation, in der Bibliothek "Shapely" implementiert, können diese zusammengefügt werden.  
Wenn ein Zusammenfügen nicht möglich ist, werden die Gebäude als Liste wiederzurückgegeben und auf dem aktuellen Stand belassen.  
Wenn das Zusammenfügen hingegen erfolgreich war, entsteht ein größeres Gebäude, das alle Gebäude der Gruppe umschließt.
```python
polygons = []
for building in buildingGroup:
    ... # Erstelle mehrere Polygone aus allen Gebäuden

union = cascaded_union(polygons)
building = cadaster.Building()
if(union.boundary.is_closed == False):
    ... # Zusammenfügen fehlgeschlagen, gibt einzelne Gebäude als Liste zurück
    return buildings
for coord in union.boundary.coords:
    building.coordinates.append(cadaster.Coordinate(coord[0], coord[1], coord[2]))
return building
```

## cutBuildingFromPointcloud

Das Problem um das [tatsächliche Ausschneiden eines Gebäudes aus der Punktwolke](methodendokumentation?id=ausschneiden-eines-gebäudes) wurde bereits auch in der Methodendokumentation erläutert. Dieser Aspekt wird in der Methode "cutBuildingFromPointcloud" implementiert.  
Diese Methode ist sehr komplex und lässt sich daher nicht gut in Teilaspekte gliedern. Aus diesem Grund wird im Folgenden der entwickelte Algorithmus erklärt, gefolgt von einem Code-Snippet, welches die Umsetzung dessen in Python widerspiegelt.  

Als Erstes wird ein Rechteck um das Gebäude herum ausgeschnitten. Diese geschieht [mit Hilfe der schon ermittelten Koordinatengrenzen](programmierdokumentation?id=preprocesslasfiles) und ist daher eine sehr schnelle Operation.  
Im Anschluss können mit der gefilterten Punktwolke die einzelnen Punkte eines Gebäudes herausgefiltert werden. Dafür wird der Algorithmus ["Point-In-Polygon"](methodendokumentation?id=punkt-in-einem-gebäude) verwendet. Diese geometrische Operation ist sehr langsam, weswegen eine Minimierung der Operationen wichtig ist, um die Laufzeit niedrig zu halten. Weiterhin wird von diversen Quellen behauptet, dass Shapely diese Problem nicht performant genüg löst. Hier bieten sich zwei Optimierungen für die Zukunft an:
- Die Polygone werden in Dreiecke aufgeteilt, die die gleiche Fläche abdecken. Es ist sehr leicht und performant zu überprüfen, ob sich ein Punkt in einem Dreieck befindet.
- Eine andere Bibliothek finden: sollte sich eine andere Bibliothek finden lassen, die dieses Problem effizienter löst, würde es sich anbieten, diese an Stelle von "Shapely" zu verwenden.

```python
points = pointCloudReader.getPoints()
writablePoints = pointCloudReader.file.points

poly = Polygon([(point.x, point.y) for point in building.coordinates])

polyExtend = affinity.scale(poly, extendInclude, extendInclude, extendInclude)
polyMaximum = affinity.scale(poly, maximumBoundsExtend, maximumBoundsExtend, maximumBoundsExtend)
... #Hole maximale Bounds 'maxBounds' des Polygons

... #Setze Dateinamen auf Koordinaten des Mittelpunkts des Gebäudes

#Filtert die Punktwolke nach den maximalen Bounds, um die folgende geometrische Operation nicht für alle Punkte der Punktwolke machen zu müssen
selection = (points[:, 0] > minX) & (points[:, 1] > minY) & (points[:, 0] < maxX) & (points[:, 1] < maxY)
writablePoints = writablePoints[selection]
points = points[selection]

selection = []

#Geometrisches Bestimmen, ob die einzelnen Punkte in dem Polygon liegen - Sehr langsam
for point in points:
    shapelyPoint = Point(point[0], point[1])
    if(polyExtend.contains(shapelyPoint)):
        selection.append(True)
    else:
        selection.append(False)

writablePoints = writablePoints[selection]
points = points[selection]

countFiltered = len(writablePoints)

if(countFiltered == 0): #Falls Katasterdaten fehlerhaft waren
    return

pointCloudReader.writeFileToPath("{}/{}".format(saveFolder, filename), points=writablePoints)
```