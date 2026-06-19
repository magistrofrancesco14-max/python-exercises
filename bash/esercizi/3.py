# Scrivi un programma che, data una lista di numeri, 
# fornisca in output il maggiore tra tutti gli elementi della lista

# Soluzione

lista_numeri = [42, 9, 23, 11, 17, 56, 3]
numero_maggiore = lista_numeri[0] # per ora considero come numero più grande il primo della lista, serve perché devi partire da un valore di riferimento per confrontare gli altri
for numero in lista_numeri: # questo ciclo prende uno alla volta tutti i numeri della lista
    # qui sta il cuore del programma: confronti ogni elemento della lista (numero) con il massimo trovato finora (numero_maggiore = 42) 
    # se trovi un numero più grande aggiorni numero_maggiore
    if numero > numero_maggiore: 
        numero_maggiore = numero
print("Il numero maggiore tra tutti è:", numero_maggiore)


# Scrivi un programma che, data una lista di numeri, 
# fornisca in output il minore tra tutti gli elementi della lista.

lista = [42, 9, 23, 11, 17, 56, 3]

numero_minore = lista[0]
for n in lista:
    if n < numero_minore:
        numero_minore = n
print("Il numero minore tra tutti è:", numero_minore)