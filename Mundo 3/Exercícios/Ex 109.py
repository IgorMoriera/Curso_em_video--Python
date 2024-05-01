# Exercício 109 #
#
# Modifique as funções que froma criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor
#  retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 109 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

from modulos.ex109 import moeda

p = float(input('Digite um preço: '))

print(f'A metade de {moeda.formato(p, formatado=True)} é {moeda.metade(p, False)}')
print(f'O dobro de {moeda.formato(p, formatado=False)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, False)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, True)}')
