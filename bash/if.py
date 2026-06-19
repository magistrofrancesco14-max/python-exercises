x = 10

if x == 10: # == significa è uguale a ...
    print("condizione verificata")

y = 11

if y != 10: # != significa diverso da ...
    print("condizione verificata")

z = 11

if z <= 10: # <= significa minore o uguale a ...
    print("condizione verificata")
else: # oppure
    print("condizione NON verificata")

a = 8

if a >= 10: # >= significa maggiore o uguale a ...
    print("maggiore o uguale a 10")
elif a != 8: # else if (oppure se)
    print("diverso da 8")
else: # oppure
    print("minore e diverso")

b = 11
c = 21

if b > 5 and c < 20: # se b e c sono compresi tra 5 e 20 (entrambi)
    print("condizione verificata")
else:
    print("condizione NON verificata")

q = 11
w = 21

if q > 5 or c < 20: # se q e w sono compresi tra 5 e 20 (almeno uno)
    print("condizione verificata")

p = 2
d = 3

if p % 2 == 0: # se p è modulo 2 (i numeri pari danno resto 0, i numeri dispari danno resto 1)
    print("numero pari")
else:
    print("numero dispari")
if d % 2 == 0: # se p è modulo 2 (i numeri pari danno resto 0, i numeri dispari danno resto 1)
    print("numero pari")
else:
    print("numero dispari")