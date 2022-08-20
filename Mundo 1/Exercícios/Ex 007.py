# Exercício 007 #
#
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 007 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Definindo as variáveis para identificar as notas de un aluno qualquer
n1 = float(input('Entre com a 1º nota: '))
n2 = float(input('Entre com a 2º nota: '))

# Mostrando o resultado da média para o usuário com relaçao aos valores inputados
print('A média enter {:.2f} e {:.2f} é igual a: {:.2f}'.format(n1, n2, (n1+n2)/2))
