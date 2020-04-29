from flask import Flask
from flask import render_template
from flask import request

app = Flask("Intermittent Fasting")


@app.route('hello/<name>')
def hello(name):
	return render_template('index.html', name + "!")

@app.route('/neues_rezept', methods=["GET", "POST"])
def rezept():
	if request.method == "POST":
		rezept = request.from.to_dict()
		rezept["rezepttitel"] = rezepttitel
		rezept["zutaten"] = zutaten
		rezept["zubereitung"] = zubereitung
		rezept["kcal"] = kcal
		rueckgabe_rezept = "Das Rezept" + rezepttitel + "wurde erfolgreich hinzugefügt!"
		print(rezept)
		return rueckgabe_rezept
	return render_template('index/neues_rezept.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
