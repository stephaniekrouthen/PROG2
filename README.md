# Projektidee 1  
## Ausgangslage:  
Ich ernähre mich seit einiger Zeit nach dem "Intermittend Fasting" Konzept. Dabei handelt es sich um eine Ernährungs- bzw. Diät-Form, bei der je nach Plan eine gewisse Zeit lang gefastet wird. Es gibt dabei folgende sechs bekannte Methoden:  
1. *The 5/2 Diet*: Zwei Tage pro Woche fasten, an den anderen Tagen normal essen. Während den Fasten-Tagen sind bei Männern 600 kcal erlaubt, bei Frauen 500 kcal.  
2. *16:8 Methode*: 16 Stunden fasten und in den folgenden 8 Stunden werden die Mahlzeiten zu sich genommen.   
3. *20:4 Methode*: 20h fasten, während 4h essen    
4. *Eat-Stop-Eat*: ein oder zwei mal in der Woche einen ganzen Tag komplett fasten  
5. *Alternate-day fasting*: jeden zweiten Tag komplett fasten  
6. *The Warrior Diet*: den ganzen Tag fasten, ausser rohes Gemüse und Früchte sind erlaubt; am Abend eine grosse Mahlzeit zu sich nehmen  

## Funktion/Projektidee:  
Diese Applikation soll einen bei dieser Ernährungsform zu untersützen und die Zeiten bzw. Kalorieneinnahme besser im Blick zuhaben. Es soll die Möglichkeit geben, auszuwählen ob man einen neuen Plan erstellen möchte oder Infos zum aktuellen Plan zu erhalten.  
1. Man muss auswählen, welchen Plan man verfolgen möchte, um sich danach die Fasten-Tage und Zeiten zu überlegen und festzuhalten.  
2. Ebenfalls soll es die Applikation ermöglichen, Infos darüber zu erhalten, bis wann man noch fasten muss bzw. wann man wieder essen darf. Bzw. wenn man die 5/2 Diet wählt, soll die Applikation ausrechnen, wie viele Kalorien man am heutigen Tag noch zu sich nehmen darf.   

## Workflow:  
**Dateieingabe:**  
Auswahl, ob man einen neuen Plan erstellen möchte (1.) oder Informationen zum aktuellen Plan einsehen möchte (2.):
    1. neuer Plan erstellen:  
    * Auswahl zwischen den 6 Plänen
    * Auswahl auf wann die Fastenzeiten fallen sollen (Tages- sowie Zeitabhängig)
    * Auswahl, was mit dem erstellten Plan passieren soll (Liste oder Tabelle)
    2. aktueller Plan einsehen:  
    * Auswahl, was man mit der Tabelle machen möchte (ausdrucken, per Mail senden, abspeichern)
    * Bei der 5/2 Diet können Rezepte ausgewählt werden, die für diese Fastenart empfohlen sind, um diese dem aktuellen "Fastentag" hinzuzufügen.
**Datenverarbeitung/Speicherung:**  
* ausgewählte Fastenzeiten speichern und in der gewählten Form (Liste oder Tabelle) formatieren
* bei der 5/2 Diet die kcal der Rezepte zusammenrechnen die an zu den Fastentagen hinzugefügt worden sind, Daten formatieren 
**Datenausgabe:**  
    1. neuer Plan erstellen:  
    * die 6 Pläne inkl. kurzer Beschreibung auflisten
    * Liste oder Tabelle des Plans anzeigen, Daten an Drucker senden oder per Mail an jemanden senden.
    2. aktueller Plan einsehen:  
    * Tabelle bzw. Liste anzeigen, ausdrucken, abspeichern oder versenden
    * Kalorienbilanz bei 5/2 Diät anzeigen 
