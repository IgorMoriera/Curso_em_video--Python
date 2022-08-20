print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 091 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

from random import randint
from operator import itemgetter
from time import sleep

valores = list()
sorte = {'jogador 1': randint(1, 6),
         'jogador 2': randint(1, 6),
         'jogador 3': randint(1, 6),
         'jogador 4': randint(1, 6)}

print('Valores sorteados:')

for k, v in sorte.items():
    print(f'    {k} tirou: {v}')
    sleep(1)
    valores.append(v)

print('-=' * 20)
print(f'Ranking dos jogadores: ')

c = 1
for k, v in sorted(sorte.items(), key=itemgetter(1), reverse=True):
       print(f'   {c}º lugar: {k} com {v}')
       c += 1
       sleep(1)
