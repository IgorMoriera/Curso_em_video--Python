# Exercício 102 #
#
# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular
#  e o outro chamado show, que será um valor lógico (opcional) indicando se deverá mostrar ou não na tela o processo
#  de cálculo do fatorial.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 102 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)


def fatorial(num, show=False):
    """
    --> Calcula o Fatorial de um número.
    > parâmetro n: O número a ser calculado.
    > parâmetro show: (opcional) Mostrar ou não a resolução da conta.
    > parâmetro return: O valor do Fatorial de um número n.
    """
    mult = 1

    if show is True:
        while num > 0:
            if num > 1:
                print(f'{num} x ', end='')
                mult *= num
                num -= 1
            else:
                return f'{num} = {mult}'

    else:
        while num > 0:
            if num > 1:
                mult *= num
                num -= 1
            else:
                return mult


# Programa principal
print(fatorial(5))
