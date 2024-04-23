# Exercício 098 #
#
# Faca um programa que tenha uma função chamada contador(), que receba três paraâmetros: início, fim e passo e realize
#  a contagem.
#
# Seu programa tem que realizar três contagens atraveés da função criada:
#
#  a) De 1 até 10, de 1 em 1;
#  b) De 10 até 0, de 2 em 2;
#  c) Uma contagem personalizada.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 098 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

from time import sleep


def contador(i, f, p):

    # Tratando as condições do passo
    if p < 0:
        p = abs(p)

    if p == 0:
        p = 1

    print('-=' * 20)
    print(f'Contagem de {i} até {f} de {p} em {p}')

    # Realizando a contagem de forma crescente
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont += p
        print(' -- FIM!')

    # Realizando a contagem de forma regressiva
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont -= p
        print('-- FIM!')


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

print('Agora é sua vez de personalizar acontagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)
