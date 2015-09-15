import random as rd
import Klassen
import Funktionen as fk

def spieler_erstellen():
    name = input("Wie meochtest du heißen?")

    geschlecht = ""
    moegl_geschlechter = ("maennlich","weiblich","leo","zwitter")
    while geschlecht not in moegl_geschlechter:
        geschlecht = input("Welches Geschlecht bist du?(maennlich/weiblich)")
        geschlecht = fk.text_anpassen(geschlecht)

    geschicklichkeit = rd.randint(2,7)
    staerke = rd.randint(2,7)
    alter = rd.randint(17,42)
    spieler = Klassen.Spieler(name,geschlecht,alter,geschicklichkeit,staerke)
    print ("Hallo,",spieler.name," du bist",spieler.alter,"Jahre alt und",spieler.geschlecht)
    return spieler

def zombie_erstellen(position):
    geschicklichkeit = rd.randint(2,4)
    staerke = rd.randint(2,12)
    leben = 15
    name = "Zombie"+str(position)
    zombie = Klassen.Zombie(leben,geschicklichkeit,staerke,name)
    return zombie