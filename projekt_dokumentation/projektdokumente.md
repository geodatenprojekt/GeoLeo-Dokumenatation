# Projektdokumente

## Klassendiagramm
![Klassendiagrammn](/include/klassendiagramm.jpeg)

## Sequenzdiagramm
![Sequenzdiagramm](/include/sequence_geodaten.png)

## Use-Case Diagramm
![Use-Case Diagramm](/include/use_case_geodaten.png)

## Grundkonzept
![Grundkonzept](/include/grundkonzept.png)

## Lastenheft

### Einführung

Das Projekt handelt von der Verarbeitung von Geodaten, bestehend aus Punktwolken und Katasterdaten einer Stadt . Die Anwendung soll über eine Benutzeroberfläche bedienbar und über die Kommandozeile parametrisierbar sein. Das Programm verarbeitet die Punktwolke zusammen mit den Katasterdaten und erzeugt für jedes Gebäude eine zugeschnitte Punktwolke.



### Beschreibung des Ist-Zustands

Derzeit muss man mühselig die Katasterdaten und Punktwolken übereinander legen und per Hand zuschneiden. Dieser Vorgang kostet für eine Vielzahl von Gebäuden sehr viel Zeit und Aufwand.



### Beschreibung des Soll-Konzepts

Die Anwendung schneidet automatisch die von dem Benutzer zur Verfügung gestellten Katasterdaten und Punktwolken zurecht. Gegebenfalls muss der Benutzer die Katasterdaten manuell über die Benutzeroberfläche so verschieben, dass diese mit der Punktwolke übereinstimmen. Es resultieren einzelne Punktwolken für jedes Gebäude aus der Punktwolke.



### Beschreibung von Schnittstellen

- Kommandozeile
- Graphische Benutzeroberfläche
- Benutzereingabe
  - Katasterdaten
  - Punktwolke
  - Ggf. Verschiebung der Katasterdaten/Punktwolke 



### Funktionale Anforderungen

- Automatisches Ausschneiden von Gebäuden, anhand der Grundrisse
- Entfernen von Objekten, die nicht zu einem Gebäude gehören
- Anbauten, wie zum Beispiel Balkone oder Erker die über den Grundriss hinausragen, nicht entfernen.
- Exportieren von ausgeschnittenen Gebäude in einzelnen Dateien
- Einfach bedienbare, graphische Benutzerobferläche zur Visualisierung der Katasterdaten/Punktwolke
- Möglichkeit zur Verschiebung der Katasterdaten/Punktwolke
- Parametrisierbarkeit über Kommandozeile



### Nichtfunktionale Anforderungen
#### Benutzbarkeit

Einfache und intuitive Interaktion mit Programm und graphischer Benutzeroberfläche.

#### Zuverlässigkeit

Die Präzision des Ausschneidens kann, aufgrund von unvorhersehbaren Umwelteinflüssen und ungenauen Benutzereingaben, variieren. 

Im Falle eines Programmabsturzes soll die manuelle Verschiebung des Benutzers gesichert werden, sodass diese nicht nochmal vorgenommen werden muss.

#### Effizienz

Da das Programm mit großen Dateien arbeitet, sollte die Anwendung performant programmiert sein, damit die Wartezeit nicht zu groß ist.

#### Änderbarkeit

Die Anwendung soll eine strukturierte Architektur haben. Der Quelltext soll sich an einen gewissen Codestil halten.

#### Übertragbarkeit

Die Anwendung soll betriebssystemunabhängig sein.



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

## Meilensteinplanung mit Teambesetzung

* 07.05
    * Parameter definieren (Moritz Withöft)
    * Katasterdaten und Punktwolke einlesen (Hannes Rüffer, Michelle Vorwerk)
    * GUI (ohne grafische Darstellung von Katasterdaten und Punktwolke) fertiggestellt (Dejan Novakovic, Leon Hornig)
* 14.05
    * Grundlegende Parametrisierung einbauen (Moritz Withöft)
    * Daten grafisch darstellen (Dejan Novakovic, Leon Hornig)
* 21.05
    * Koordinatensystem anpassen (Justin, Hannes, Michelle, )
* 28.05
    * GUI Option verschieben (Dejan Novakovic, Leon Hornig)
* 05.06
    * Gebäude ausschneiden (Moritz Withöft, Hannes Rüffer, Valentin Hertel)
    * Dateien exportieren (Moritz Withöft, Hannes Rüffer, Valentin Hertel)
* 11.06
    * Fertigstellung der Tests (Valentin Hertel)
* 18.06
    * Abgabe:
        * Aktualisiertes Konzept (Michelle Vorwerk, Dejan Novakovic)
        * Teamarbeitsbericht (Justin Drögemeier)
        * SW-Testbericht (Valentin Hertel)
        * SW-Dokumentation (Moritz Withöft)
        * Funktionalität nach Lastenheft (Hannes Rüffer, Leon Hornig)
* 25.06
    * Präsentation:
        * Benutzerhandbuch (Moritz Withöft, Dejan Novakovic)
        * Projektbericht (Justin Drögemeier)
        * PPT-Präsentation mit SW-Demo (Michelle Vorwerk)
        * Präsentation der Software nach Vorgaben im Lastenheft (Hannes Rüffer, Leon Hornig)

## Logging in Python *3*

### Installation
Python bietet schon standardmäßig eine ordentliche Logging Libary. Um sie nutzen zu können, muss nur folgendes Modul importiert werden:

```py
import logging
```

### Anwendung
#### Logger instanzieren / bereits vorhandenen holen
Das Modul verhält sich ähnlich wie wir es schon in Java kennen. Mit Hilfe des folgenden Befehls, kann eine Logger Instanz erstellt bzw. eine bereits vorhandene geholt werden:
```py
logger = logging.getLogger(__name__)
```
In unseren Beispiel wird das built-in Keyword genutzt, dass den Namen des Modules bereithält. Sobald in einem Modul ein Logger an einen Namen gebunden ist, kann der gleiche Logger mit obigen Aufruf geholt werden. 

#### Vererbung
Ähnlich wie in Java spielt Vererbung eine Rolle. Das Zeichen **.** stellt das Trennzeichen dar.

Beispiel: 

- foo < Parent
    - foo.kind < Kind
        - foo.kind.kind < Kind von Kind


Das hat zur Folge, dass wenn eine Einstellung in einem Logger nicht explizit festgelegt ist, geschaut wird, ob der nächste Elternteil dies Festgelegt hat.
Falls man diesen Effekt sich nicht wünscht, kann Vererbung folgender Maße deaktiviert werden:

```py
logger.propagate = False
```

#### Loggen und die verschiedenen Log-Stufen

Es gibt verschiedene Log-Stufen, um einen Log zu kategorisieren bzw. auch zu priorisieren und mit eventuelle Konfigurationen das Log Verhalten zu ändern.

| Stufe | Numerischer Wert |
| :---: | :---: |
| CRITICAL | 50 |
| ERROR | 40 |
| WARNING | 30 |
| INFO | 20 |
| DEBUG | 10 |
| NOTSET | 0 |

Erklärung folgender Stufen:

| Stufe | Erklärung |
| :---: | --- |
| CRITICAL | Ein Seriöser Fehler, der höchstwahrscheinlich dafür sorgt, dass das Programm nicht weiter laufen kann. |
| ERROR | Es ist ein Fehler enstanden, der dafür sorgen kann, dass Funktionallitäten eingeschränkt werden oder nicht funktionieren |
| WARNING | Etwas unerwartetes ist passiert bzw. es existieren Indikatoren, die dafür sorgen könnten, dass die Software in der Zukunft nicht funktionsgemäß funktioniert. |
| INFO | Information über das aktuelle Geschehen |
| DEBUG | Wie es der Name sagt, für Datenanalyse bzw. Debug Gründen |


Um jetzt mit dem Logger in einer gewünschten Stufe zu loggen, kann man folgende Methoden benutzen.

```py
logger.debug('Level: DEBUG')
logger.info('Level: INFO')
logger.warning('Level: WARNING')
logger.error('Level: ERROR')
logger.critical('Level: CRITICAL')
logger.exception("Besonders: Siehe unten")
```

Ein besonderen Aufruf stellt *.exception(message)* dar. Diese Methode sollte man nur in einem *catch* Block aufrufen. Man bekommt als Log Meldung ein Stacktrace und die übergebene Nachricht.

Falls eine Log Meldung "verschluckt" werden sollte, kann dies daran liegen, dass die Log Meldung eine niedrigere Stufe hat, als bei den Logger eingestellt ist. Um die niedrigste Log Stufe festzulegen, die ein Logger verarbeitet, kann folgende Methode benutzt werden:

```py
logger.setLevel(LEVEL)
```

> Falls die Meldung weiterhin verschluckt wird, kann dies daran liegen, dass der Handler die Nachricht verschlucht. Siehe dazu das Kapitel 'Handler'

#### Handler

Der Logger hat erstmal die Aufgabe zu bestimmen welche Log Messages weiter geleitet werden und bietet die Funktionalitäten um zu loggen. Damit wir aber die Log Meldungen sehen können bzw. an das richtige Output System weitergeleitet, sind Handler zuständig. 

Handler können unterschiedliche die Nachrichten weiterleiten, unter anderem auf der Konsole oder in Dateien. Um einen Logger einen Handler hinzuzufügen, kann folgende Methode verwendet werden:

```py
logger.addHandler(HANDLER)
```

##### File Handler

Um ein Handler Objekt zu erstellen, dass Log Meldungen in Dateien schreibt, kann folgender Befehl verwendet werden:

```py
fileHandler = logging.FileHandler(filename, mode='a', encoding=None, delay=False)
```
- filename:
    - Name der Datei bzw. Pfad   
- mode: 
    - Ob Datei bei einer neuen Session überschrieben werden soll oder die Log Meldungen angehängt werden soll.
        - 'a' => Anhängen
        -  'w' => Überschreiben
- encoding: 
    - Codierung kann mit angegeben werden
- delay:
    - Delay ab wann geflushed werden soll   

#### Formatter

Formatter Objekte könnne, wie der Name es schon sagt, für Formatierungen benutzt werden bzw. definieren die Formatierung. Jedes Handler Objekt kann eine eigenes Formater Objekt zugewiesen bekommen. Um ein Formater Objekt zu erstellen, kann folgende Methode benutzt werden: 

```py
formater = logging.Formatter(fmt=None ,datefmt=None)
```

- fmt
    - Gibt an, wie allgemeine Log Meldung formatiert werden soll
    - Beispiel Formatierung: '%(asctime)s - %(levelname)s - %(message)s'
- datefmt
    - Falls in der Log Meldung ein Datum benutzt wird, gibt datefmt an, wie das Datum formatiert werden soll.
    - Beispiel Formatierung: '%Y-%m-%d %H:%M:%S'


Um dann ein Formater Objekt einem Handler zuzuweisen, kann folgende Methode benutzt werden:

```py
handler.setFormatter(formatterObject)
```

#### Beispiel

Hier ein kleines Beispiel, wie man alle oben genannten Komponenten nutzen kann:

```py
import logging

# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
```
