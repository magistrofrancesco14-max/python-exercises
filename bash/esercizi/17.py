# Scrivi una funzione che, dato un carattere in ingresso, restituisca in output il codice ASCII associato al carattere passato.

def ascii():
    dati_ingresso = input("Scrivi un carattere: ")
    return ord(dati_ingresso) # converte il carattere in ingresso in codice ASCII. Return va chiamato sul input

print(ascii())

# Soluzione

def trova_ascii():
    carattere = input("Inserisci il carattere che ti interessa convertire: ")
    valore = ord(carattere)
    output = f"Il valore ASCII associato a '{carattere}' è {valore}"
    return output
print(trova_ascii())