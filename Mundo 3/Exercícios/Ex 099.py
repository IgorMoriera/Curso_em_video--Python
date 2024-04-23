# Exercício 099 #
#
# Faca um programa que tenha uma funcionalidade chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 099 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

from time import sleep


def maior(*num):

    cont = maior_num = 0
    print('-=' * 20)
    print('Analisando os valores passados... ')

    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)

        if cont == 0:
            maior_num = valor
        else:
            if valor > maior_num:
                maior_num = valor
        cont += 1

    print(f'>> Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior_num}.')


# Programa Princípal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
