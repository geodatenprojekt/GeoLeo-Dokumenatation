# Protokolle  
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
