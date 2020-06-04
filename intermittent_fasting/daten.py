import json

def speichern_namen(datei, value):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt["name"] = value

def namen_speichern(name):
    datei_name = "namen.json"
    speichern_namen(datei_name, name)
    return name

def speichern_rezept(datei, titel, zutaten, zubereitung, kcal):
    try:
        with open(datei) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    datei_inhalt[titel] = {"zutaten": zutaten, "zubereitung": zubereitung, "kcal": kcal}


    # print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)


def rezept_speichern(titel, zutaten, zubereitung, kcal):
    datei_name = "rezepte.json"
    speichern_rezept(datei_name, titel, zutaten, zubereitung, kcal)
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


    # print(datei_inhalt)

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)


def mahlzeiten_speichern(rezept_titel, kalorien):
    datei_name = "mahlzeiten.json"
    speichern_mahlzeiten(datei_name, rezept_titel, kalorien)
    return  rezept_titel, kalorien


def mahlzeiten_laden():
    datei_name = "mahlzeiten.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt

    with open(datei, "w") as open_file:
        json.dump(datei_inhalt, open_file)

def benutzer_speichern(username):
    datei_name = "mahlzeiten" + username + ".json"


