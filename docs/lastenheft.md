# Lastenheft

## Einführung

Das Projekt handelt um die Verarbeitung von Geodaten, mit Hilfe von einer Punktwolke und den Katasterdaten einer Stadt. Die Andwendung soll über eine Benutzeroberfläche bedienbar und über die Kommandozeile parametrisierbar sein. Das Programm verarbeitet die Punktwolke mit den Katasterdaten und erzeugt für jedes Gebäude eine zugeschnitte Punktwolke.



## Beschreibung des Ist-Zustands

Derzeit muss man mühselig die Katasterdaten und Punktwolken übereinander legen und per Hand zuschneiden. Dieser Vorgang kostet für eine Vielzahl von Gebäuden sehr viel Zeit und Aufwand.



## Beschreibung des Soll-Konzepts

Die Anwendung schneidet automatisch die von den Benutzer zur Verfügung gestellten Katasterdaten und Punktwolken zurecht. Gegebenfalls muss der Benutzer die Katasterdaten manuell über die Benutzerfläche so verschieben, dass diese mit der Punktwolke übereinstimmen. Es resultieren einzelne Punktwolken für jedes Gebäude aus der Punktwolke.



## Beschreibung von Schnittstellen

- Kommandozeile
- Benutzeroberfläche
- Benutzereingabe
  - Katasterdaten
  - Punktwolke
  - Ggf. Verschiebung der Katasterdaten/Punktwolke 



## Funktionale Anforderungen

- Automatisches Ausschneiden von Gebäuden, anhand der Grundrisse
- Entfernen von Objekten, die nicht zu einem Gebäude gehören
- Anbauten, wie zum Beispiel Balkone oder Erker die über den Grundriss hinausragen, nicht entfernen.
- Exportieren von ausgeschnittenen Gebäude in einzelnen Dateien
- Einfache bedienbare graphische Benutzerobferläche zur Visualisierung der Katasterdaten/Punktwolke
- Möglichkeit zur Verschiebung der Katasterdaten/Punktwolke
- Parametrisierbarkeit über Kommandozeile



## Nichtfunktionale Anforderungen
### Benutzbarkeit

Einfache und intuitive Interaktion mit Programm und graphischer Benutzeroberfläche.

### Zuverlässigkeit

Die Präzision des Ausschneidens kann, aufgrund von unvorhergesehenen Umwelteinflüssen und ungenauen Benutzereingaben, variieren. 

Im Falle eines Programmabsturzes soll die manuelle Verschiebung des Benutzers gesichert werden, sodass diese nicht nochmal vorgenommen werden müssen.

### Effizienz

Da das Programm mit großen Dateien arbeitet sollte die ANwendung performant Programmiert sein, damit die Wartezeit nicht zu groß ist.

### Änderbarkeit

Die Anwendung soll eine gut durchdachte Architektur haben. Der Quelltext soll sich an einen gewissen Codestil halten

### Übertragbarkeit

Die Anwendung soll Betriebssystem unabhängig sein.



## Risikoakzeptanz

Showstopper sind zu vermeiden.



## Skizze des Entwicklungszyklus und der Systemarchitektur oder auch ein Struktogramm

tbd.



## Lieferumfang

Das fertige Programm zusammen mit der graphischen Benutzeroberfläche.



## Abnahmekriterien

tbd.

## Branchenspezifikation

-Keine-