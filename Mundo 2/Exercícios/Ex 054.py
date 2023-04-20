# Exercício 054 #
#
# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda nçao atingiram
# a maioridade e quantas já são maiores.


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 054 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

from datetime import date

totmaior = 0
totmenor = 0

for pess in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(pess)))
    idade = date.today().year - ano

    if idade >= 21:
        totmaior += 1

    else:
        totmenor += 1
print('Ao todo temos: {} pessoas maiores e {} pessoas menores de idade.'.format(totmaior, totmenor))
