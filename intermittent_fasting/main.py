from flask import Flask
from flask import render_template
from flask import request
import daten
import pandas as pd
import plotly.graph_objects as go


app = Flask("Intermittent Fasting")

"""
@app.route('/hello/plotly')
def plotly():
	mahlzeiten = daten.mahlzeiten_laden()
	kalorien_bilanz = 0
	for kcal in mahlzeiten.values():
		kcal = int(kcal)
		kalorien_bilanz += kcal
	verbraucht = (100/500)*kalorien_bilanz
	verfuegbar = 100 - verbraucht
	colors = ['mediumturquoise', 'lightgreen']
	labels = ['verbraucht', 'verfügbar']
	values = [verbraucht, verfuegbar]

	fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole= 0.9)])
	fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20, marker=dict(colors=colors, line=dict(color='#000000', width=2)))
	fig.show()
	return render_template('kalorienbilanz.html')
"""


@app.route('/hello/')
def hello():
	return render_template('index.html', name="du")

@app.route('/hello/<name>')
def hello_persoenlich(name=False):
	if name:
		return render_template('index.html', name=name)
		name = daten.namen_speichern(name)
	else:
		return render_template('index.html')


@app.route('/hello/neues_rezept.html', methods=["GET", "POST"])
def rezept_speichern():
	if request.method == "POST":
		titel = request.form['titel']
		zutaten = request.form['zutaten']
		zubereitung = request.form['zubereitung']
		kcal = request.form['kcal']
		bestätigung_rezept = "Das Rezept " + titel + " wurde erfolgreich zur Datenbank hinzugefügt!"
		titel, zutaten, zubereitung, kcal = daten.rezept_speichern(titel, zutaten, zubereitung, kcal)
		return render_template('neues_rezept.html', bestätigung_rezept=bestätigung_rezept)

	return render_template('neues_rezept.html')



@app.route('/hello/kalorienbilanz.html',  methods=["GET", "POST"])
def mahlzeiten_speichern():
	if request.method == "POST":
		rezept_titel = request.form['rezept_titel']
		data = daten.rezepte_laden()
		kalorien = data[rezept_titel]["kcal"]
		bestätigung_mahlzeit = "Die Mahlzeit " + rezept_titel + " wurde erfolgreich zu deinem Fastentag hinzugefügt!"
		rezept_titel, kalorien = daten.mahlzeiten_speichern(rezept_titel, kalorien)
		mahlzeiten = daten.mahlzeiten_laden()
		kcal_verbraucht = 0
		for kcal in mahlzeiten.values():
			kcal = int(kcal)
			kcal_verbraucht += kcal
		kcal_verbraucht_str = "Du hast heute bereits " + str(kcal_verbraucht) + " gegessen."
		kcal_verfuegbar = 500-kcal_verbraucht
		kcal_verfuegbar_str = "Das heisst, du hast noch " + str(kcal_verfuegbar) + " Kalorien verfügbar heute."
		if kcal_verfuegbar <= 0:
			kcal_ueberschritten = "Das heist, du hast heute deinen Kalorienbedarf um " + str(kcal_verfuegbar) + " überschritten!"
			kcal_verfuegbar = kcal_ueberschritten
			return render_template('kalorienbilanz.html', kcal_ueberschritten=kcal_ueberschritten, kcal_verfuegbar=False, bestätigung_mahlzeit=bestätigung_mahlzeit, kcal_verbraucht_str=kcal_verbraucht_str)
		return render_template('kalorienbilanz.html', bestätigung_mahlzeit=bestätigung_mahlzeit, kcal_verbraucht_str=kcal_verbraucht_str, kcal_verfuegbar_str=kcal_verfuegbar_str)
	return render_template('kalorienbilanz.html')

@app.route('/hello/rezepte.html')
def uebersicht():
    rezepte = daten.rezepte_laden()
    rezepte_liste = ""
    for key, value in rezepte.items():
    	zeichen_laenge = len(key)
    	binde_striche = "_" * (100-zeichen_laenge)
    	titel = key + binde_striche
    	zutaten = rezepte[key]["zutaten"]
    	zubereitung = rezepte[key]["zubereitung"]
    	kcal = rezepte[key]["kcal"]
    	rezepte_liste += titel + " Zutaten: " + zutaten + " // Zubereitung: " + zubereitung + " // Anzahl Kalorien: " + kcal + " // "
    	
    return render_template('rezepte.html', rezepte_liste=rezepte_liste)


"""

    rezepte_liste = ""
    for key, value in rezepte.items():
    	titel = key + " - "
    	rezepte_liste += titel
    	for key, value in rezepte[key].items():
        	zeile = str(key) + ": " + str(value)
        	rezepte_liste += zeile


    return render_template('rezepte.html', rezepte_liste=rezepte_liste)



@app.route('/pandas/')
def pandas():
	data = daten.rezepte_laden()
	data_df = pd.DataFrame(data, colums=[key, value])
	return print(data_df)



@app.route('/hello/neues_rezept.html', methods=["GET", "POST"])
def rezept_hinzufügen():
	if request.method == "POST":
		ende = "Die Rezept-Eingabe wurde beendet!"
		rezepte = {}
		rezept_titel = request.form['titel']
		rezept_zutaten = request.form['zutaten']
		rezept_zubereitung = request.form['zubereitung']
		rezept_kcal = request.form['kcal']
		weiteres_rezept = request.form['mehr']
		while weiteres_rezept != "n":
			for eintrag in request.form:
				rezepte[rezept_titel] = {
					"zutaten": rezept_zutaten,
					"zubereitung": rezept_zubereitung,
					"kcal": rezept_kcal,
				}
				rueckgabe_rezept = "Das Rezept " + rezept_titel + " wurde zur Datenbank hinzugefügt!"
				return render_template('neues_rezept.html', bestätigung_rezept=rueckgabe_rezept, übersicht=rezepte)
		return render_template('neues_rezept.html', ende=ende)
	return render_template('neues_rezept.html')

"""

if __name__ == "__main__":
    app.run(debug=True, port=5000)

"""
	return render_template('neues_rezept.html', bestätigung_rezept=rueckgabe_rezept)
	return render_template('neues_rezept.html')


name abspeichern, dass immer Hallo name kommt -> json
Rezept Übersicht schön darstellen
kalorienbilanz -> pro Nutzer eine eigene Bilanz
Grafik -> im HTML integrieren

"""



