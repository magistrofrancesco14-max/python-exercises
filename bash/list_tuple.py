
# # Liste

utenti = ['John', 'Sara', 'Dave']

data = ['Dave', 42, True]

listavuota = []

print('Dave' in utenti)
print(utenti[0])
print(utenti[-1])
print(utenti.index('Sara')) # il valore è 1 perchè la numericazione parte da 0
print(utenti[0:1]) # stampa gli elementi della lista da 0 fino a 1 escluso
print(utenti[0:2]) # stampa gli elementi della lista da 0 fino a 2 escluso
print(utenti[0:]) # stampa gli elementi della lista da 0 in poi

utenti.append('Elsa') # aggiungi un elemento alla lista in fondo
print(utenti)

utenti.insert(0, 'Antonio') # aggiungi un elemento alla lista scegliendo la posizione

# utenti.extend(data) # unire due liste oppure aggiungere più elementi a una lista
# print(utenti)

utenti.remove('John') # rimuovere elemento da lista
print(utenti)

x = [1, 2, 3]
x.clear() # svuotare una lista (la lista continua ad esserci)
print(x)

del utenti[0] # eliminare elemento da lista
print(utenti)

utenti.extend(['Mario', 'Antonio', 'Carmelo', 'Andrea']) # aggiungere elementi ad una lista
print(utenti)

utenti.sort() # ordinare lista alfabeticamente
print(utenti) 

numeri = [1, 2, 3, 4, 5]
print(numeri)

numeri.reverse()
print(numeri)

print(len(utenti)) # stampare numero elementi nella lista

# # Tuples
# a differenza delle liste, gli elementi all'interno non si possono modificare

giorni = ('Lun', 'Mar', 'Mer', 'Gio', 'Ven')
print(giorni)

# spacchettare tuple
citta = ('Milano', 'Roma', 'Napoli')
(x, y, z) = citta 

print(x)
print(y)
print(z)