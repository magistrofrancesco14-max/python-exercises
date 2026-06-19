# Scrivi una semplice funzione che, data una lista di numeri, 
# fornisca in output un istogramma basato su questi numeri, usando asterischi per disegnarlo 
# Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:
# - ***
# - *******
# - *********
# - *****

lista = [3, 7, 9, 5]

def istogramma(lista):
    for numero in lista:
        print("*"* numero)

istogramma(lista)