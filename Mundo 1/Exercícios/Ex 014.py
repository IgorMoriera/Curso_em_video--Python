# Exercício 014 #
#
# Escreva um programa que converta uma temperatura digitada em ºC e converta em ºF


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 014 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Entrando com a temperatura em ºC
temperatura = float(input('Digite a temperatura em ºC: '))

# Convertendo o valor de ºC para ºF
F = ((9 * temperatura) / 5) + 32

# Imprimindo os valor na tela
print('A temperatura de {}ºC corresponde a {}ºF.'.format(temperatura, F))
