import json


def speichern_rezept(datei, titel, zutaten, zubereitung, kcal): #daten in Klammern wurde von der Funktion rezept_speichern übergeben
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[titel] = {"zutaten": zutaten, "zubereitung": zubereitung, "kcal": kcal} #Aufbau des Json-Files rezepte.json

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)


def rezept_speichern(titel, zutaten, zubereitung, kcal): #die Daten in der Klammer wurden von main.py an diese Funktion übergeben
    datei_name = "rezepte.json"
    speichern_rezept(datei_name, titel, zutaten, zubereitung, kcal) #daten an funktion speichern_rezepte übergeben
    return  titel, zutaten, zubereitung, kcal


def rezepte_laden(): #den Inhalt des rezepte.json aufrufen können
    datei_name = "rezepte.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)


def speichern_mahlzeiten(datei, key, value): #daten in klammer von mahlzeiten_speichern übergeben
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[key] = value #key ist Rzepttitel und value ist Azahl kcal

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)


def mahlzeiten_speichern(tag, username, rezept_titel, kalorien): #Daten in der Klammer von main.py übergeben
    datei_name = "mahlzeiten-" + username + "-" + str(tag) + ".json" #für jeden Nutzer und jeden Tag ein neues json-File erstellen
    try:
        with open(datei_name) as open_file: #überprüfen ob es schon ein Json-File für diesen Nutzer und diesen Tag gibt
            datei_inhalt = json.load(open_file)
    except FileNotFoundError: #ansonsten ein neues File für Nutzer un Tag erstellen
        with open(datei_name, "w") as open_file:
            open_file.write("{}")
    speichern_mahlzeiten(datei_name, rezept_titel, kalorien) #daten in Klammern an speichern_mahlzeiten übergeben
    return  rezept_titel, kalorien


def mahlzeiten_laden(username, tag): #daten in klammer von main.py erhalten
    datei_name = "mahlzeiten-" + username + "-" + str(tag) + ".json"
    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt #den Inhalt des rezepte.json aufrufen können

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)





