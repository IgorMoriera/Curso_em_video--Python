# Exercício 023 #
#
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
#  Ex:
#     Digite um número: 1834
#     Unidade: 4 Dezena: 3 Centena: 8 Milhar: 1


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 023 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Entrando com um número entre 0 e 9999
num = int(input('Escolha um número de 0 até 9999: '))

# Calculando as unidades, pegando o resto das divisões por 10
u = num // 1 % 10 #Pegando o número, dividindo por 10 e pegando o resto da divisão
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

# Mostrando os valores na tela
print('Unidade: {}'.format(u))
print('Dezena:  {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar:  {}'.format(m))
