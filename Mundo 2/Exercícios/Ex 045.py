print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 045 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

from time import sleep
import random

print('\n{:=^40}'.format(' JOGANDO JOKENPO!!! '))
print('\nVamos começar . . .\n')
sleep(1)

itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = random.randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual asua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 10)
print('Jogador escolheu {}'.format(itens[jogador]))
print('Computador escolheu {}'.format(itens[pc]))
print('-=' * 10)

if pc == 0: #jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif pc == 1: #jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA!')

elif pc == 2: #jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
