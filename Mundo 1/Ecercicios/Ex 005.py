# Exercício 005 #
#
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 005 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Interação com o usuário
n0 = int(input('Entre com um número qualquer: '))

# Calculando o número antecessor de n0
n1 = n0-1
# Calculando o número sucessor de n0
n2 = n0+1

# Mostrando na tela os valores solicitados pelo problema
print('O número antecessor de {} é: {}; E o sucessor é: {}'.format(n0, n1, n2))

# Ou, realizando a conta direta dentro da função PRINT. O que também dá certo e maximiza o código
print('O número antecessor de {} é: {}; E o sucessor é: {}'.format(n0, (n0-1), (n0+1)))