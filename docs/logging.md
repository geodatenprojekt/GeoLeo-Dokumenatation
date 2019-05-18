# Logging in Python *3*

## Installation
Python bietet schon standardmäßig eine ordentliche Logging Libary. Um sie nutzen zu können, muss nur folgendes Modul importiert werden:

```py
import logging
```

## Anwendung
### Logger instanzieren / bereits vorhandenen holen
Das Modul verhält sich ähnlich wie wir es schon in Java kennen. Mit Hilfe des folgenden Befehls, kann eine Logger Instanz erstellt bzw. eine bereits vorhandene geholt werden:
```py
logger = logging.getLogger(__name__)
```
In unseren Beispiel wird das built-in Keyword genutzt, dass den Namen des Modules bereithält. Sobald in einem Modul ein Logger an einen Namen gebunden ist, kann der gleiche Logger mit obigen Aufruf geholt werden. 

### Vererbung
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

### Loggen und die verschiedenen Log-Stufen

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

### Handler

Der Logger hat erstmal die Aufgabe zu bestimmen welche Log Messages weiter geleitet werden und bietet die Funktionalitäten um zu loggen. Damit wir aber die Log Meldungen sehen können bzw. an das richtige Output System weitergeleitet, sind Handler zuständig. 

Handler können unterschiedliche die Nachrichten weiterleiten, unter anderem auf der Konsole oder in Dateien. Um einen Logger einen Handler hinzuzufügen, kann folgende Methode verwendet werden:

```py
logger.addHandler(HANDLER)
```

#### File Handler

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

### Formatter

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

### Beispiel

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