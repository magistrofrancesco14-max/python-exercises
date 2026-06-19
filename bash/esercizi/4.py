# Scrivi un programma che chieda all'utente 
# una stringa composta da un solo carattere e dica se si tratta di una vocale oppure no.

input_utente = str(input("Scrivi un solo carattere e vediamo se si tratta di una vocale oppure no: "))

vocali = ["a, e, i, o, u"]

for input_utente in vocali:
    if input_utente == vocali:
        print("Si è una vocale")
    else:
        print("No non è una vocale")

# Soluzione

carattere = input("Inserisci un carattere: ").lower()
vocali = "aeiou"

if carattere in vocali:
    print(f"Il carattere '{carattere}' è una vocale")
else:
    print(f"Il carattere '{carattere}' non è una vocale")