import random as rd
import time
import Karte
import Funktionen as fk

todesnachrichten = (
    "ist leider von uns gegangen. ", "lebt nicht mehr.", "stuerzte zu Tode.", "Wurde von Schlamm verschluckt",
    "wurde zu Muß verarbeitet")


class Spieler:
    def __init__(self, name, geschlecht, alter, geschicklichkeit, staerke):
        self.name = name
        self.geschlecht = geschlecht
        self.geschicklichkeit = geschicklichkeit
        self.alter = alter
        self.leben = 30
        self.lebend = 1
        self.staerke = staerke
        self.angriffschaden = (self.geschicklichkeit * 0.05 + 2) * (self.staerke * 0.07 + 2)
        self.ruestung = 0
        self.maximalesleben = 30
        self.standort = (4, 3)

    def sterben(self, todesnachricht):
        print(self.name, todesnachrichten[todesnachricht])
        self.lebend -= 1

    def fortschreiten(self, schwierigkeit, gefahrenfaktor):
        entscheidendeNr = rd.randint(self.geschicklichkeit, schwierigkeit)
        if entscheidendeNr > (schwierigkeit * (gefahrenfaktor)):
            return True
        else:
            return False

    def kaempfen(self, gegner, gegnerexistenz):

        while gegner.leben > 0 and self.leben > 0:
            print("Du hast", int(self.leben), "Leben.")
            print("Dein Gegner", int(gegner.leben), "Leben")
            time.sleep(4)
            treffer_self = rd.randint(self.geschicklichkeit, int(20 + gegner.ruestung))
            treffer_gegner = rd.randint(gegner.geschicklichkeit, int(20 + self.ruestung))
            if treffer_gegner > (10 + self.ruestung):
                self.leben -= gegner.angriffschaden

            if treffer_self > (10 + gegner.ruestung):
                gegner.leben -= self.angriffschaden

        if gegner.leben <= 0:
            print("Du hast gewonnen!")
            gegner.sterben(gegnerexistenz)
            return True


        if self.leben <= 0:
            self.sterben(4)

    def bewegen(self, richtung):

        if richtung in Karte.richtungen:
            bewegunsrichtung = Karte.richtungen[richtung]
            neuerStandort = (
                self.standort[0] + bewegunsrichtung[0],
                self.standort[1] + bewegunsrichtung[1])

            if fk.ob_in_karte(neuerStandort, Karte.KoordinatenGrenze) is True:
                neuerStandort = self.standort
                print("du Hast den Rand der Karte erreichst und kannst nicht mehr weitergehen")

            return neuerStandort

        else:
            print("Es faellt mir schwer nach", richtung, " zu laufen. Moegliche Richtungen: nord, ost, sued, west")
            return self.standort

    def wo(self):
        ort = Karte.karte[self.standort[0]][self.standort[1]]
        return ort


class Monster:
    def __init__(self, leben, geschicklichkeit, staerke, ruestung = 0):
        self.leben = leben
        self.geschicklichkeit = geschicklichkeit
        self.ruestung = ruestung
        self.staerke = staerke
        self.angriffschaden = (self.geschicklichkeit * 0.03 + 3) * (self.staerke * 0.1 + 1)
        self.standort = (rd.randint(Karte.KoordinatenGrenze[0], Karte.KoordinatenGrenze[1]),
                         rd.randint(Karte.KoordinatenGrenze[0], Karte.KoordinatenGrenze[1]))

    def sterben(self, existenz):
        existenz.remove(self)
        pass

    def bewegen(self):
        richtung = fk.zufaellige_richtung()
        bewegunsrichtung = Karte.richtungen[richtung]
        neuerStandort = (
            self.standort[0] + bewegunsrichtung[0],
            self.standort[1] + bewegunsrichtung[1])

        if fk.ob_in_karte(neuerStandort, Karte.KoordinatenGrenze) is True:
            neuerStandort = self.standort

        return neuerStandort


class Zombie(Monster):
    def __init__(self, leben, geschicklichkeit, staerke):
        super(Zombie, self).__init__(leben, geschicklichkeit, staerke, 1)


class NPC:
    pass


class Haendler(NPC):
    pass
