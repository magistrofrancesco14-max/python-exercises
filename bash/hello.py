# Variabili
# possono iniziare solamente con una lettera o underscore, non con un numero, case-sensitive
# nome_variabile = valore_variabile
# le constanti non esistono, ma si usa scrivere le variabili in stampatello per determinare una constante
# NOME_COSTANTE = VALORE_COSTANTE
 

## Operatori
# booleani sono elementi logici che rappresentato True or False, si possono usare per verificare la validità di una condizione

## Variabil1
num = 42

# Per scoprire il tipo di dato
x = 5
print(type(x))

# Logica
if num > 10:
    print('è superiore')
else:
    print('Non è superiore')

# Testo su più linee
multiline = """
Ciao, come va?
Tutto bene te?
                Bene bene
"""
print(multiline)

# Caretteri speciali
apostrofo_a_capo = 'Cos\'è\nnon lo so '
print(apostrofo_a_capo)

my_name = 'francesco'
my_secondName = 'magistro'

print(my_name)
print(my_name.lower())
print(my_name.upper())
print(my_name.title(), my_secondName.title())

print('') # riga vuota
print('') # riga vuota
print('') # riga vuota
print('') # riga vuota
print('') # riga vuota
print('') # riga vuota

# Build a Menu
title = 'menu'.upper()
print(title.center(20, '='))
print('='* 20)
print('Caffè'.ljust(16, '.') + '$1')