print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 020 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

import random

A = str(input('1º Grupo: '))
B = str(input('2º Grupo: '))
C = str(input('3º Grupo: '))
D = str(input('4º Grupo: '))


lista = [A, B, C, D]
random.shuffle(lista)

print('A sequência das apresentações é: {}'.format(lista))
