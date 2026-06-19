
# * recursion è quando una funzione chiama sé stessa per risolvere un problema

def conto(n):
    if n == 0:
        print('Fine')
    else:
        print(n)
        conto(n-1)

conto(3) # per eseguire la funzione

def conto(n):
    if n == 0:
        print(0)
    else:
        print(n)
        conto(n-1)

conto(3) # per eseguire la funzione

print('')

