# Scrivi una funzione che fornisca in output il nome del Sistema Operativo utilizzato con eventuali relative informazioni sulla release corrente. 
# Suggerimento: per risolvere questo esercizio potreste dover utilizzare una libreria!

import platform

def info_sistema():
    print(f"Sistema in uso: {platform.system()}")
    print(f"Processore in uso: {platform.processor()}")
    print(f"Release in uso: {platform.release()}")
    
info_sistema()