# Scrivi una funzione che restituisca la lunghezza di una stringa o lista passata come parametro.
# In sostanza, seppur presente, provate a scrivere la nostra versione della funzione len!

lista_citta = ["Milano", "Roma", "Napoli"]

def lunghezza_lista(lista_citta):
    for citta in lista_citta:
        count +=0
        print(citta)

lunghezza_lista(lista_citta)

# Soluzione

def my_len(lst_or_str):
    length = 0
    for unit in lst_or_str:
        length += 1
    return length