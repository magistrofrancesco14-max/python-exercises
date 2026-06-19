# Scrivi un programma "moltiplicatore" che, 
# data una lista di numeri, moltiplichi tra loro tutti gli elementi.

lista_numeri = [3, 5, 8, 20]
risultato = 1

for numero in lista_numeri:
    risultato *= numero
print("Il risultato della moltiplicazione della lista è..." + str(risultato))

# Soluzione

lista = [7, 66, 100, 457, 472]
risultato = 1
for numero in lista:
    if numero != 0: # non uguale a 0
        risultato *= numero
print("Il risultato della moltiplicazione tra tutti gli elementi della lista è... " + str(risultato))