# Exercícios 013 #
#
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 013 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Lendo o valor do salário
salario = float(input('Digite o seu salário R$ '))

# Calculando o novo salario
novo_salario = salario+(salario*(15/100))

# Mostrando o resultado na tela
print('\nO novo salário é de R$ {}.'.format(novo_salario))
