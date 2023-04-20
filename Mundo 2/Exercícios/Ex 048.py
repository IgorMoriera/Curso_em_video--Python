# Exercício 048 #
#
# Faça um programa que calcule a soma entre todos os números impares que são múltiplos de três e que se encontram
# no intervalo de 1 à 500


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 048 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

cont = 0
soma = 0

for c in range(1, 501, 2):
    if  c % 3 == 0:
        cont = cont +1
        soma = soma + c

print('\nA soma dos {} valores de 1 até 500 multiplos de 3 é: {}.'.format(cont, soma))
