# Datendokumentation

# LAS-Dateien
Im Zuge des Projekts GeoLeo werden zwei verschiedene Dateitypen benötigt, die von der Software verarbeitet werden. Einer diesen Typen ist der .las Dateityp.

**LAS und LIDAR:**  
Eine LAS-Datei ist ein Standard zum Speichern von luftgestützten LIDAR-Daten. LIDAR steht hierbei für Ligh Detection and Ranging, was eine optische Fernkundungstechnik ist, bei der durch Laserlicht die Erdoberfläche abgetastet wird und somit sehr genaue X-, Y- und Z-Messwerte ermittelt werden können. Dabei werden Punktwolken erzeugt, die als Teil der Daten in der .las-Datei gespeichert werden.

**Weitere Daten:**  
Neben den Koordinaten der einzelnen Punkte stellt eine .las-Datei noch weitere Informationen bereit. Diese werden werden für GeoLeo nur eingeschränkt benötigt, werden hier aber im Interesse der Vollständigkeit erwähnt. Solche Informationen sind einerseits Informationen zur Messung selbst:
- Laserzeitraum
- Laserabtastwinkel
- GPS-Position des Messungsgerätes

Andererseits auch Informationen zu den einzelnen Punkten:
- Intensität
- Punktklassifizierung
- RGB

*Einbezogene Quellen:*
- *http://desktop.arcgis.com/de/arcmap/10.3/manage-data/las-dataset/what-is-lidar-data-.htm [Zugriff: 12.06.2019]*
- *http://desktop.arcgis.com/de/arcmap/10.3/manage-data/las-dataset/what-is-a-las-dataset-.htm [Zugriff: 12.06.2019]*

# GML-Dateien
Neben den verwendeten .las-Dateien, tritt der zweite Dateityp in Form von .gml-Dateien auf. Diese Dateien beinhalten die Katasterdaten der einzelnen Gebäude, die später über die Punktwolke gelegt werden sollen.

**Geography Markup Language:**  
Die Endung .gml steht für Geography Markup Language, die eine XML-Grammatik beinhaltet, die von dem OGC (Open Geospatial Consortium) definiert wurde.
GML ermöglicht hierbei die Bereitstellung von Geodaten in Form von Objekten (in unserem Fall Gebäude) mit Attributen, Relationen und der entsprechenden Geometrie. In GeoLeo werden dabei ``LoD 1-Dateien`` verwendet.

**Dateiinhalt:**  
Eine GML-Datei stellt dabei verschiedene Attribute bereit, die nicht alle von GeoLeo benötigt werden, aber im Interesse der Vollständigkeit trotzdem dargelegt werden sollen:
- Objekt
- Geometrie
- Koordinaten(referenz)system
- Maßeinheit
- Gestaltungsregeln für die Kartendarstellung
- Eventuelle Überdeckung von geographischen Abbildungen


*Einbezogene Quellen:*
- *https://en.wikipedia.org/wiki/Geography_Markup_Language [Zugriff: 12.06.2019]*


# LAS-Eingabe/Ausgabe
GeoLeo soll sowohl eine Schnittstelle zum Einlesen von .las-Dateien bereitstellen als auch eine Schnittstelle, die .las-Dateien nach dem Ausschneiden der Gebäude erzeugen kann bzw. speichert. Diese Anforderung wird in der Klasse ```class PointCloudFileIO:``` umgesetzt.
Sie kapselt das Lesen und Schreiben bzw. den Zugriff auf .laz(komprimierte .las-Dateien) und .las ab. Die Klasse ist also in der Lage sowohl .laz als auch .las-Dateien einzulesen. Jedoch werden .laz-Dateien vor der Verarbeitung dekomprimiert. Weiterhin schreibt die Klasse nur .las-Dateien.

**Klassenattribute:**  
Folgende Klassenattribute werden genutzt, um eine .las-Datei zu öffnen und zu bearbeiten. Es wird der Pfad, die geöffnete Datei und die enthaltenen Punkte gespeichert.
```python
self.path = path
self.file = None
self.points = None
```

## Eingabe
Das Einlesen findet in der Methode "readFile" statt. Wenn im Folgenden von File oder Datei gesprochen wird, handelt sich auf Grund der Nutzung von "laspy.file" automatisch um eine .las-Datei.

Sollte die Datei eine .laz sein, wird sie dekomprimiert:
```python
if(self.path.endswith(".laz")):
    util.unzipLAZFile(self.path)
    self.path = ".laz".join(self.path.split(".laz")[0:-1]) + ".las"
```

Danach wird sie in jedem Fall zur weiteren Bearbeitung geöffnet:
```python
self.file = File(self.path, mode='r')
```

## Ausgabe
Das Schreiben findet in der Methode "writeFileToPath" statt, die einen Pfad zur Ausgabe und ein Numpy-Array der Punkte erwartet, die gespeichert werden sollen.

Es wird eine neue Datei im Schreibmodus erzeugt, die den Header der ursprünglichen .las-Datei übernimmt.
Danach werden die Punkte gemäß laspy-File Spezifikation in die Datei geschrieben, wodurch die Punkte wolke nun in der Datei existiert. Abschließend muss die Datei nur noch geschlossen und somit gespeichert werden.

```python
outFile = File(path, mode='w', header=self.file.header)
outFile.points = points
outFile.close()
```

## Kombinieren von Punktwolken
Eine letzte wichtig zu erwähnende Methode in der Klasse PointCloudFileIO ist "mergePointClouds".
Daneben gibt es noch andere Methoden in der Klasse, die aber nur Getter- bzw. Setter-Funktionen dienen wobei Informationen in die Klasse geschrieben werden oder aus dem Header der Datei ausgelesen werden.

Der hier verwendete Algorithmus wurde bereits [in der Methodendokumentation](methodendokumentation?id=zusammenf%c3%bchren-mehrerer-punktwolken) beschrieben.

Algorithmus:
- Eine Punktwolke wird als Ursprung gewählt:
> Der Ursprung ist die Instanz, in der wir uns befinden.
- Der Offset wird über den Header geholt:
```python
thisOffset = self.file.header.get_offset()
```
- Für die übrigen Punktwolken wird der Unterschied des Offsets zum Ursprung berechnet (in einer for-Schleife):
```python
otherReader = PointCloudFileIO(listPaths[i])
otherOffset = otherReader.file.header.get_offset()
translate = [otherOffset[0] - thisOffset[0], otherOffset[1] - thisOffset[1], otherOffset[2] - thisOffset[2]]
translate[0] *= 1000
translate[1] *= 1000
translate[2] *= 1000
```
- Zuletzt wird der Unterschied auf die einzelnen relativen Punktwolkenkoordinaten addiert und die Punktwolken aneinander gehängt:
```python  
realCoords[0] = np.append(realCoords[0], otherReader.file.X + round(translate[0]))
realCoords[1] = np.append(realCoords[1], otherReader.file.Y + round(translate[1]))
realCoords[2] = np.append(realCoords[2], otherReader.file.Z + round(translate[2]))
pointsCombined = np.append(pointsCombined, otherReader.file.points)
outFile = File(newPath, mode='w', header=self.file.header)
outFile.points = pointsCombined
outFile.X = realCoords[0]
outFile.Y = realCoords[1]
outFile.Z = realCoords[2]
outFile.close()
```


# GML-Eingabe
GeoLeo soll neben der Verwendung von .las-Dateien für die Daten der Punktwolken auch eine Schnittstelle zum Einlesen der Katasterdaten bereitstellen, damit die Punktwolken anhand der Katasterdaten ausgeschnitten werden können. Dabei geht es nur um das Einlesen der Katasterdaten, nicht aber um das Ausgeben, weil das Produkt der Software nur Punktwolken als Daten beinhaltet und die Katasterdaten nur zur Findung dienen.

Zur Umsetzung dieser Anforderung dienen drei verschiedene Klassen:
```python
class Cadaster:
class Coordinate:
class Building:
```
>Die Klasse "Cadaster" ist eine Struktur zum Speichern von Gebäuden.  

>Die Klasse "Building" ist eine Struktur zum Speichern von Koordinaten, die zu einem Gebäude gehören. 

>Die Klasse "Coordinate" setzt eine Koordinate um. Die Klassenvariablen sind somit ``x``, ``y`` und ``z``. Es werden die Methoden ``__eq__`` und ``__hash__`` überladen, damit die Koordinaten vernünftig auf Gleichheit geprüft werden können und damit eine Koordinate als Key in einer HashMap genutzt werden kann.

```python
def __eq__(self, other):
    return self.x == other.x and self.y == other.y and self.z == other.z
def __hash__(self):
    return self.x.__hash__() + 7 * self.y.__hash__()
```

## Eingabe

Das Einlesen einer .gml-Datei erfolgt mit Hilfe von drei verschiedenen Methoden. Die Hauptmethode hierfür ist die Methode "getBuildings", die jeweils die Methoden "getBuilding" und "getXML_Element" aufruft.

Zuerst musst die Datei geöffnet werden und aus der XML-Struktur das Wurzelelement erhalten werden.
```python
tree = ET.parse(fileName)
root = tree.getroot()
```
Danach wird mittels einer for-Schleife nach "cityObjectMember" gesucht. Da so ein "CityObjectMember" aber nicht unbedingt ein Gebäude sein muss, sondern irgendein Objekt in der Stadt, wird mit Hilfe der Methode ``getXML_Element(elems, xml_elem)`` nach einem Gebäude gefiltert. 
```python
xml_elem = xml_elem.find(elems[0])
if len(elems) > 1:
    elems.pop(0)
    xml_elem = getXML_Element(elems, xml_elem)
    return xml_elem
```
Aus dem XML-Objekt können nun die Punkte entnommen werden. Aus diesen Punkten gilt es nun noch ein Gebäude gemäß unserer Klassendefinition für ein Gebäude mit Koordinaten zu erstellen und dies in die Liste aller Gebäude einzutragen.
Das erstellen eines Gebäudes passiert in ``getBuilding(points)``:  
 ```python
building = cadaster.Building()
building.coordinates = list()
for counter in range(0, len(points)):
    coord = (counter + 1) % 3
    if coord == 1:
        x = float(points[counter])
    elif coord == 2:
        y = float(points[counter])
    elif coord == 0:
        z = float(points[counter])
        coord = cadaster.Coordinate(x, y, z)
        building.coordinates.append(coord)
 ```
Das Anfügen an die Liste passiert als letzter Schritt in der beschriebenen Hauptmethode zum Einlesen mit folgendem Schritt: ``buildings.append(building)``.

Somit wären nun auch die Katasterdaten neben den Daten zur Punktwolke eingelesen.