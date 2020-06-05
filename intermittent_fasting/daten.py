import json


def speichern_rezept(datei, titel, zutaten, zubereitung, kcal):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[titel] = {"zutaten": zutaten, "zubereitung": zubereitung, "kcal": kcal} #Aufbau des Json-Files rezepte.json


    # print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)


def rezept_speichern(titel, zutaten, zubereitung, kcal):
    datei_name = "rezepte.json"
    speichern_rezept(datei_name, titel, zutaten, zubereitung, kcal) #daten an funktion speichern_rezepte übergeben
    return  titel, zutaten, zubereitung, kcal


def rezepte_laden():
    datei_name = "rezepte.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)


def speichern_mahlzeiten(datei, key, value):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[key] = value 

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)


def mahlzeiten_speichern(tag, username, rezept_titel, kalorien):
    datei_name = "mahlzeiten-" + username + "-" + str(tag) + ".json" #für jeden Nutzer und jeden Tag ein neues json-File erstellen
    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        with open(datei_name, "w") as open_file:
            open_file.write("{}")
    speichern_mahlzeiten(datei_name, rezept_titel, kalorien)
    return  rezept_titel, kalorien


def mahlzeiten_laden(username, tag):
    datei_name = "mahlzeiten-" + username + "-" + str(tag) + ".json"
    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)





