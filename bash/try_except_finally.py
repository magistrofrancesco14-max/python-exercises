
# # Costrutti usati per gestire gli errori (eccezioni) senza far crashare il programma
# Try: provi codice “rischioso”, cioè quello che potrebbe generare un errore
# Except: viene eseguito se dentro il try si verifica un errore.
# Finally: viene eseguito sempre, sia che ci sia errore sia che non ci sia

try:
    x = int(input("Inserisci un numero "))
except:
    print("Non hai inserito un numero valido")

z = 5
try:
    print(z)
except:
    print("C'è un errore")
else: # se non c'è errore, manda a schermo
    print("Tutto ok") 

y = 4
try:
    print(y)
except:
    print("C'è un errore")
finally: # a prescindered manda a schermo
    print("finally") 

# # Raise / Exception 
# si utilizza per lanciare un errore

r = -1

if r < 0:
    raise Exception("Numero minore di zero")
