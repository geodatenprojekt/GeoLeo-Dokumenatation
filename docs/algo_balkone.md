## Algorithmus zur Eingrenzung der Punktewolke

### Annahmen

Unter den Optimalbedingungen:
- Kataster liefert Rechteckige Fläche mit Koordinaten, die abgeglichen sind mit der Punktewolke
- Die Punktewolke weißt keine übermäßigen Lücken auf

Eingabe:
- Rechteck ((x1, y1), (x2, y2)) aus dem Kataster, Punkt unten links und oben rechts
- Punktewolke eingelesen durch PointCloudFileIO
- Eingrenzungsdistanz (wie weit +/- um das Kataster herum die Punkte zur Bestimmung gewählt werden) -> muss noch bestimmt werden
- Distanztoleranz (wie weit benachbarte Punkte voneinander entfernt liegen dürfen, um als zusammenhängend gewertet zu werden) -> muss noch bestimmt werden

Ausgabe:
- Liste mit booleans. Entsprechend lang wie die eingegebende Punktewolke und enumeriert, welche der Punkte in der finalen Punktwolke vorhanden sein sollen. Das muss so gemacht werden, damit laspy & numpy die eingelesene Punktewolke richtig ausschneiden können

### Algorithmus
```
eingDist #Eingrenzungsdistanz
distanzTol #Distanztoleranz
x1, y1, x2, y1 = Kataster() #Koordinaten des Katasters, x1<x2 & y1<y2
x1 = x1 - eingDist
y1 = y1 - eingDist
x2 = x2 + eingDist
y2 = y2 + eingDist
punkte = Punktwolke()
auswahlAllerPunkte = punktwolkeSubsetAuswählen(punkte, x1, y1, x2, y2) #Liste mit boolean Werten
punkteEingegrenzt = punkte[auswahlAllerPunkte] #Nehme nur die konkreten Punkte aus der Punktwolke
\#An dieser Stelle evt. Punkte aus dem Inneren des Rechtecks aus der Auswahl herausnehmen, um die Performance für den folgenden Part zu verbessern

n = punkteEingegrenzt.length

for i bis n
  punkt = punkte[i]
  auswahlNaherPunkte = berechnePunkteNahAnPunkt(punkt, punkte, distanzTol)
  auswahlAllerPunkte = auswahlAllerPunkte & auswahlNaherPunkte

  nahePunkte = punkte[auswahlNaherPunkte]
  for j bis auswahlNaherPunkte.length
    if auswahlNaherPunkte[j] == True and auswahlAllerPunkte[j] == False
      naherPunkt = punkte[j]
      punkteEingegrenzt.append(naherPunkt)
      n++

\#An dieser Stelle evt. Grenzen für die Auswahl aller Punkte setzen, in dem Fall, dass eine Kette von Punkte, die nicht zu einem Haus gehört haben (z.B. ein nahestehender Baum), mitgescannt wurde. Dann würde verhindert werden, dass zu viel außerhalb des tatsächlichen Hauses ausgeschnitten wird.

return auswahlAllerPunkte
```
