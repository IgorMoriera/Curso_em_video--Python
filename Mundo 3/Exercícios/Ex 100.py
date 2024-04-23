# Exercício 100 #
#
# Crie um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a segunda função vai mostrar
#  a soma entre todos os valores PARES sorteados pela função anterior.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 100 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

from random import randint
from time import sleep


def sorteia(lista):
    print('Soerteando 5 valores da lista: ', end='')

    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)

        print(f'{n}...', end='')
        sleep(0.2)

    print('PRONTO!')


def somaPar(lista):
    soma = 0

    for valor in lista:
        if valor % 2 == 0:
            soma += valor

    print(f'Somando os valores pares de {lista}, temos {soma}.')


# Programa Principal
numeros = list()
sorteia(numeros)
somaPar(numeros)
