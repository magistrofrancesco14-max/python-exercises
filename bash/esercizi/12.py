# Scrivi una funzione che, dato in ingresso un valore espresso in metri, mandi in print l'equivalente in miglia terrestri, iarde, piedi e pollici.

a = int(input("Scrivi un valore in metri e ti verrà restituito in miglia, iarde, piedi e pollici: "))

def americana(a):
    miglia = a * 0.000621371 # fattore di conversione
    iarde = a * 1.0936132983 # fattore di conversione
    piedi = a * 3.28084 # fattore di conversione
    pollici = a * 39.3701 # fattore di conversione
    print(f"Miglia: {round(miglia, 4)}") # round() per arrontondare ed evitare troppi decimali
    print(f"iarde: {iarde}")
    print(f"piedi: {piedi}")
    print(f"pollici: {pollici}")
    
americana(a)