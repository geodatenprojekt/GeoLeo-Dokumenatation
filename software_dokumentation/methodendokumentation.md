# Methodendokumentation

## Allgemeines zur Software

GeoLeo ist eine Software, mit der aus Punktwolken Gebäude ausgeschnitten werden können. Diese Gebäude werden dann einzeln in eine neue Punktwolke gespeichert, eine Datei für ein Gebäude. Damit aus den Punktwolken die einzelnen Gebäude gefiltert werden können, werden Katasterdaten zur Hand genommen, die die Grundrisse der Gebäude beinhalten. Mit Hilfe der Software können schließlich eventuell auftretende Verschiebungen der beiden Koordinatensysteme behoben werden, um ein gründliches Ausschneiden der beiden Gebäude zu gewährleisten. Weiterhin kann die Software auch mit Kommandozeilenparametern gestartet werden, sodass eine Verwendung der GUI nicht zwingend notwendig ist. Im Folgenden wird auf Algorithmen eingegangen, die in GeoLeo verwendet wurden bzw. im Zuge der Entwicklung GeoLeos entwickelt wurden.

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

## Erzeugung einer Punktwolke

## Ausschneiden eines Gebäudes

## Punktwolken eines Gebäudes finden

## Gebäudegruppe ermitteln