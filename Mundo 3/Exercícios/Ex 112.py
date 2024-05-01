# Exercício 112 #
#
# Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
#  leiaDinheiro() que seja capaz de funcionar como a função input(), mas vom ums vslidação dos dados para aceitar
#  apenas valores que sejam monetários.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 112 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

from modulos.ex112.utilidadescev import moeda, dado

p = dado.leiaDinheiro('Digite um preço: R$')
moeda.resumo(p, 35, 22)
