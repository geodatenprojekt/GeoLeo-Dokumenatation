# Installationsdokumentation

## Voraussetzungen

Man benötigt folgende Programme um GeoLeo zu installieren:
* [git](https://git-scm.com)
* [Python 3.6](https://python.org) oder höher
* [OSGeo4W](https://trac.osgeo.org/osgeo4w/) (Oder die Installation von `shapely` und `laspy` über wheels mit eingebundenem GEOS)

## GeoLeo Herunterladen

Das Projekt kann von GitHub via dem git Kommando `git clone https://github.com/geodatenprojekt/GeoLeo` heruntergeladen werden

## Benötige Bibliotheken

GeoLeo benötigt einige Python Bibliotheken, die via `pip` herunterladbar sind. Folgende Bibliotheken sind benötig:
* argparse
* laspy [wheel](https://pypi.org/project/laspy/#files)
* shapely [wheel](https://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely)
* numpy
* tkinter
* PyOpenGL

Mit dem Kommando `pip3 install <package>` werden diese Heruntergeladen
