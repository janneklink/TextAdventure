import Funktionen as fk

richtungen = {"nord": [0, -1], "ost": [-1, 0], "sued": [0, 1], "west": [1, 0]}


class EinfacherOrt:
    def __init__(self, name, beschreibung=""):
        self.name = name
        self.beschreibung = beschreibung

    def __str__(self):
        return self.name

    def verhalten(self, spieler):
        pass


class Schlucht(EinfacherOrt):
    def __init__(self):
        super(Schlucht, self).__init__("Schlucht", "Du stehst vor einer tiefen Schlucht.")

    def verhalten(self, spieler):
        ueberquerung = fk.ja_nein_frage("Moechtest du die Schlucht durchklettern(ja/nein)")

        if ueberquerung is True:
            erfolg = spieler.fortschreiten(50, 3/4)
            if erfolg is False:
                spieler.sterben(2)

            else:
                print("Du hast die Schlucht erfolgreich durchklettert.(+2 geschicklichkeit)")
                spieler.geschicklichkeit += 2

        elif ueberquerung is False:
            print("Du kehrst lieber um.")
            return True


class Berge(EinfacherOrt):
    def __init__(self):
        super(Berge, self).__init__("Berge", "Du siehst gigantische Berge in den Himmel aufragen.")


    def verhalten(self, spieler):
        besteigen = fk.ja_nein_frage("Moechtest du die Berge ueberqueren?")
        if besteigen is True:
            erfolg = spieler.fortschreiten(15, 3/4)
            if erfolg is True:
                spieler.staerke += 0.5
                print("Von der Spitze des Berges hast du eine wunderbare Aussicht.(+0,5 staerke)")
            elif erfolg is False:
                spieler.staerke -= 1.25
                print ("Du bist abgestuerzt und verlierst, waehrend deiner Genesung staerke.(-1,25 staerke)")
        elif besteigen is False:
            print ("Da du die Berge nicht ueberqueren willst kehrst du um.")
            return True


class Wald(EinfacherOrt):
    def __init__(self):
        super(Wald, self).__init__("Wald", "Du wirst doch wohl wissen wie ein Wald aussieht. Viele Baeume und sonst nicht besonders viel.")

class Moor(EinfacherOrt):
    def __init__(self):
        super(Moor, self).__init__("Moor" ,"Du siehst eine Schlammige und matschige Gegend.")
    def verhalten(self, spieler):
        durchqueren = fk.ja_nein_frage("Moechtest du das Moor auf die Gefahr zu versinken durchqueren?")
        if durchqueren is True:
            erfolg = spieler.fortschreiten(50, 1/2)
            if erfolg is True:
                spieler.geschicklichkeit +=2
                print ("Du bist erfolgreich duch dieses Moor geschritten(+2 geschicklichkeit)")
            elif erfolg is False:
                spieler.sterben(3)
        if durchqueren is False:
            print ("Du kehrst um, weil du nicht riskieren moechtest vom Moor verschluckt zu werden")
            return True

class Fluss(EinfacherOrt):
    def __init__(self):
        super(Wald, self).__init__()

    def verhalten(self, spieler):
        durchqueren = fk.ja_nein_frage("Moechtest du durch den reißenden Fluss schwimmen?")
        if durchqueren is True:
            erfolg = spieler.fortschreiten(50, 1/2)
            if erfolg is True:
                spieler.geschicklichkeit +=2
                print ("")
            elif erfolg is False:
                spieler.sterben(3)
        if durchqueren is False:
            print ("Du kehrst um, weil du nicht riskieren moechtest vom Moor verschluckt zu werden")
            return True

                # osten


null = [Wald(), Wald(), Wald(), Moor(), Moor() ,EinfacherOrt("Wiese"), EinfacherOrt("Wiese"), Berge()]
eins = [EinfacherOrt("Wiese"), EinfacherOrt("Wiese"), Wald(), Moor(), EinfacherOrt("Wiese"), EinfacherOrt("Wiese"), Berge(), Schlucht()]
zwei = [Berge(), EinfacherOrt("Wiese"), Wald(), Wald(), Wald(), Wald(), Berge(), Schlucht()]
drei = [Schlucht(), Berge(), Wald(), EinfacherOrt("Lichtung"), Wald(), Berge(), Berge(), Schlucht()]
vier = [Berge(), Schlucht(), Berge(), EinfacherOrt("Spawnpunkt"), Wald(), Berge(), Berge(),Berge()]  # sueden
fuenf = [Berge(), Berge(), Berge(), Wald(), Wald(), Berge(), EinfacherOrt("Tal"), EinfacherOrt("Tal")]
sechs = [Berge(), Berge(), Wald(), EinfacherOrt("Felder"), EinfacherOrt("Felder"), EinfacherOrt("Fluss"),Berge(), EinfacherOrt("Tal")]
sieben = [Berge(), Wald(), Wald(), EinfacherOrt("Felder"), Wald(), Wald(), EinfacherOrt("Fluss"), EinfacherOrt("Fluss")]

acht = [Wald(), Wald(), EinfacherOrt("Felder"), EinfacherOrt("Felder"),
        Wald(), Wald(), EinfacherOrt("Fluss"), EinfacherOrt("Wiese"), Wald(),
        EinfacherOrt("Felder"), EinfacherOrt("Felder"), EinfacherOrt("Meer"), EinfacherOrt("Meer"),
        EinfacherOrt("Meer")]
neun = [Wald(), Wald(), EinfacherOrt("Dschungel"), EinfacherOrt("Dschungel"),
        EinfacherOrt("Felder"), EinfacherOrt("Felder"), EinfacherOrt("Fluss"), EinfacherOrt("Wiese"),
        Wald(), Wald(), EinfacherOrt("Wiese"), EinfacherOrt("Meer"), EinfacherOrt("Meer")]
zehn = [EinfacherOrt("Dschungel"), EinfacherOrt("Dschungel"), EinfacherOrt("Dschungel"), EinfacherOrt("Dschungel"),
        EinfacherOrt("Felder"), EinfacherOrt("Fluss"), EinfacherOrt("Fluss"), EinfacherOrt("Fluss"),
        EinfacherOrt("Felder"), EinfacherOrt("Wiese"), EinfacherOrt("Wiese"), EinfacherOrt("Wiese"),
        EinfacherOrt("Meer")]
elf = [Moor(), Moor(), EinfacherOrt("Dschungel"), EinfacherOrt("Felder"),
       EinfacherOrt("Felder"), EinfacherOrt("Fluss"), EinfacherOrt("Berge"), EinfacherOrt("Fluss"),
       EinfacherOrt("Fluss"), EinfacherOrt("Berg"), EinfacherOrt("Wiese"), EinfacherOrt("Wiese"), EinfacherOrt("Meer")]
zwoelf = [Moor(), Moor(), Moor(), EinfacherOrt("Wiese"),
          EinfacherOrt("Wiese"), EinfacherOrt("Fluss"), EinfacherOrt("Berge"), EinfacherOrt("Berge"),
          EinfacherOrt("Fluss"), EinfacherOrt("Fluss"), EinfacherOrt("Fluss"), EinfacherOrt("Fluss"),
          EinfacherOrt("Fluss")]

# westen

karte = [null, eins, zwei, drei, vier, fuenf, sechs, sieben]

KoordinatenGrenze = (0, len(karte) - 1)
