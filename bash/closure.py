
# # Una closure è una funzione che “ricorda” le variabili del contesto in cui è stata creata, anche dopo che quel contesto non esiste più.
# # è una funzione dentro un’altra funzione che si porta dietro i dati della funzione esterna

# Esercizio contatore
def contatore():
    count = 0

    def incrementa():
        nonlocal count # modificare una variabile che sta nella funzione esterna
        count +=1
        return count

    return incrementa

c = contatore()
print(c())
print(c())

# Esercizio somma (non serve nonlocal perchè non si modifica x)
def crea_somma(x):
    def somma(y):
        return x + y
    return somma

add10 = crea_somma(10)
print(add10(5)) 

# Esercizio moltiplicatore (non serve nonlocal perchè non si modifica n)
def moltiplicatore(n):
    def moltiplica(x):
        return n * x
    return moltiplica

per3 = moltiplicatore(3)
print(per3(5)) 

