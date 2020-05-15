from flask import Flask
from flask import render_template
from flask import request
import daten
import pandas as pd

app = Flask("Intermittent Fasting")

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
		return render_template('kalorienbilanz.html', bestätigung_mahlzeit=bestätigung_mahlzeit, kalorienbilanz=kalorienbilanz, )

	return render_template('kalorienbilanz.html')



@app.route('/hello/rezepte.html')
def uebersicht():
    rezepte = daten.rezepte_laden()

    rezepte_liste = ""
    for key, value in rezepte.items():
    	titel = key + " - "
    	rezepte_liste += titel
    	for key, value in rezepte[key].items():
        	zeile = str(key) + ": " + str(value) + "\n"
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


Für mehrere Rezepte, Schleifen?
Das Dict rezept muss irgendwo abgespeichert werden, damit es dann im mahlzeit_hinzufügen.html abgerufen werden kann 
und damit mehrere Dicts erstellt werden können.
rekursive funktion
"""



