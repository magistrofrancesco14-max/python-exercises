
# # I moduli sono librerie di file, i file sono insieme di funzioni che si possono utilizzare, c'è ne sono diversi pre caricati.

import math # formule matematiche
import random # numeri casuali
import datetime # date e orari
import sys # sistema
import platform

import saluti

print(saluti.ciao('Luca'))
# import saluti -> importi il modulo
# saluti.ciao(...)  -> chiami la funzione dentro al modulo
# 'Luca' -> è il valore passato alla funzione

from calcoli import quadrato

print(quadrato(4))

from utente import info # importi la funzione dal modulo

nome = input('Inserisci nome: ') # prendi dati dall'utente
eta = input('Inserisci età: ') # prendi dati dall'utente

print(info(nome, eta)) # passi i valori alla funzione

from controlli import pari

n = int(input('Inserisci un numero: ')) # convertire la risposta in numero

if pari(n):
    print("Pari")
else:
    print("Dispari")

