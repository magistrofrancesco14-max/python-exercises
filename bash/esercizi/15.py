# Un indirizzo MAC (Media Access Control address) è un indirizzo univoco associato dal produttore, 
# a un chipset per comunicazioni wireless (es WiFi o Bluetooth), composto da 6 coppie di cifre esadecimali separate da due punti.
# Un esempio di MAC è 02:FF:A5:F2:55:12.
# Scrivi una funzione genera_mac() che generi degli indirizzi MAC pseudo casuali utilizzando il modulo random.

import random

cifre_esadecimali = "0123456789ABCDEF"

def genera_mac():
    coppie = [] 
    for i in range(6):
        coppia = (random.choice(cifre_esadecimali) + random.choice(cifre_esadecimali)) #creo la coppia
        coppie.append(coppia) # unisco le coppie e con il ciclo for in range(6) ripeto 6 volte alfine di inserire nella lista [coppie] 6 coppie
    print(":".join(coppie)) # stampo le coppie con i : tra le coppie #! mettere print fuori dal ciclo

genera_mac()

# Soluzione 

import random

def genera_mac():
    char_set = "ABCDEF0123456789"
    mac_addr = ""
    due_punti = 0

    for _ in range(6):
        for _ in range(2):
            mac_addr += random.choice(char_set)
        if due_punti < 5:
          mac_addr += ":"
          due_punti += 1

    return mac_addr