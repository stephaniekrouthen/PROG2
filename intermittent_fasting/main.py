from flask import Flask
from flask import render_template
from flask import request
import daten
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot

app = Flask("Intermittent Fasting")

"""
def data():
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

	fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
	fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20, marker=dict(colors=colors, line=dict(color='#000000', width=2)))

	div = plot(fig, output_type="div")
	return div

@app.route("/")
def index():
	div = viz()
	return render_template("index.html", viz_div=div)
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

	fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
	fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20, marker=dict(colors=colors, line=dict(color='#000000', width=2)))
	fig.show()


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

		kalorienbilanz = 0
		for kcal in mahlzeiten.values():
			kcal = int(kcal)
			kalorienbilanz += kcal
		return render_template('kalorienbilanz.html', bestätigung_mahlzeit=bestätigung_mahlzeit, kalorienbilanz=kalorienbilanz,)

	return render_template('kalorienbilanz.html')



@app.route('/hello/rezepte.html')
def uebersicht():
    rezepte = daten.rezepte_laden()

    rezepte_liste = ""
    for key, value in rezepte.items():
    	titel = key + " - "
    	rezepte_liste += titel
    	for key, value in rezepte[key].items():
        	zeile = str(key) + ": " + str(value)
        	rezepte_liste += zeile


    return render_template('rezepte.html', rezepte_liste=rezepte_liste)


"""
@app.route('/pandas/')
def data():
	data = daten.rezepte_laden()
	data_df = pd.DataFrame(data)
	return print(data)



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



