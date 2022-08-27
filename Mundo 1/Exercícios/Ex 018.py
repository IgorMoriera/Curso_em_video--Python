# Exercício 018 #
#
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
#  cosseno e tangente desse ângulo


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 018 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

# Importando a função math
import math

# Determinando o valor do ângulo
ang = float(input('Digite o valor do angulo: '))

# Realização dos cálculo
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

# Mostrando os resultados
print('Para um angulo de {}º, temos: '
      '\n>> Cos = {:.2f}'
      '\n>> Sen = {:.2f}'
      '\n>> Tan = {:.2f}'.format(ang, sen, cos, tan))
