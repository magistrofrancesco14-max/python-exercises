# Scrivi una semplice funzione che converta un dato numero di giorni, ore e minuti, 
# passati dall'utente tramite funzione input, in secondi.

giorni = int(input("Giorni: "))
ore = int(input("Ore: "))
minuti = int(input("Minuti: "))

def conversione(giorni, ore, minuti):
    giorno = giorni * 86400
    ora = ore * 3600
    minuto = minuti * 60
    print(f"Totale secondi: {giorno + ora + minuto}")

conversione(giorni, ore, minuti)