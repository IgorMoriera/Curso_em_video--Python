# Exercício 108 #
#
# Adapte o código do desafio 107, criando uma função adicionaç chamada moed() que consiga mostrar os valores como um
#  valor monetário formatado.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 108 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

from modulos.ex108 import moeda

p = float(input('Digite um preço: R$'))

print(f'A metade de {moeda.formato(p)} é {moeda.formato(moeda.metade(p))}')
print(f'O dobro de {moeda.formato(p)} é {moeda.formato(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.formato(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moeda.formato(moeda.diminuir(p, 13))}')
