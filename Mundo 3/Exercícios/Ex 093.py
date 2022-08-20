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
print(f'{desempenho}')
print('-=' * 30)

for k, v in desempenho.items():
    print(f' O campo {k} tem o valor {v}.')
print('-=' * 30)

print(f'O jogador {desempenho["Nome"]} jogou {partidas} partidas.')
c = 1

for k in desempenho['Gols']:
    print(f'     => Na partida {c}, fez {k} gols.')
    c += 1

print(f'Foi um total de {desempenho["Total"]} gols.')
