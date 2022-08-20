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


def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}.')


numeros = list()
sorteia(numeros)
somapar(numeros)
