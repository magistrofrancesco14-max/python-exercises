# Scrivi un programma che chieda due numeri all'utente tramite la funzione input e mostri il più grande tra i due utilizzando la funzione print

playerchoice1 = input("Scrivi un numero: ")
playerchoice2 = input("Scrivi un'altro numero: ")

def due_numeri():
    if playerchoice1 > playerchoice2:
        print(playerchoice1)
    elif playerchoice2 < playerchoice1:
        print(playerchoice2)

due_numeri()

# Soluzione

a = int(input("Inserisci il primo numero: "))
b = int(input("Inserisci il secondo numero: "))

if a == b:
    print("I numeri sono identici")
elif a > b:
    print("Il numero più grande tra i due è " + str(a))
else:
    print("Il numero più grande tra i due è " + str(b))