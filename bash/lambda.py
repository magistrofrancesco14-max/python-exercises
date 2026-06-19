 # # Le lambda sono funzioni anonime, non utilizzano def e restituiscono automaticamente il risultato senza return

somma = lambda a, b: a + b

print(somma(2, 3))

# equivalente a

def somma (a, b):
    print (a + b)

somma(2, 3)
