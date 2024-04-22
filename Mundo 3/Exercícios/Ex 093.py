# Exercício 093 #
#
# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso sera guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 093 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

desempenho = dict()
gol_partida = list()

desempenho['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {desempenho["Nome"]} jogou? '))

cont = soma = 0
for c in range(1, partidas+1):
    gols = int(input(f'Quantos gols na partida {c}? '))
    cont += 1
    soma += gols
    gol_partida.append(gols)

desempenho['Gols'] = gol_partida
desempenho['Total'] = soma

print('-=' * 30)
print('>> Nível de resolução 1\n')
print(f'{desempenho}')

print('-=' * 30)

print('>> Nível de resolução 2\n')
for k, v in desempenho.items():
    print(f' O campo {k} tem o valor {v}.')

print('-=' * 30)

print('>> Nível de resolução 3\n')
print(f'O jogador {desempenho["Nome"]} jogou {partidas} partidas.')
c = 1

for k in desempenho['Gols']:
    print(f'     => Na partida {c}, fez {k} gols.')
    c += 1

print(f'Foi um total de {soma} gols.')
