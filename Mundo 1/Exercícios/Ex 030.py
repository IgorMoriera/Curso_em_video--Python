# Exercício 030 #
#
# Crie um programa que leia um número inteiro e mostre na tela se ele é
# PAR ou ÍMPAR.


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 030 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

num = int(input('Digite um número: '))
result = num % 2

if result == 0:
    print('\nO número {} é PAR.'.format(num))
else:
    print('\nO número {} é ÍMPAR.'.format(num))