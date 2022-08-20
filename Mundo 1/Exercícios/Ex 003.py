# Exercício 003 #
#
# Crie um programa que leia 2 números e mostre a soma entre eles


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 003 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Definindo variáveis como números inteiros
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))

# Realizando a operação de soma entre os 2 números escolhidos pelo o usuário
soma = n1+n2

# Mostrando o resultado entre a soma dos valores escolhidos pelo usuário
print('A soma entre {} e {} vale {}'.format(n1, n2, soma))

#Apenas um teste
