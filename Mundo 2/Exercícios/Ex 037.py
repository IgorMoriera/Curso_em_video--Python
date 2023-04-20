# Exercício 037 #
#
# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para Binário
# - 2 para Octal
# - 3 para Hexadecimal


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 037 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

from time import sleep

bi = 1
oc = 2
he = 3

n = int(input('\nDigite um número que deseja converter: '))
sleep(0.5)

print('\nDigite:\n [ 1 ] conversão para Binário\n [ 2 ] conversão para Octal\n [ 3 ] conversão para Hexadecimal')
sleep(0.5)

escolha = int(input('\nQual base você deseja? '))

if escolha == bi:
    bii = bin(n)
    print('\nO número {} em binário é: \033[1;32m{}'.format(n, bii [2:]))

elif escolha == oc:
    occ = oct(n)
    print('\nO número {} em octal é: \033[1;32m{}'.format(n, occ [2:]))

elif escolha == he:
    hexx = hex(n)
    print('\nO número {} em hexadecimal é: \033[1;32m{}'.format(n, hexx [2:]))

elif escolha != bi or escolha != oc or escolha != he:
    print('Desculpe, esta opção é inválida. Tente novamente.')
