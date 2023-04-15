# Exercício 035 #
#
# Dasenvolva um programa que leia o comprimento de três retas a diga ao usuário se elas podem ou
# não formar um triângulo.


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 035 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

print('-=-' * 10)
print('Análisando Triângulos . . . ')
print('-=-' * 10)

a = float(input('Digite a 1º medida: '))
b = float(input('Digite a 2º medida: '))
c = float(input('Digite a 3º medida: '))

if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print('Com os valores de a = {} , b = {} e c = {}, podemos formar um triângulo.'.format(a, b, c))
else:
    print('Com os valores de a = {} , b = {} e c = {}, não podemos formar um triângulo.'.format(a, b, c))
