# Exercício 095 #
#
# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 095 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

desempenho = []
jogador = 0

while True:
    jogador_data = {}
    print('--' * 25)

    jogador_data['Nome'] = str(input('Nome do jogador: '))
    jogador += 1

    partidas = int(input(f'Quantas partidas {jogador_data["Nome"]} jogou? '))
    gols_partida = []

    for c in range(1, partidas + 1):
        gols_partida.append(int(input(f'Quantos gols na partida {c}? ')))

    jogador_data['Gols'] = gols_partida
    jogador_data['Total'] = sum(gols_partida)
    desempenho.append(jogador_data.copy())

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        print('Erro! Por favor, responda apenas S ou N.')
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resposta == 'N':
        break

print('-=' * 30)

print(f'{"COD":<5}{"Nome":<15}{"Gols":<25}{"Total":<10}')
print('-' * 60)

for indice, jogador_data in enumerate(desempenho):
    print(f'{indice:<5}{jogador_data["Nome"]:<15}{str(jogador_data["Gols"]):<25}{jogador_data["Total"]:<10}')

print('-' * 60)

while True:
    busca = int(input('Mostrar dados de qual jogador (999 para parar)? '))

    if busca == 999:
        break

    if busca >= len(desempenho):
        print(f'ERRO! Não existe jogador com código {busca}!')

    else:
        print(f' -- LEVANTAMENTO DO JOGADOR: {desempenho[busca]["Nome"]}')

        for idx, gols in enumerate(desempenho[busca]['Gols']):
            print(f'    No jogo {idx + 1} fez {gols} gols.')

    print('-' * 60)

print('\n<<< ENCERRADO >>>')
