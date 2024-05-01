# Exercício 107 #
#
# Crie um módulo chamado moeda.py que tenha as funções incorporadas: aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 107 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

from modulos.ex107 import moeda

p = float(input('Digite um preço: R$'))

print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')
