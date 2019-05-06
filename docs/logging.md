# Logging in Python *3*

## Installation
Python bietet schon standardmäßig eine ordentliche Logging Libary. Um sie nutzen zu können, muss nur folgendes Modul importiert werden:

```py
import logging
```

## Anwendung
Das Modul verhält sich ähnlich wie wir es schon in Java kennen. Mit Hilfe des folgenden Befehls, kann eine Logger Instanz erstellt bzw. eine bereits vorhandene geholt werden:
```py
logger = logging.getLogger(__name__)
```

In unseren Beispiel wird das built-in Keyword genutzt, das den Namen des Modules bereithält. Sobald in einen Modul ein Logger an einen Namen gebunden ist, kann der gleiche Logger mit obigen Aufruf geholt werden. 

Ähnlich wie in Java spielt Vererbung eine Rolle. Das Zeichen **.** stellt das Trennzeichen dar.

Beispiel: 

- foo
    - foo.kind
        - foo.kind.kind


Das hat zur Folge, dass wenn eine Einstellung in einem Logger nicht explizit festgelegt ist, geschaut wird, ob der nächste Elternteil dies Festgelegt hat.
Falls man diesen Effekt sich nicht wünscht, kann Vererbung folgender Maße deaktiviert werden:

```py
logger.propagate = False
```
