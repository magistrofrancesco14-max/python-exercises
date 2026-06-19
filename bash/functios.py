
# * le funzioni sono blocchi di codice riutilizzabili che eseguono un’azione specifica. 
# * servono per evitare di ripetere codice.

# per definire la funzione su usa la parola def:
def saluta():
    print('Ciao!') # la funziona non viene eseguita automaticamente

saluta() # ! per eseguirla

# parametri in funzione
def fai_la_pasta(tipo_pasta):
    print("metti l'acqua")
    print("fai bollire")
    print("metti " + tipo_pasta)

fai_la_pasta("spaghetti")

# si definisce la funzione somma per poi eseguirla con qualsiasi valore 
def somma(a, b):
    print(a + b)

somma(1, 2)
somma(3, 5)

# return: a differenza di print, con return il valore che viene restituito si può salvare in una variabile e riutilizzarlo 
def somma(a, b):
    return(a + b)
risultato = somma(50, 50)
print(risultato)

# ! Esempio:
def doppio(numero):
    return(numero * 2)
risultato = doppio(111)
print(risultato)

def pari_o_dispari(numero):
     if numero % 2 == 0:
        return 'Pari'
     else: 
        return 'Dispari'
risultato = pari_o_dispari(38)
print(risultato)
risultato = pari_o_dispari(3)
print(risultato)

def maggiore(a, b):
    if a > b:
        return a
    else: 
        return b
risultato = maggiore(23, 11)
print(risultato)

def maggiore3(a, b, c):
    return max(a, b, c)
risultato = maggiore3(100, 200, 300)
print(risultato)

