# Scrivi un programma che chieda tre numeri a, b, c all'utente e mostri il più grande tra loro.

a = int(input("Scrivi il primo numero "))
b = int(input("Scrivi il secondo numero "))
c = int(input("Scrivi il terzo numero "))

if a == b == c:
    print("I numeri sono uguali")
elif a > b:
    print(str(a))
elif c > a:
    print(str(c))
elif b > c:
    print(str(b))

# Soluzione

a = int(input("Scrivi il primo numero "))
b = int(input("Scrivi il secondo numero "))
c = int(input("Scrivi il terzo numero "))

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
elif c >= a and c >= b:
    print(c)