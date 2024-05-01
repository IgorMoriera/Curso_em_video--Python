# Exercício 110 #
#
# Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostra na tela algumas
#  informações geradas pelas funções que já temos no módulo criado até aqui.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 110 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

from modulos.ex110 import moeda

p = float(input('Digite um preço: '))
moeda.resumo(p, 20, 12)
