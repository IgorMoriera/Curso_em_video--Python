print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 074 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

from random import randint


num = (randint(1, 20), randint(1, 20), randint(1, 20),
       randint(1, 20), randint(1, 20))

print(f'Os números sorteados foram: ', end=' ')
for n in num:
    print([n], end=' ')

print(f'\nO MAIOR valor sorteado foi: {max(num)}')
print(f'O MENOR valor sorteado foi: {min(num)}')
