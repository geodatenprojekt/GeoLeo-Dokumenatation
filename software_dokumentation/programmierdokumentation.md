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