from flask import Flask
from flask import render_template
from flask import request
import daten #daten.py importieren
import plotly.graph_objects as go 
from plotly.offline import plot
from datetime import date


app = Flask("Intermittent Fasting")


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/neues_rezept.html', methods=["GET", "POST"])
def rezept_speichern():
	if request.method == "POST":
		titel = request.form['titel']
		wort_liste = titel.split()
		wort_anzahl = len(wort_liste) #Anzahl Zeichen des Rezepttitels ermitteln
		zutaten = request.form['zutaten']
		zubereitung = request.form['zubereitung']
		kcal = request.form['kcal']
		if wort_anzahl >= 2: #da der Rezepttitel nur aus einem Wort bestehen darf
			fehler_meldung = "Bitte beachte, dass der Rezepttitel nur aus einem Wort bestehen darf!"
			return render_template('neues_rezept.html', fehler_meldung=fehler_meldung)
		else: 
			bestätigung_rezept = "Das Rezept " + titel + " wurde erfolgreich zur Datenbank hinzugefügt!"
			titel, zutaten, zubereitung, kcal = daten.rezept_speichern(titel, zutaten, zubereitung, kcal) #eingaben vom Formular in daten.json übergeben und abspeichern
			return render_template('neues_rezept.html', bestätigung_rezept=bestätigung_rezept)
	return render_template('neues_rezept.html')


@app.route('/kalorienbilanz.html',  methods=["GET", "POST"])
def mahlzeiten_speichern():
	if request.method == "POST":
		username = request.form['username']
		rezept_titel = request.form['rezept_titel']
		data = daten.rezepte_laden()
		if rezept_titel in data: #überprüfen, ob das Rezept überhaupt in rezepte.json ist
			tag = date.today()
			kalorien = data[rezept_titel]["kcal"] #nur die kcal Anzahl des entsprechenden Rezeptes ist für diese Funktion relevant
			bestätigung_mahlzeit = "Die Mahlzeit " + rezept_titel + " wurde erfolgreich zu deinem Fastentag hinzugefügt!"
			rezept_titel, kalorien = daten.mahlzeiten_speichern(tag, username, rezept_titel, kalorien) #Informationen an daten.json übergeben, um die Mahlzeit abzuspeichern
			mahlzeiten = daten.mahlzeiten_laden(username, tag) #auch diese funktion benötigt username und tag damit der korrekte Dateiname aufgerufen werden kann
			
			#Verbrauchte Kcal-Anzahl berechnen
			kcal_verbraucht = 0
			for kcal in mahlzeiten.values(): #alle kcal in mahlzeiten.json der entsprechenden Person sollen zusammengerechnet werden
				kcal = int(kcal)
				kcal_verbraucht += kcal
			kcal_verfuegbar = 500-kcal_verbraucht #ermitteln, wieviele kcal von denn 500 noch verfügbar sind

			#Rückmeldung der Applikation wieviele kcal verfügbar sowie verbraucht sind
			kcal_verbraucht_str = username + ", du hast heute bereits " + str(kcal_verbraucht) + " gegessen."
			kcal_verfuegbar_str = "Das heisst, du hast noch " + str(kcal_verfuegbar) + " Kalorien verfügbar heute."

			#Plotly-Grafik:
			colors = ['mediumturquoise', 'lightgreen']
			labels = ['verbraucht', 'verfügbar'] #Beschriftung der Plotly-Grafik
			values = [kcal_verbraucht, kcal_verfuegbar] #Werte der Plotly-Grafik
			fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole= 0.9)]) #Angaben für die Plotly-Grafik
			fig.update_traces(hoverinfo='label', textinfo='value', textfont_size=20, marker=dict(colors=colors, line=dict(color='#000000', width=2))) #Formatierung der Grafik
			grafik = plot(fig, output_type="div") #Plotly in der Variable "grafik" abspeicher, um sie dann ins html übergeben zu können

			#ermitteln, ob max kcal-Anzahl von 500 bereits überschritten wurde
			if kcal_verfuegbar <= 0:
				kcal_ueberschritten = "Das heisst, du hast heute deinen Kalorienbedarf um " + str(-1*kcal_verfuegbar) + " überschritten!"
				kcal_verfuegbar = kcal_ueberschritten #kcal verfügbar wurde mit kcal überschritten überschrieben
				return render_template('kalorienbilanz.html', kcal_ueberschritten=kcal_ueberschritten, kcal_verfuegbar=False, bestätigung_mahlzeit=bestätigung_mahlzeit, kcal_verbraucht_str=kcal_verbraucht_str, viz_div=grafik, username=username)
			
			return render_template('kalorienbilanz.html', bestätigung_mahlzeit=bestätigung_mahlzeit, kcal_verbraucht_str=kcal_verbraucht_str, kcal_verfuegbar_str=kcal_verfuegbar_str, viz_div=grafik, username=username)
		else: #wenn das Rezept nicht gefunden werden kann, kommt diese Fehlermeldung
			fehler_meldung = "Das gewählte Rezept ist nicht in der Datenbank vorhanden. Bitte prüfe die Schreibweise (Gross- und Kleinschreibung beachten!).\
			Am besten kopierst du den Rezeptnamen direkt von der Übersicht! Falls das Rezept noch nicht vorhanden ist, füge es zur Datenbank hinzu."
			return render_template('kalorienbilanz.html', fehler_meldung=fehler_meldung)
	return render_template('kalorienbilanz.html')
	

@app.route('/rezepte.html')
def uebersicht():
    rezepte = daten.rezepte_laden() #Inhalt von rezepte.json als ditc in variable "rezepte" speichern
    rezepte_liste = ""
    for key, value in rezepte.items():
    	zeichen_laenge = len(key)
    	binde_striche = "_" * (130-zeichen_laenge) #damit der Rest der Zeile mit Bindestrichen aufgefüllt wird und der weitere Inhalt auf eine neue Zeile kommt
    	titel = key + binde_striche
    	zutaten = rezepte[key]["zutaten"] #die zugehörigen Zutaten des entsprechenden Rezepttitels aufrufen
    	zubereitung = rezepte[key]["zubereitung"]
    	kcal = rezepte[key]["kcal"]
    	rezepte_liste += titel + " Zutaten: " + zutaten + " // Zubereitung: " + zubereitung + " // Anzahl Kalorien: " + kcal + " // " #Zeilenumbruch konnte mit "<br>" oder "\n" nicht erreicht werden 	
    return render_template('rezepte.html', rezepte_liste=rezepte_liste)


if __name__ == "__main__":
    app.run(debug=True, port=5000)




