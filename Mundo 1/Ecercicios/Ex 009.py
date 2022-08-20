# Exercício 009 #
#
#  Faça um programa que leia um número inteiro qualquer e moste na tela a sua tabuada

print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 009 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Deinindo o valor do qual será exibido a tabuada
n = int(input('Entre com um número: '))

# Calculando o valor da tabuada definida em n
n0 = 0*n
n1 = 1*n
n2 = 2*n
n3 = 3*n
n4 = 4*n
n5 = 5*n
n6 = 6*n
n7 = 7*n
n8 = 8*n
n9 = 9*n
n10 = 10*n

# Mostrando o valor da tabuada na tela
print('A tabuada de {}, é: \n'.format(n))

print('===== Tabuada de {} ====='.format(n))

print('0 x {} = {}'.format(n, n0))
print('1 x {} = {}'.format(n, n1))
print('2 x {} = {}'.format(n, n2))
print('3 x {} = {}'.format(n, n3))
print('4 x {} = {}'.format(n, n4))
print('5 x {} = {}'.format(n, n5))
print('6 x {} = {}'.format(n, n6))
print('7 x {} = {}'.format(n, n7))
print('8 x {} = {}'.format(n, n8))
print('9 x {} = {}'.format(n, n9))
print('10 x {} = {}'.format(n, n10))

print('=========================')