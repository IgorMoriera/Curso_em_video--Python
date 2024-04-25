# Exercício 103 #
#
# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um
#  jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha, mesmo que algum dado
#  não tenha sido informado corretamente.


print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 103 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

nome_jogador = "<desconhecido>"

def ficha (nome_jogador="<desconhecido>", gols=0):

    if nome_jogador != "<desconhecido>":
        nome_jogador = str(input('Nome do jogador: '))
        gols = str(input('Quantos gols ele marcou: '))

    else:
        nome_jogador == "<desconhecido>"

    return print(f'O jogador {nome_jogador} fez {gols} gol(s) no campeonato.')


ficha()

