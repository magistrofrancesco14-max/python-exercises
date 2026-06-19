# Scrivi un semplice programma che, data una lista di numeri, sommi tra loro tutti gli elementi

lista_numeri = [1, 3, 5, 10]
somma = sum(lista_numeri)

print(somma)

# Soluzione

lista = [3, 6, 100, 23, 42]
risultato = 0
for numero in lista:
    risultato += numero
print("Il risultato della somma è... " + str(risultato))