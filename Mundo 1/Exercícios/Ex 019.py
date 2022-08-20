print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 019 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

A = str(input('1º Aluno: '))
B = str(input('2º Aluno: '))
C = str(input('3º Aluno: '))
D = str(input('4º Aluno: '))

lista = [A, B, C, D]

import random

print('O aluno(a) sorteado(a) para apagar o quadro é o(a): {}'.format(random.choice(lista)))
