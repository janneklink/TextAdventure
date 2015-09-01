def text_anpassen(text):
    text = text.lower()
    text = text.strip()
    return text

def ja_nein_frage(frage):
    antwort = input(frage)
    antwort = text_anpassen(antwort)
    if antwort =="ja":
        return True
    elif antwort =="nein":
        return False
    else :
        print("Bitte antworte mit ja oder nein.")
        return ja_nein_frage(frage)

def ob_in_karte(standort,kartengrenze):
    if (standort[0] < kartengrenze[0]
            or standort[1] > kartengrenze[1]
            or standort[1] < kartengrenze[0]
            or standort[0] > kartengrenze[1]  ):
        return True
