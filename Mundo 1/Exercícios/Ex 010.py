# Exercício 010 #
#
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
#  quantos dolares ela pode ocmrpar


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 010 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Variável da quantidade de dinheri em float
v = float(input('Quanto dinheiro você tem na carteira? R$'))

# Convertendo de Real para Dólar
dolar = (v/3.27)

# Mostrando o valor na tela em dólar
print('Você pode comprar US${:.2f} com R${:.2f}'.format(dolar, v))
