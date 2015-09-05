
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
        monsterliste = [zombie]
        if spieler.leben < spieler.maximalesleben:
            spieler.leben += 2

        if eingabe.startswith("gehen"):

            if eingabe == "gehen":
                aktuelleRichtung = input("gehen? In welche Richtung(nord/ost/sued/west)")

            elif eingabe.startswith("gehen "):
                aktuelleRichtung = eingabe[6:]

            else:
                aktuelleRichtung = eingabe[5:]

            if aktuelleRichtung == "himmel" or aktuelleRichtung == "hoelle":

                spieler.sterben(0)

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

            monsterentstehung = rd.randint(0, 4)
            if monsterentstehung == 4:
                monsterliste.append(zombie_erstellen())
            for monster in monsterliste:
                monster.standort = monster.bewegen()
                if monster.standort == spieler.standort:
                    print(
                    "Plötzlich taucht ein Gestalt auf welche auf dich zugerannt kommt und anfängt dich zu attackieren.")
                    spieler.kaempfen(monster, monsterliste)


        if eingabe.startswith("stop"):
            beenden = fk.ja_nein_frage("Moechtest du das Spiel wirklich verlassen?")
            if beenden is True:
                print("Auf Wiedersehen.")
                break

        if eingabe.startswith("wo"):
            print(spieler.wo().name)
            print(spieler.wo().beschreibung)

        if eingabe.startswith("help"):
            print(
                "Du kannst gehen, indem du 'gehen' und danach die Himmelsrichtung,in welche du gehen willst, schreibst.")
            print("Mit dem Befehl 'wo' erfaerst du wo du bist.")
            print(
                "Und wenn du das Spiel verlassen moechtest schreibe einfach, wenn du gefragt wirst was du tun willst, 'stop'.")



if __name__ == "__main__":
    spieler = spieler_erstellen()
    main()
