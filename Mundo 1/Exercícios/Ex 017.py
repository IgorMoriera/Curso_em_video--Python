# Exercício 017 #
#
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triângulo
#  retângulo, calcule e mostre o comprimento da hipotenusa


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 017 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Importanto a biblioteca math
import math
# ou #
# from math import hypot

# Entrando com os valores do cateto oposto e adjacente
CO = float(input('Digite o valor do cateto oposto: '))
CA = float(input('Digite o valor do cateto adjacente: '))

# Realizando o cálculo da hipotenusa
H = math.hypot(CO, CA)

# Imprimindo o resultado na tela
print('Dados os valores de C.O = {:.2f} e C.A = {:.2f}, temos que a hipotenusa vale H = {:.2f}'.format(CO, CA, H))