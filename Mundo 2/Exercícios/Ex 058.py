# Exercício 058 #
#
# Faç


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 058 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

num = 0
cont = 0

import random

pc = random.randint(0, 10)

print('-=-' * 16)
print('Em qual número entre 0 e 10 estou pensando?')
print('-=-' * 16)

while num != pc:
    num = int(input('Em que número pensei? '))
    if num != pc :
        cont += 1
        if num < pc:
            print('\033[1;33mMais. . .\033[m Tente novamente.')
        elif num > pc:
            print('\033[1;31mMenos. . .\033[m Tente novamente.')

if num == pc:
    print('\n\033[1;32mPARABÉNS VAGABUNDO\033[m, você acertou!!')
    print('O número escolhido foi {}. Você acertou com {} tentativas.'.format(pc, cont))
