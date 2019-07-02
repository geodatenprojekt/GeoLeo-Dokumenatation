# Methodendokumentation

## Allgemeines zur Software

GeoLeo ist eine Software, mit der aus Punktwolken Gebäude ausgeschnitten werden können. Diese Gebäude werden dann einzeln in eine neue Punktwolke gespeichert, eine Datei für ein Gebäude. Damit aus den Punktwolken die einzelnen Gebäude gefiltert werden können, werden Katasterdaten zur Hand genommen, die die Grundrisse der Gebäude beinhalten. Mit Hilfe der Software können schließlich eventuell auftretende Verschiebungen der beiden Koordinatensysteme behoben werden, um ein gründliches Ausschneiden der beiden Gebäude zu gewährleisten. Weiterhin kann die Software auch mit Kommandozeilenparametern gestartet werden, sodass eine Verwendung der GUI nicht zwingend notwendig ist. Im Folgenden wird auf Algorithmen eingegangen, die in GeoLeo verwendet wurden bzw. im Zuge der Entwicklung GeoLeos erarbeitet wurden.

## Punkt in einem Gebäude

Eine Herausforderung im Zuge der Entwicklung war das Ermitteln, ob ein Punkt einer Punktwolke in einem Gebäude der Kadasterdaten liegt und damit in die neu erstelle Punktwolke gehört oder ob der Punkt ignoriert werden kann. Auf Grund der Tatsache, dass der Grundriss eines Gebäude relativ häufig ein Polygon ist, ist die Ermittlung ein aufwändiger Algorithmus - der Ray Casting Algorithmus. Dieses Problem konnte an die Python Bibliothek "Shapely" ausgelagert werden. Shapely greift hier das Probleme "Point-in-Polygon" auf und stellt den Ray Casting Algorithmus zur Verfügung, der es uns ermöglicht die Punkte den Gebäuden zuzuordnen.

## Point close to anchor

Oft ist es nötig Punkte zu finden, die in einem festgelegten Radius zu einem anderen Punkt liegen. Beispielsweise kann auf diese Weise festgestellt werden, ob nahe einem Punkt weitere Punkte liegen, die auch Teil eines Gebäudes sein könnten.
Dieser Algorithmus wurde selbstständig implementiert, indem:
 - von einem Punkt ein Vektor zu einem anderen gespannt wird,
 - über diesen Vektor der Abstand berechnet wird,
 - überprüft wird, ob der ermittelte Abstand in den Bereich des vorgegebenen Maximalabstands fällt,
 - abhängig von der Überprüfung, der Punkt mit aufgenommen wird oder verworfen wird.


 Für die Ausführung des Algorithmus wurde sich grundlegender mathematischer Formeln bedient. Ein Beispiels hierfür ist die Berechnung des Abstands zwischen zwei Punkten:  
 Berechnung des Vektors:  
 ```vec(v) = point(b) - point(a)```  
   
 Länge des Vektors v bestimmen:    
 ```d = sqrt(x² + y² + z²)```


## Zusammenführen mehrerer Punktwolken

Eine weitere Herausforderung war das Zusammenführen mehrerer Punktwolken. Es wurde zuerst gedacht, dass die Punkte aus den Punktwolken in einer neuen Datenstruktur zusammengeführt werden können, indem sie aneinander gehängt werden. Da jede Punktwolke allerdings aus relativen Koordinaten mit eigenem Ursprung besteht, war eine einfache Verkettung nicht möglich. Für die Entwicklung des unten stehenden Algorithmus konnten allerdings Informationen verwendet werden, die in den Headern der Punktwolkedateien stehen. In diesen Headern steht auch der Offset drin, mit dem der Unterschied zum Ursprung berechnet werden kann und somit auch die Punktwolken zusammenführt werden können.

Führe den Algorithmus durch indem:
- eine Punktwolke als Ursprung gewählt wird,
- der Offset über den Header geholt wird,
- für die übrigen Punktwolken der Unterschied des Offsets zum Ursprung berechnet wird,
- zuletzt der Unterschied auf die einzelnen relativen Punktwolkenkoordinaten addiert wird und
- die Punktwolke aneinander gehängt werden.

## Gebäudegruppe ermitteln

Weil in den Katasterdaten verschiedene Wohnungen, die zu einem Haus gehören, als einzelne Einheiten dargestellt werden, müssen Gebäudegruppen ermittelt werden. Diese Gebäudegruppen sind dann entweder einzelne Gebäude, die zuvor auch schon als einzelnes Gebäude definiert waren und somit keiner weiteren Anpassung bedürfen. Oder aber sie sind eine Zusammenführung aus den zuvor erwähnten einzelnen Einheiten zu einem Gebäudekomplex.

Führe folgenden Algorithmus aus:
- laufe über alle Gebäude
- speichere jeden Punkt individuell
- überprüfe, ob ein Punkt schon in einer Gebäudegruppe existiert
 - wenn wahr: füge Punkt an Gebäudegruppe an
 - wenn falsch: lege neue Gebäudegruppe an


## Ausschneiden eines Gebäudes

Nachdem nun alle Gebäude vorliegen, geht es nun darum die einzelnen Punkte einer Punktwolke auf das Vorkommen in einem Gebäude zu testen. Dafür werden bereits schon erklärte Algorithmen benötigt. 

Denn zuerst müssen die verschiedenen Punktwolken zu einer großen zusammenfasst werden, um sinnvoll verarbeitet zu werden. Die erzeugten Gebäudekomplexe sind Polygone, sodass der Algorithmus "Punkt in einem Gebäude" verwendet werden muss. Weiterhin muss der Algorithmus "Point close to anchor" verwendet werden, um festzustellen, ob gewissen Punkte noch zu einem Gebäude gehören, die eventuell leicht außerhalb des Polygons liegen (z.B. könnte es sich hierbei um Balkone o.ä. handeln).

Diese Algorithmen gilt es hier geschickt miteinander zu verbinden. Am Ende kann für jedes Gebäude ein "numpy-Array" erzeugt werden, welches in dem Algorithmus "Erzeugung einer Punktwolke" verwendet wird.

## Erzeugung einer Punktwolke

Das Erzeugen einer Punktwolke ist ein wesentlicher Schritt in der Programmlogik. Es muss nämlich nach dem Ausschneiden eines Gebäudes eine neue Punktwolke für dieses Gebäude erzeugt werden, in der am Ende auch nur dieses Gebäude wiederzufinden ist. Das Gebäude soll schließlich isoliert in einer eigenen Datei wiederzufinden sein.

Nach dem Ausschneiden eines Gebäudes findet sich das Gebäude als Punktwolke als "numpy-Array". "Numpy" ist hierbei eine Pythonbibliothek, genauso wie auch die Bibliothek für .las-Dateien "laspy". In "laspy" kann nun eine neue Datei im Write-Mode geöffnet werden, die zu Anfang ein leeres Punktearray beinhaltet. Dieses leere Punktearray wird im Anschluss durch das "numpy-Array" befüllt, indem dieses der "laspy" zum Schreiben übergeben wird. Danach kann die Datei geschlossen werden und es ist eine neue Punktwolke erstellt worden.

