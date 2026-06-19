persona = {
    "nome": "Luca",
    "cognome": "Rossi",
    "eta": 25,
}

operazioni = ("aggiungere", "modificare", "eliminare", "uscire")

def start():
    operazione = input("Cosa vuoi fare? ")
    if operazione == operazioni[0]:
        x = input("Scrivi chiave:valore separati da una virgola: ")
        aggiungi(x.split(","))
    elif operazione == operazioni[1]:
        x = input("Scrivi chiave:valore separati da una virgola: ")
        modifica(x.split(","))
    elif operazione == operazioni[2]:
        x = input("Scrivi la chiave da eliminare: ")
        elimina(x)
     
def aggiungi(param):
    chiave = param[0]
    valore = param[1]
    persona[chiave] = valore
    print(persona)

def modifica(param):
    chiave = param[0]
    valore = param[1]
    if chiave in persona:
        persona[chiave] = valore
        print(persona)
    else: print("Chiave non trovata")

def elimina(chiave):
    chiave = chiave.strip()
    if chiave in persona:
        del persona[chiave]
        print(persona)
    else: print("Chiave non trovata")

while True:
    start()
