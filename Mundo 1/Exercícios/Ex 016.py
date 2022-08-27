# Exrecício 016 #
#
# Crire um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 016 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Importando a função math para utilizar o truncamento
import math

# Definição da variável inserida pelo usuário
num = float(input('Digite um número: '))

# Identificando a porção inteira do número lido pela variável 'num'
inteiro = math.trunc(num)

# Imprimindo o resultado na tela
print('Resultado 1: O número {} tem a parte inteira {}.'.format(num, inteiro))

# Uma outra forma de fazer sem utilizar a função 'trunc', é utilizar a segunte linha de código:
print('Resultado 2: O número {} tem a parte inteira {}.'.format(num, int(num)))