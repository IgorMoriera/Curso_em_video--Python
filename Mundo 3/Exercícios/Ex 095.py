print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 095 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

desempenho = dict()
gol_partida = list()
partida = list()
jogador = 0

while True:
    desempenho.clear()
    print('--' * 25)
    desempenho['Nome'] = str(input('Nome do jogador: '))
    jogador += 1

    partidas = int(input(f'Quantas partidas {desempenho["Nome"]} jogou? '))
    partida.clear()

    cont = soma = 0
    for c in range(1, partidas+1):
        partida.append(int(input(f'Quantos gols na partida {c}? ')))
        cont += 1

    desempenho['Gols'] = partida.copy()
    desempenho['Total'] = sum(partida)
    gol_partida.append(desempenho.copy())

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        print('Erro! Por favor, responda apenas S ou N.')
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

print('-=' * 30)

print('COD ', end='')
for i in desempenho.keys():
    print(f'{i:<15}', end='')
print()

print('-' * 40)

for k, v in enumerate(gol_partida):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('-' * 40)

while True:
    busca = int(input('Mostrar dados de qual jogador (999 para parar)? '))

    if busca == 999:
        break
    if busca >= len(desempenho):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVATAMENTO DO {desempenho["Nome"]}: ')
        for i, g in enumerate(gol_partida[busca]['Gols']):
            print(f'    No jogo {i+1} fez {g} gols.')

    print('-' * 40)
print('\n<<< ENCERRADO >>>')