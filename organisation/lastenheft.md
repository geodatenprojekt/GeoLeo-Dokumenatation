# Lastenheft

## Einführung

Das Projekt handelt von der Verarbeitung von Geodaten, bestehend aus Punktwolken und Katasterdaten einer Stadt . Die Anwendung soll über eine Benutzeroberfläche bedienbar und über die Kommandozeile parametrisierbar sein. Das Programm verarbeitet die Punktwolke zusammen mit den Katasterdaten und erzeugt für jedes Gebäude eine zugeschnitte Punktwolke.



## Beschreibung des Ist-Zustands

Derzeit muss man mühselig die Katasterdaten und Punktwolken übereinander legen und per Hand zuschneiden. Dieser Vorgang kostet für eine Vielzahl von Gebäuden sehr viel Zeit und Aufwand.



## Beschreibung des Soll-Konzepts

Die Anwendung schneidet automatisch die von dem Benutzer zur Verfügung gestellten Katasterdaten und Punktwolken zurecht. Gegebenfalls muss der Benutzer die Katasterdaten manuell über die Benutzeroberfläche so verschieben, dass diese mit der Punktwolke übereinstimmen. Es resultieren einzelne Punktwolken für jedes Gebäude aus der Punktwolke.



## Beschreibung von Schnittstellen

- Kommandozeile
- Graphische Benutzeroberfläche
- Benutzereingabe
  - Katasterdaten
  - Punktwolke
  - Ggf. Verschiebung der Katasterdaten/Punktwolke 



## Funktionale Anforderungen

- Automatisches Ausschneiden von Gebäuden, anhand der Grundrisse
- Entfernen von Objekten, die nicht zu einem Gebäude gehören
- Anbauten, wie zum Beispiel Balkone oder Erker die über den Grundriss hinausragen, nicht entfernen.
- Exportieren von ausgeschnittenen Gebäude in einzelnen Dateien
- Einfach bedienbare, graphische Benutzerobferläche zur Visualisierung der Katasterdaten/Punktwolke
- Möglichkeit zur Verschiebung der Katasterdaten/Punktwolke
- Parametrisierbarkeit über Kommandozeile



## Nichtfunktionale Anforderungen
### Benutzbarkeit

Einfache und intuitive Interaktion mit Programm und graphischer Benutzeroberfläche.

### Zuverlässigkeit

Die Präzision des Ausschneidens kann, aufgrund von unvorhersehbaren Umwelteinflüssen und ungenauen Benutzereingaben, variieren. 

Im Falle eines Programmabsturzes soll die manuelle Verschiebung des Benutzers gesichert werden, sodass diese nicht nochmal vorgenommen werden muss.

### Effizienz

Da das Programm mit großen Dateien arbeitet, sollte die Anwendung performant programmiert sein, damit die Wartezeit nicht zu groß ist.

### Änderbarkeit

Die Anwendung soll eine strukturierte Architektur haben. Der Quelltext soll sich an einen gewissen Codestil halten.

### Übertragbarkeit

Die Anwendung soll betriebssystemunabhängig sein.


## Risikoakzeptanz

Das Programm richtet sich an professionelle Anwender, nicht an die breite Masse, und soll in normaler Benutzung ohne Fehler laufen.



## Skizze des Entwicklungszyklus und der Systemarchitektur oder auch ein Struktogramm

**Entwicklungszyklus einfaches Kanban**

![](https://i.imgur.com/aNhMioF.png)

**Systemarchitektur**

![](https://i.imgur.com/TiLvNdc.png)



## Lieferumfang

Zwei Programme, dass erste ist die Konsolenanwendung und das zweite mit einer graphische Benutzeroberfläche.


## Abnahmekriterien

- Anpassen des Offsets Katasterdaten oder der Punktwolke
- Genaues auschschneiden der einzelnen Gebäude
- Darstellung der Katasterdaten und Punktwolke
- Einfache Benutzung über die Konsole

## Branchenspezifikation

Keine
