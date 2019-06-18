# Sitzungsprotokolle  
<br/>  

# 09/04/2019
## Rollenverteilung
Projektleiter: Justin Drögemeier  
Projektcontroller: Dejan Novakovic  
Systemarchitekt: Leon Hornig  
Risikomanager: Hannes Rüffer  
Stakeholdermanager: Michelle Vorwerk  
Qualitätsmanager: Valentin Hertel 
Dokumenatationsmanager: Moritz Withöft

## Spielregeln

In der Sitzung am 09. April 2019 wurden folgende Spielregeln festgehalten:  
- Spätestens am Sonntagabend haben die in der Woche erarbeiteten Ergebnisse vorzuliegen.
- Jeden Montag soll, je nach Zeitplan und Möglichkeiten, eine Besprechung stattfinden. Diese kann über digitale Medien oder in Form eines Treffens erfolgen.
- Als Vorgehensmodell hat man sich auf Kanban geeinigt. Dieses gilt es einzuhalten.
- Es darf nur ausführbarer Code in den Master gepusht werden.
- Auf jede elementare Änderung erfolgt ein Commit. Eine neue Methode ist beispielsweise ein Commit, aber auch Refactoring einer solchen.
- Es werden ausführliche Tests geschrieben. Die Tests sollen alle essentiellen Bestandteile der Software abdecken.
- Arbeiten werden pünktlich abgegeben.
- Das ganze Team beteiligt sich an dem Softwareprojekt.

## Brainstorming

Im Folgenden wurden die getätigten Überlegungen zur Umsetzung in Prosa festgehalten:

> Nach der Einigung auf geltende Regeln und der Übereinkunft auf das zuverwendende Vorgehensmodell, wurde zwischen der Umsetzung mittels einer Web-Applikation und einer Standalone-Anwendung abgewogen. Eine Webapplikation würde mit WebGL zur grafischen Darstellung und AngularJS, in Kombination mit einem Bundler sowie Bootstrap, auf Frontend-Seite implementiert. Die Backend-Seite wäre an dieser Stelle ein Java-Server, der die Verarbeitung und Analyse der Daten übernimmt. Nach Rücksprache mit dem Auftraggeber und dem Risikomanager wurde dieser Ansatz auf Grund der späteren möglichen Einbindung in größere Software verworfen, sodass man sich am Ende auf die Umsetzung einer **Standalone-Anwendung** mit **Python** geeinigt hat. Es soll nun geprüft werden, wie gut sich die Anforderungen mit Python umsetzen lassen, sodass im Falle einer Impraktikabilität mit Python die Programmiersprache noch vor Implementierungsbeginn gewechselt werden könnte. Zum jetzigen Zeitpunkt wird aber mit der Umsetzung mittels Python gerechnet.

## Werkzeugeinsatz

- GitHub
- Python
- Bibliotheken

## CodeRules

- Google bietet Koventionen für diverse Sprachen an.
  - Google Konvention für Python soll demnach befolgt werden.
- Auf Rechtschreibung ist unbedingt zu achten.
- Eine sinnvolle Namensgebung der Methoden muss gegeben sein.
- Es wird UTF-8 als Zeichensatz benutzt.
- Es werden Dokumentationskommentare verwedet.
  - Keine einzeiligen Kommentare!
- Der Programmcode ist komplett auf Englisch.
  - Sowohl Kommentare als auch Namensgebung von Klassen/Methoden!

## Vorgehensmodell

Es wurde sich auf ein agiles Modell in Form von Kanban geeinigt. Weiterhin sollen regelmäßige Rücksprachen und Teamsitzungen einen positiven Projektverlauf unterstützen.

## Risikomanagement

Im letzten Tagespunkt wurden erste Risiken identifiziert und mögliche Gegensteuerungsmaßnahmen erläutert.

**Identifizierung:**  
- Unwissenheit über die Form/Aussehen/Bestand der zu erhaltenden Daten
- Probleme mit der grafischen Oberfläche
- Falsche zeitliche Planung des Ablaufs
- Verwendung von falschen Tools/Bibliotheken
- Unzureichendes Änderungsmanagement sowie plötzlich auftretende Komplikationen, die den zeitlichen Ablauf gefährden

**Gegensteuerungsmaßnahmen:**
- Einholen von Expertenmeinungen sowie Erfahrungsberichte
- Regelmäßiger Austausch mit dem Auftraggeber
- Frühzeitige Auseinandersetzung mit der Sprache/Tools/Bibliotheken
- Sorgfältige Planung
- Schnelle aber gründliche Umsetzung von notwendigen Änderungen


# 16/04/2019

In der Sitzung am 16. April 2019 wurden einige Dinge besprochen und diskutiert.  

Im ersten Schritt der Sitzung wurden weitere Aufgaben verteilt, die in den anstehenden Wochen durchgeführt werden müssen.
- Anforderungsanalyse: Justin Drögemeier
- Usecasediagramme: Dejan Novakovic
- Sequenzdiagramme: Dejan Novakovic
- Klassendiagramme: Valentin Hertel
- Arbeitsplan/Meilensteinplanung: Michelle Vorwerk, Moritz Withöft
- Lastenheft: Hannes Rüffer, Leon Hornig

Zudem wurde die Bibliothek "laspy" genauer betrachtet. Es handelt sich sowohl um eine Read-Bibliothek als auch um eine Write-Bibliothek, sodass diese sowohl zum Einlesen der gegebenen las-Dateien verwendet werden kann als auch zur Bereitstellung, der im Programm neu erzeugt las-Dateien, dient. Hier hat es sich angeboten, dass man sich auch einmal die Katasterdaten anschaut, die vom Land NRW bereitgestellt werden. Da es sich hier um unglaublich große Datenmengen handelt, sind ein paar weitere Fragen aufgetreten (siehe unten), die zu beantworten gilt.

Im nächsten Schritt wurde die Struktur des Lastenhefts festgelegt und besprochen, welches in nächster Zeit von Hannes Rüffer und Leon Hornig fertiggestellt wird.

Zuletzt wurde ein grober Zeitplan, zusammen mit den festgelegten Abgabedaten der einzelnen Projektfortschritte, besprochen. Daraus wird in nächster Zeit die Meilensteinplanung von Michelle Vorwerk und Moritz Withöft erstellt, die die weitere Orientierung des Projekts vorgibt.

## Aufgetretene Fragen
Folgende Fragen sind im Verlauf aufgetreten und sollten möglichst bald im Sinne eines positiven Projektverlaufs beantwortet werden:
- Werden zusätzliche Informationen bzgl. der Stadt angegeben oder wie wird man anhand der Punktwolke fündig?
- Welche Dateien müssen genutzt werden?
- Sollen Dateien hinterlegt werden oder stellt der Nutzer beide Daten (Punktwolke und Kataster) bereit?  

Dabei ist es überaus wahrscheinlich, dass in den kommenden Tagen und Wochen weitere Fragen auftreten. Diese Fragen werden je nach Art im Team geklärt oder werden individuell durch die einzelnen Rollenverteter bewältigt.

# 23/04/2019

In der Sitzung am 23. April 2019 wurden in einem Meeting mit Herrn Schiffel zunächst die noch offenen Fragen der Vorwoche beantwortet, sodass im weiteren Verlauf mit einer gut geplanten und risikominimierten Arbeit begonnen werden konnte.

Dabei wurden folgende Punkte geklärt:
- Die Katasterdaten sind bisher noch nicht von der Firma geliefert worden, die diese zur Verfügung stellt und werden unserem Team ausgehändigt, sobald diese eingetroffen sind
- Die Punktwolke steht nun zur Verfügung und kann von jedem Teammitglied heruntergeladen werden
- **Jedes** Grundstück wird im Endergebnis in einer eigenen Datei abgespeichert
- Die Grundstücke werden aus der Punktwolke **mit Hilfe der Katasterdaten** "herausgeschnitten"
- Anzustreben ist eine Draufsicht auf die jeweiligen Karten, sodass diese von oben angepasst bzw. übereinandergelegt werden können
  - Hier kann es eine Navigation geben, mit der eine Karte verschoben werden kann (links, rechts, oben, unten)
- Es handelt sich um Gauß-Krüger-Koordinaten
- Eine Punktwolke kann zuvor mit einem Tool (z.B. Cloudcompare) betrachtet werden, um sich mit der Form vertraut zu machen

Nach der Klärung der Fragen wurde mit der Arbeit in den einzelnen Teilgruppen begonnen.
- Hannes Rüffer und Leon Hornig arbeiten am Lastenheft
- Justin Drögemeier arbeitet an der Anforderungsanalyse
- Valentin Hertel arbeitet an den Klassendiagrammen
- Dejan Novakovic arbeiten an den Usecasediagrammen
- Moritz Withöft und Michelle Vorwerk arbeiten an der Meilensteinplanung

# 30/04/2019
Am heutigen Tage wurden die definierten Meilensteine dem Auftraggeber vorgestellt. Dies wurde im Zuge einer Präsentation durchgeführt, in der zudem auch das Konzept vorgestellt wurde, sowie die verwendete Programmiersprache, Risikomanagement, Aufteilung der einzelnen Gruppenmitglieder auf die zu bewältigenden Aufgaben und weitere Anforderungen.

Danach folgte ein kleines Gruppenmeeting, um sich über den aktuellen Projektstand zu informieren, aber auch um das weitere strategische Vorgehen genauer festzulegen. Der aktuelle Zeitplan mag etwas zu kleine Schätzzeiten enthalten, sodass empfohlen wurde, einen größeren Puffer zu erlauben, da sich die bisher bestimmten Zeiten mit hoher wahrscheinlichkeit erhöhen werden.

# 07/05/2019

Zu dieser Sitzung wurden die akutellen Fortschritte der jeweiligen Arbeitsgruppen mitgeteilt.

- Dejan und Leon haben sich mit der GUI-Bibliothek tkinter beschäftigt. Diese erfüllt die funktionalen Anforderungen, hat jedoch eine sehr unästhetische Benutzeroberfläche. Der Projektleiter in Form von Justin hat vorgeschlagen, sich mit der Bibliothek Kivy zu beschäftigen, weil diese eine anschauliche Oberfläche bietet, aber auch eine OpenGL-ähnliche grafische Darstellung zur Verfügung stellt.
- Justin hat sich mit Logging beschäftigt und wird in der nächsten Woche die zu verwendende Bibliothek/Schnittstelle vorstellen. Weiterhin hat er sich bereit erklärt das GUI-Team bei der Entwicklung zu unterstützen.
- Moritz hat sich mit der Definition der Parameter beschäftigt und hat die Aufgabe, dass die Eingabe mittels der Kommandozeilenparameter bis zur nächsten Woche implementiert wurde.
- Valentin hat sich mit der Testbibliothek "unittest" beschäftigt und wird diese in der nächsten Woche vorstellen, sowie sich fortlaufend mit dem Testen der Anwendung beschäftigen. Er ist ja schließlich auch der Qualitätsmanager und hat diese Aufgabe.

# 14/05/2019 und 21/05/2019

Die Protokolle aus den beiden Sitzungen entfallen. An diesen Terminen wurde weiter konzentriert und effizient am Projekt gearbeitet, daher ist eine detaillierte Protokollführung der Teambesprechungen obsolet.

# 28/05/2019

An diesem Tag war der Auftraggeber nicht anwesend. Aus diesem Grund wurde selbstständig und konzentriert in den einzelnen Teilgruppen der verschiedenen Aufgabenbereiche gearbeitet. Besonders die Arbeit im Backend macht große Fortschritte. Unter dem Kommando von Abteilungsleiter Rüffer stellt er zusammen mit Hertel und Withöft ein hervorragendes Team dar.
Während dieses Trio auf Seiten der Punktwolke aktiv ist, setzt Michelle Vorwerk effektiv das Einlesen und die Verarbeitung der Katasterdaten um. Es lassen sich diese bereits auswerten und verändern, sodass diese zur Anzeige aus dem Frontend heraus bereitsteht.

Weiterhin kümmert sicht Valentin Hertel konzentriert um das ausführliche Testen der einzelnen Module und Moritz Withöft um die Dokumentation des Projekts sowie die Protokollführung in den einzelnen Sitzungen.

# 04/06/2019

Da bereits in zwei Wochen die Dokumentation mit allen Heften des Projekts abgegeben werden werden sollen, wurden zu Beginn der Sitzung ausführliche Fortschrittsberichte von Backendleiter Hannes Rüffer und von Frontendleiter Leon Hornig eingeholt.

**Bericht des Leiters für Backend-Development - Hannes Rüffer:**

Der Algorithmus zur Eingabe von Las Dateien wurde fertiggestellt. Diese lassen sich unter der Angabe des Ordners einlesen und verarbeiten. Mittels der Kombination mit den erhaltenen Katasterdaten können bereits Koordinaten von Gebäuden identifiziert werden. Dafür wird ein Algorithmus einer Bibliothek verwendet, die in der Lage ist zu prüfen, ob sich ein Punkt in einem Polygon befindet. Die Laufzeit ist inzwischen zufriedenstellend. Obwohl diese Anfangs ein Problem darstellte, konnte bereits der zeitliche Aufwand einer 10GB Datei auf ca. 2 Minuten begrenzt werden.
Dabei wird schon ein Preprocessing vorgenommen, um die Laufzeit weiter zuverbessern sowie im Vorfeld die global höchsten und tiefsten Koordinaten bestimmt, um Fehler zu vermeiden und Grenzen zu setzen.

In den nächsten Schritten müssen Punktwolken zusammengeführt werden (einfach), sowie diese ausgeschnitten werden (herausfordernd).

**Bericht des Leiters für Frontend-Development - Leon Hornig:**

Der Bericht von Leon Hornig beinhaltete den Fortschritt im Frontend. Zur Anzeige soll TKinter benutzt werden. Hier wird PyOpenGL eingebunden, um aus den Koordinaten ein Bild zu erzeugen. Hier wird noch einiges an Arbeit nötig sein.


**Weitere Besprechungen:**

Desweiteren wurde über die Art der Anzeige und die Einstellung des Offsets diskutiert. Da eine komplette Darstellung einer 10GB großen Punktwolke einem normalen haushältsüblichen Computers nicht zuzumuten ist, wird nur ein Ausschnitt angezeigt, über den die entsprechende Verschiebung angepasst. Im Hintergrund werden dann alle Punktwolken mit Häusern ausgeschnitten und gespeichert.

Im weiteren Verlauf wurde an den besprochenen Punkten gearbeitet, um einen zufriedenstellenden Fortschritt zu erreichen.

# 11/06/2019

Am heutigen Tag fand die letzte Teamsitzung vor der Abgabe der Projektdokumentation am 18. Juni 2019 statt. Es handelt sich somit auch um das letzte Protokoll der Teamsitzungen. Es wurde sich noch einmal ausführlich mit den Teammitgliedern ausgetauscht.

**Backend:**  
Hannes Rüffer macht weiterhin große Fortschritte im Backend. Er wird in naher Zukunft die letzten erforderlichen Methoden fertigstellen. Das Ausschneiden der einzelnen Punktwolken funktioniert nun. Aktuell arbeitet er an Feinheiten, um auch komplexere bzw. seltene Fälle sauber lösen zu können.

**Frontend:**  
Im Frontend schreiten Leon und Dejan ebenfalls mit großen Schritten voran. Während Leon die Anzeige der Daten mit OpenGL erledigt hat, kann Dejan eine funktionierende GUI vorweisen, mit der die angezeigten Daten auf die Bedürfnisse des Nutzers angepasst werden können.

**Weiteres:**  
Die restlichen Teammitglieder beschäftigen sich ebenfalls mit diversen Bereichen, in denen noch Arbeit zu tun ist. Während sich Valentin mit dem Schreiben und Prüfen von Testfällen um die Softwarequalität kümmert, haben sich die übrigen mit der Erzeugung einer ausführlichen Projektdokumentation beschäftigt, die es zur nächsten Woche abzuschließen gilt.