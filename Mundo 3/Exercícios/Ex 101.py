# Exercício 101 #
#
# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 101 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

from datetime import date


def voto(ano=0):
    print('--'*20)
    ano = int(input('Em que ano você nasceu? '))

    idade = (date.today().year - ano)

    if idade >= 18 and idade <= 65:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO')

    elif idade <= 17:
        return print(f'Com {idade} anos: NÃO VOTA')

    else:
        return print(f' Com {idade}: VOTO OPCIONAL')

voto()