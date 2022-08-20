# Exercício 006 #
#
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 006 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Solicitando um valor ao usuário
n0 = int(input('Digite um número: '))

# Calculando o dobro de n0
n1 = 2 * n0
# Calculando o triplo de n0
n2 = 3 * n0
# Calculando a raiz quadrada de n0
n3 = n0 ** (1/2)

# Imprimindo os resultados do problema na tela para o usuário
print('O dobro de {}, vale: {}\nO Triplo vale: {} \nE a raíz quadrada é igual a: {:.4f}.'.format(n0, n1, n2, n3))
