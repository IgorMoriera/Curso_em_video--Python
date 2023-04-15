# Exercício 028 #
#
# Escreva um programa que faça o computador "pensar" em um
# número inteiro entre 0 a 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.
# O programa devará escraver na tala se o usuário venceu ou perdeu.


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 028 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

import random

pc = random.randint(0, 5)

print('-=-' * 16)
print('Em qual número entre 0 e 5 estou pensando?')
print('-=-' * 16)

num = int(input('Em que número pensei? '))

print('\nProcessando . . .\n')
sleep(3) # Equivalente ao delay, faz o código aguardar por 'n' segundos

if num == pc:
    print('O número escolhido foi {}.'.format(pc))
    print('PARABÉNS VAGABUNDO, você acertou!!')
else:
    print('O número escolhido foi {}.'.format(pc))
    print('SE FUDEU, TENTA DE NOVO!')
