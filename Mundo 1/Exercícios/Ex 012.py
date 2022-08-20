# Exercício 012 #
#
# Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 012 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Definindo o preço da roupa
p = float(input('Digite o preço da roupa R$ '))

# Calculando o desconto de 5 %
d = p-(p*(5/100))

# Mostrando o resultado na tela
print('\nO preço com desconto é de R$ {}.'.format(d))