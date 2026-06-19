import sys
import random

print('')
playerchoice = input(
    'Clicca...\n1 per Carta,\n2 per Forbice, \n3 per Sasso\n\n'
)

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit('Devi scegliere 1, 2 o 3')

computerchoice = random.choice('123')
computer = int(computerchoice)

print('')
print('Hai scelto ' + playerchoice + '.')
print('Python ha scelto ' + computerchoice + '.')
print('')

if player == 2 and computer == 1:
    print('🎉 Hai Vinto!')
elif player == 3 and computer == 2:
    print('🎉 Hai Vinto!')
elif player == 3 and computer == 1:
    print('🎉 Hai Vinto!')
elif player == computer:
    print('Pareggio!')
else:
    print('🐍 Ha Vinto Python')

print('')

