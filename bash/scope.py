
# * lo scope è il contesto in cui una variabile esiste

# # Variabile globale
# viene definita fuori dalla funzione

x = 10 # variabile globale, cioè viene definita fuori dalla funzione

def stampa():
    print(x)

stampa()

# # Variabile locale
# viene definita dentro alla funzione

def funzione():
    y = 5 # variabile locale, cioè viene definita dentro alla funzione
    print(y)

funzione()

# # Modificare una variabile globale

x = 10

def cambia():
    global x # per cambiare la variabile globale dentro alla funzione
    x = 20

cambia()
print(x)


# Python cerca le variabili così:
# 1. Dentro la funzione (Local)
# 2. Funzione esterna (Enclosing)
# 3. Globale (Global)
# 4. Funzioni di Python (Built-in)