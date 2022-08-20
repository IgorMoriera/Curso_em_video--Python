## Exercício 011 #
#
# Faça um programa que leia a largura e a altura de uma parede em metros. Calcle a sua área
#  e a quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m²

print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 011 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Lendo o valor da largura
l = float(input('Digite a largura: '))
# Lendo o valor da altura
a = float(input('Digite a altura: '))

# Calculando a área
area = l * a

# Claculando a quantidade de tinta
quantidade_tinta = area / 2

# Mostrando os resultados na tela em litros de tinta
print('A área é de {}[m^2]. \nÉ necessário {} litros de tinta para a pintar.'.format(area, quantidade_tinta))
