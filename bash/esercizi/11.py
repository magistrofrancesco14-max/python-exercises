# Scrivi una funzione che, data una stringa come parametro, restituisca un dizionario rappresentante la "frequenza di comparsa" di ciascun carattere componente la stringa.
# Per fare un esempio, data una stringa "ababcc", otterremo in risultato {"a": 2, "b": 2, "c": 2}

stringa = "ababcc"

def dizionario(stringa):
    dizionario = {}
    for lettera in stringa:
        if lettera in dizionario:
            dizionario[lettera] += 1
        else:
            dizionario[lettera] = 1
    return dizionario  

print(dizionario(stringa))

def frequenza(stringa):
    contatore = {}
    for lettera in stringa:
        contatore[lettera] = contatore.get(lettera, 0) + 1
    return contatore