# Exercício 111 #
#
# Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
# Transfira todas as funções utilizadas nos desafios 107 até o 110 para o primiero pacote e mantenha tudo funcionando.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 111 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)


from modulos.ex111.utilidadescev import moeda

p = float(input('Digite um preço: '))
moeda.resumo(p, 20, 12)
