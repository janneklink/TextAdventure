
from Erstellen import spieler_erstellen,zombie_erstellen
import Funktionen as fk
import random as rd



def main():
    while True:

        if spieler.lebend <= 0:
            break
        eingabe = input("Was willst du tun?")
        eingabe = fk.text_anpassen(eingabe)
        zombie = zombie_erstellen()
        monsterliste =[zombie]
        if rd.randint(0,4) == 4:
            monsterliste.append(zombie_erstellen())
        for monster in monsterliste:
            monster.standort = monster.bewegen()
            if monster.standort == spieler.standort:
                monsterexistenz = spieler.kaempfen(monster)
                if monsterexistenz is False:
                    monsterliste.remove(monster)
        if spieler.leben < spieler.maximalesleben:
            spieler.leben += 2

#        if eingabe == "kaempfen" :
#            monster = zombie_erstellen()
#            spieler.kaempfen(monster)

        if eingabe.startswith("gehen"):

            if eingabe == "gehen":
                aktuelleRichtung = input("gehen? In welche Richtung(nord/ost/sued/west)")

            elif eingabe.startswith("gehen "):
                aktuelleRichtung = eingabe[6:]

            else:
                aktuelleRichtung = eingabe[5:]

            if aktuelleRichtung == "himmel" or aktuelleRichtung == "hoelle":

                spieler.sterben(0, spieler.name)

                if spieler.lebend <= 0:
                    break
            vorherigerstandort = spieler.standort
            spieler.standort = spieler.bewegen(aktuelleRichtung)
            print("Du bist jetzt: ", (spieler.wo().name))

            bleiben = spieler.wo().verhalten(spieler)
            if bleiben is True:
                spieler.standort = vorherigerstandort
                print("Dein Standort ist:",(spieler.wo().name))
            else:
                pass

        if eingabe == "stop":
            print("Auf Wiedersehen.")
            break

        if eingabe == "wo":
            print(spieler.wo().name)
            print(spieler.wo().beschreibung)



if __name__ == "__main__":
    spieler = spieler_erstellen()
    main()
