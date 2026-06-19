
# # Set
# collezioni di dati non ordinate, non indicizzate, non modificabili e senza duplicati
from curses import meta


citta = {'Milano', 'Roma', 'Napoli'}
print(citta)


# # Dictionary
# collezioni di dati per memorizzare coppie chiave valori,
# invece di usare indici numerici come nelle liste, usi una chiave per accedere al valore.

studente = {
    'nome': 'Francesco',
    'eta': 30,
    'corso': 'Informatica'
}
# nome, età e corso sono le chiavi
# Francesco, 25 e informatica sono i valori

# mandare a schermo valori
print(studente['nome'])
print(studente.get('eta'))

studente['nome'] = 'Andrea' # modificare dato
studente['città'] = 'Milano' # aggiungere dato
del studente['città'] # eliminare chiave
studente_copia = studente.copy() # creare una copia

print(studente['nome'])

# ! Esercizio
utenti_raw = ["Anna", "Luca", "Anna", "Marco", "Luca", "Giulia"]
print(utenti_raw)
utenti_unici = set(utenti_raw) # trasfomo la lista in set per eliminare i duplicati
utenti_clean = list(utenti_unici) # trasformo il set in lista 
utenti_clean.sort() # ordino la lista in ordine alfabetico
print(utenti_clean)
for nome in utenti_clean:    
    if nome.startswith('A'):
        print(nome)
