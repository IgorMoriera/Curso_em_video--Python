print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 073 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

premier_ligue = ('', 'LIV', 'MCU', 'LEI', 'TOT', 'MCI', 'SOU', 'EVE', 'AVI', 'CHE', 'WHA', 'ARS', 'LEE', 'WOL', 'CPA', 'NEW', 'BUR', 'BHA', 'FUL', 'WBA', 'SFU')

print('==' * 25)

# A
print('Os 5 primeiros times do Campeonato da Premier Ligue são:')
for cont in range(1, len(premier_ligue[:6])):
    print(f'{cont}º - {premier_ligue[cont]}')
print('=~' * 25)

# B
print(f'Os 4 ultimos times do Campeonato da Premier Ligue são:')
for cont in range(17, len(premier_ligue[:21])):
    print(f'{cont}º - {premier_ligue[cont]}')
print('=~' * 25)

# C
print('Os times em ordem alfábetica ficam:')
print(f'{sorted(premier_ligue[1:21])}')
print('=~' * 25)

# D
print(f'O {premier_ligue[11]} está na {premier_ligue.index("ARS")}º posisão.')
print('=~' * 25)
print('==' * 25)
