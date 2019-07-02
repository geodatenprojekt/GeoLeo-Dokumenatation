# Testdokumentation

# Testplan

## Zu testende Komponenten

In dieser Testdokumentation werden folgende Module des GeoLeo Projekts behandelt:

- util
- pointcload
- file_helper
- cmdarguments
- cadaster_reader

Diese Module bieten elementare Funktionen zum Arbeiten mit Punktwolken und Kadasterdaten, die verwendet werden um Häuser aus Punktwolken auszuschneiden.



## Zu testende Funktionalitäten

In der Testdokumentation werden die Funktionalität des Einlesens von Punktwolken, Kadasterdaten und Ordnerstrukturen behandelt. Des Weiteren wird das Auftreten von Fehlerfällen, wie nicht vorhandene Daten oder invalide Eingaben untersucht. Bei auftretenden Fehlern soll eine entsprechende Fehlerbehandlung durchgeführt werden.



## Vorgehen

Die einzelnen Komponenten der Software werden mithilfe von Unittest getestet, dabei werden Dummydaten erstellt und mit den Rückgabewerten der Funktionen verglichen. Oder aber es werden gezielt Exceptiones provoziert.

## Testumgebung

Zum Testen der Software wird Unittest von Python verwendet. Dazu wird für jedes Modul eine eigene Testklasse erstellt, in der die jeweiligen Funktionen getestet werden. Zudem werden alle Testklassen in einer Testsuite zusammengefasst.



# Testskript

## Testziel

Ziel diese Testskripts ist es alle unten genannten Tests durchzuführen und eine Rückmeldung über alle erfolgreichen und fehlgeschlagenen Tests in der Kommandozeile zu erhalten.

## Spezielle Anforderungen

Das Testskript startet alle Tests aus dem Testordner und sollte daher im root-Verzeichnis liegen, da sonst die angegebenen Pfade nicht mehr stimmen.

## Testablauf

Während der Testdurchführung muss kein Eingriff erfolgen. Wenn die Tests durchgelaufen sind, kann in der Kommandozeile entnommen werden, wie viele Tests erfolgreich abgeschlossen wurden und welche Tests nicht erfolgreich abgeschlossen wurden. Bei den Tests, die nicht erfolgreich abgeschlossen wurden, kann entnommen werden, warum sie nicht erfolgreich waren und was sie testen, um den Fehler leichter ausfindig machen zu können.



# Testfälle

## Get all path to file none file

In diesem Testfall, wird die Methode "getPathToFile" aus dem Modul "Util" getestet. Dabei wird der Methode "None" als Parameter übergeben und als Rückgabewert "None" erwartet.

```python
def test_get_path_to_file_none_file(self):
    self.assertEqual(None, util.getPathToFile(None))
```





## Get path relativ to root none file

Wie im [Testfall 3.1](testdokumentation?id=get-all-path-to-file-none-file) wird der Methode "getPathRelativToRoot" in dem Modul "Util" ein "None" als Parameter übergeben und ein "None" als Rückgabewert erwartet.

```python
def test_get_path_relative_to_root_none_file(self):
	self.assertEqual(None, util.getPathRelativeToRoot(None))
```





## Get points close to anchor

Die Methode ["getPointsCloseToAnchor"](methodendokumentation?id=point-close-to-anchor) in dem Modul "Util" wird mithilfe von drei Testmethoden getestet.

In der ersten Methode werden verschiedene Punkte erstellt, die alle denselben ``y Wert (y=3)`` haben, aber verschiedene x und z Werte. Wobei ``x = 0<x<4`` ist und ``z = 4<z<8`` ist. Die Punkte werden zusammen mit dem Ankerpunkt und der Distanz der Funktion übergeben. Der Rückgabewert sollte eine Liste sein, die für jeden Punkt ein "True" enthält, da alle Punkte nicht weiter als ``3`` vom Ankerpunkt entfernt sind.

```python
def test_get_points_close_to_anchor_in_range(self):
	points = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
	anchor = [1, 3, 5]
	distance = 3
	numpy_arr = np.vstack(points)
	assert_list = [True, True, True, True, True, True, True, True, True]
	close_list = util.getPointsCloseToAnchor(anchor, numpy_arr, distance)
	for i in range(len(assert_list)):
		self.assertEqual(assert_list[i], close_list[i])
```



Die zweite Methode ist wie die Erste aufgebaut, nur dass ein Punkt nicht in den x und z Definitionen liegt. Aufgrund dessen sollte in der Rückgabeliste für den 4. Punkt ein "False" stehen.

```python
def test_get_points_close_to_anchor_not_in_range(self):
	points = [p1, p2, p3, p4, p5, p6, p7, p8, p9]
	anchor = [1, 3, 5]
	distance = 3
	numpy_arr = np.vstack(points)
	assert_list = [True, True, True, False, True, True, True, True, True]
	close_list = util.getPointsCloseToAnchor(anchor, numpy_arr, distance)
	for i in range(len(assert_list)):
		self.assertEqual(assert_list[i], close_list[i])
```



In der letzten Methode, wird der Funktion ein negativer Wert für die Distanz vom Ankerpunkt gegeben. Da es in der Geometrie keine negativen Längen gibt, sollte die Funktion ein "None" zurückgeben.

```python
def test_getPointsCloseToAnchor_Find_negative_range(self):
        """Test the method "get points close to anchor" withe an negativ integer as distance"""
        """coords"""
        b1 = np.array([5, 8, 3]).reshape(3)
        b2 = np.array([1, 0, 3]).reshape(3)
        b3 = np.array([6, 1, 2]).reshape(3)
        b4 = np.array([1, 3, 2]).reshape(3)
        b5 = np.array([5, 2, 5]).reshape(3)
        """all coords"""
        points = [b1, b2, b3, b4, b5]
        numpy_arr = np.vstack(points)
        """anchor cord"""
        anchor = [5, 8, 4]
        distance = -3
        close_list = util.getPointsCloseToAnchor(anchor, numpy_arr, distance)
        self.assertEqual(None, close_list)

```





## Unzip Lazfile

Die Methode "unzipLAZFile" in dem Modul "Util" wird mithilfe dieser Testmethode getestet. Dafür wird der Methode eine vorhandene .laz Datei gegeben und anschließend geprüft, ob es eine .las Datei mit dem selben Namen gibt.

```python
def test_unzip_LAZFILE(self):
	if os.path.exists("example_data/pointcloud_examples/47078_575411_0011.las"):
	os.remove("example_data/pointcloud_examples/47078_575411_0011.las")
	util.unzipLAZFile("example_data/pointcloud_examples/47078_575411_0011.laz")
	self.assertTrue(os.path.exists(
        "example_data/pointcloud_examples/47078_575411_0011.las"))
```

Rückgabelose Funktionen haben keine Möglichkeit dem Benutzer der Funktion bei falscher Benutzung eine Rückmeldung durch den Rückgabewert zu liefern. Aus diesem Grund muss die Funktion den Benutzer auf Fehlbenutzung hinweisen. Da dies am besten durch Exceptiones durchgeführt wird, müssen mit dem Fehler entsprechende Exceptiones geworfen werden.





## Point cloud file io

In der Klasse "PointCloadFileIO" gibt es zwei Methoden die getestet werden.

Zum einem wird die Methode "readFile" getestet. Dort wird der Methode ein nicht existierender Pfad übergeben und ein "OSError" erwartet.

```python
def test_point_cloud_file_io_read_file_no_file(self):
	with self.assertRaises(OSError):
	pointcloud.PointCloudFileIO("No File")
```



Die zweite Methode ist "writeFile". Zum Testen dieser Methode wird der Methode der Pfad zu einer .laz Datei übergeben und anschließend überprüft, ob es in diesem Verzeichnis eine .las Datei mit dem selben Namen gibt. Anschließend wird die .las Datei wieder gelöscht.

```python
def test_point_cloud_file_io_writefile(self):
	point_cloud = pointcloud.PointCloudFileIO(
							"example_data/pointcloud_examples/47078_575411_0011.laz")
    point_cloud.writeFileToPath("example_data/pointcloud_examples/test.las")
    self.assertTrue(os.path.isfile("example_data/pointcloud_examples/test.las"))
    os.remove("example_data/pointcloud_examples/test.las")
```





## File helper

Die Methode "get_all_paths_from_dir" in dem Modul "file_helper" wird mithilfe von 3 Methoden getestet.

Im ersten Test wird der Methode "None" als Pfad übergeben und ein "None" als Rückgabewert erwartet.

```python
def test_get_all_paths_from_dir_none__path(self):
	self.assertEqual(None, file_helper.get_all_paths_from_dir(None))
```

In dem zweiten Test wird ein Verzeichnis "test" und  zwei Dateien in dem Verzeichnis erstellt. Anschließend wird "test" als Parameter an die Methode übergeben. Als Rückgabewert wird eine Liste mit allen Dateien im Ordner Test erwartet.

```python
def test_get_all_paths_from_dir_ReadAllFiles(self):
	os.mkdir("test")
	file_path_list = ["test\\test1", "test\\test2"]
	file1 = open(file_path_list[0], "w")
	file1.close()
	file2 = open(file_path_list[1], "w")
	file2.close()

	path_list = file_helper.get_all_paths_from_dir("test")
	shutil.rmtree("./test")
	self.assertEqual(file_path_list, path_list)
```

Im dritten Testfall wird ein nicht existierender Pfad angegeben und "None" als Rückgabewert erwartet.

```python
def test_get_all_paths_from_dir_not_valid_path(self):
	self.assertEqual(None, file_helper.get_all_paths_from_dir("None"))
```





## Get Coordinates

Für die Methode "get_coordinates" in dem Modul "cadaster_reader" gibt es 3 Testfälle.

Der erste Testfall prüft, ob der Rückgabewert "None" ist, wenn der Methode "None" als Parameter übergeben wird.

```python
def test_get_coordinates_none_points(self):
	self.assertEqual(None, cadaster.get_coordinates(None))
```

Im zweiten Testfall wird ein valider Punkt angegeben mit Werten, im Bereich -3000 bis 3000, als eine Liste von Strings. Als Rückgabewert wird ein Objekt von Coordinates erwartet und den x, y und z Attributen äquivalent zur übergebenen Liste.

```python
def test_get_coordinates_valid_point(self):
        x = "5"
        y = "2999"
        z = "-2999"
        point_list = [x, y, z]
        self.assertEqual(5.0, cadaster.get_coordinates(point_list)[0].x)
        self.assertEqual(3000.0, cadaster.get_coordinates(point_list)[0].y)
        self.assertEqual(-3451.0, cadaster.get_coordinates(point_list)[0].z)
```

In dem letzten Testfall wird eine ungültige Liste mit nur zwei Werten übergeben und ein "ValueError" erwartet.

```python
def test_get_coordinates_not_valid_point(self):
        x = "4"
        y = "5"
        point_list = [x, y]
        with self.assertRaises(ValueError):
            cadaster.get_coordinates(point_list)
```





## Get buildings und get xml element

Den beiden Methoden, "get_building" und "get_xml_element" in dem Modul "cadaster_reader" wird "None" als Parameter übergeben und ein "None" als Rückgabewert erwartet.

```python
def test_get_buildings_none_dir(self):      
	self.assertEqual(None, cadaster.get_buildings(None))

def test_get_xml_element_None_para(self):
	self.assertEqual(None, cadaster.get_xml_element(None, None))
```





## Parameters

Die Klasse "Parameters" in dem Modul "cmdargs" kann die übergebenen Argumente beim Aufruf der Software über die Kommandozeile verarbeiten. Die Testklasse "TestCmdArguments" testet dabei das Einlesen jedes Arguments. Insgesamt gibt es 10 Tests, die alle gleich aufgebaut sind. Das Argument wird in die sys.argv übergeben und anschließend wird der Wert mit der getMethode abgefragt.

```python
def test_parameters_point_cloud_path_short(self):
    sys.argv.append("-p")
    sys.argv.append("example_data")
    para = cmdargs.Parameters()
	self.assertEqual(para.getPointCloudPath(),"example_data")
```