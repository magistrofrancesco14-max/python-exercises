
# * for loop si usa quando sai già quante volte vuoi ripetere qualcosa oppure vuoi scorrere una lista.
for numbers in range(11):
    print(numbers)

# Scorrere lista
lista_citta = ["Milano, Roma, Torino"]

for citta in lista_citta: # per ogni elemento della lista (elemento si può chiamare come si vuole, la variabile deve esistere)
    print(citta)

print('')

# * loop while si usa quando vuoi ripetere qualcosa finché una condizione è vera.
x = 1
while x <= 5:
    print(x)
    x += 1 # significa: prendi x e aggiungi 1 (se non si mettesse la riga il loop sarebbe all'infinito)

print('')

for ex in range(1, 21):
    if ex % 2 == 0: 
        print(ex, 'Pari')
    else: 
        print(ex, 'Dispari')

print('')

for ex in range(1, 21):
    if ex % 2 == 0:
        print(ex)

# * Break
x = 1
while x <= 5:
    print(x)
    if x == 3:
        break
    x += 1
