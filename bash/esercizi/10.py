# Scrivi una funzione che data in ingresso una lista A contenente n parole, 
# restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.

lista_a = ["an", "brt", "cedg", "d", "eqwert"]

def char_counter(lista_a):
    lista_b = []
    for parola in lista_a:
        lista_b.append(len(parola))
    return lista_b

risultato = char_counter(lista_a)
print(risultato)


