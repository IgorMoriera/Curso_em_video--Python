print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 016 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

import math

num = float(input('Digite um número: '))

inteiro = math.trunc(num)

print('O número {} tem a parte inteira {}.'.format(num, inteiro))
