# Exercício 088 #
#
# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O program vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrado tudo em uma lista composta.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 088 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

from random import randint
from time import sleep

jogo = list()
lista_jogos = list()

print('--' * 15)
print('    JOGANGO NA MEGA SENA     ')
print('--' * 15)

palpites = int(input('Digite a quantidade de jogos que você deseja fazer: '))
total_palpites = 1

while total_palpites <= palpites:
    cont = 0

    while True:
        num = randint(1, 60)

        if num not in jogo:
            jogo.append(num)
            cont += 1

        if cont >= 6:
            break

    jogo.sort()
    lista_jogos.append(jogo[:])
    jogo.clear()
    total_palpites += 1

print('\n', '--' * 5, f' SORTEANDO {palpites} JOGOS ', '--' * 5, '\n')

for i, c in enumerate(lista_jogos):
    print(f'jogo {i+1}: {c}')
    sleep(1)

print('\n', '--' * 5, f' << BOA SORTE >> ', '--' * 5)
