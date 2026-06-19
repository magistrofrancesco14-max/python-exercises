# Scrivi una funzione che, a scelta dell'utente, calcoli l'area di:
# un cerchio
# un quadrato
# un rettangolo
# un triangolo

import math

scelta = input("Ciao, di quale figura vuoi calcolare l'area: cerchio, quadrato, rettangolo, tringolo: ")

def area(scelta):
    if scelta == "cerchio":
        raggio = float(input("raggio: "))
        area_cerchio = math.pi * (raggio ** 2)
        print(f"Area cerchio = {round(area_cerchio, 2)}")
    elif scelta == "quadrato":
        lato = float(input("Lato: "))
        area_quadrato = lato ** 2
        print(f"Area quadrato = {area_quadrato}")
    elif scelta == "rettangolo":
        base_rettangolo = float(input("Base: "))
        altezza_rettangolo = float(input("Altezza: "))
        area_rettangolo = base_rettangolo * altezza_rettangolo
        print(f"Area rettangolo: {area_rettangolo}")
    elif scelta == "triangolo":
        base_triangolo = float(input("Base: "))
        altezza_triangolo = float(input("Altezza: "))
        area_triangolo = base_triangolo * altezza_triangolo / 2
        print(f"Area triangolo: {area_triangolo}")

area(scelta)    

# Soluzione

def geometra():
    print("""
    Benvenuti alla funzione Geometra!
    In fase di selezione, a ciascun possibile calcolo corrisponde un valore numerico:
    - Area Quadrato: 1
    - Area Rettangolo: 2
    - Area Triangolo: 3
    - Area Cerchio: 4
    """)

    print('Dunque. Di quale figura geometrica desideri calcolare l\'area?')
    scelta = int(input(">>> "))
    if scelta == 1:
        print("Hai scelto: Area Quadrato")
        lato = float(input('Inserisci il valore del lato del quadrato '))
        print(f"L'Area del Quadrato, avente lato {lato} è: {lato * lato}")
    elif scelta == 2:
        print("Hai scelto: Area Rettangolo")
        base = float(input('Inserisci il valore della base '))
        altezza = float(input('Inserisci il valore dell´altezza '))
        print(f"L'Area del Rettangolo, avente base {base} e altezza {altezza} è: {base * altezza}")
    elif scelta == 3:
        print("Hai scelto: Area Triangolo")
        base = float(input('Inserisci il valore della base '))
        altezza = float(input('Inserisci il valore dell´altezza '))
        print(f"L'Area del Triangolo, avente base {base} e altezza {altezza} è: {(base * altezza) / 2}")
    elif scelta == 4:
        print("Hai scelto: Area Cerchio")
        r = float(input('Inserisci il valore del raggio '))
        print(f"L'Area del Cerchio, avente raggio {r} è: {(r * r) * 3.14}")
    else:
        print ('Nessun calcolo disponibile per la scelta effettuata!')