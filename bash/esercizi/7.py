# Scrivi un programma che a partire da un elemento e una lista di elementi dica in output 
# se l'elemento passato sia presente o meno nella lista.
# Qualora l'elemento sia presente nella lista, il programma dovrà comunicarci l'indice dell'elemento

elemento1 = 30
elemento2 = 10
lista_elementi = [3, 5, 10]

if elemento1 in lista_elementi:
    print("L'elemento è nella lista" + str(lista_elementi.index(elemento1)))
else:
    print("L'elemento non è nella lista")

if elemento2 in lista_elementi:
    print("L'elemento è nella lista, all'indice ..." + str(lista_elementi.index(elemento2)))
else:
    print("L'elemento non è nella lista")

# Soluzione

lista = ['Marco', 'Luigi', 'Paolo', 'Giuseppe', 'Maria']
el = input("Inserisci un nome da cercare: ")
trovato = False
for nome in lista:
    if nome == el:
        trovato = True
        break
if trovato:
    print(f"{el} è presente nella lista all'indice {lista.index(el)}")
else:
    print(f"{el} non è presente nella lista.")