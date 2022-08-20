print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 042 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

from time import sleep

print('\n\033[1;33mAnálisando Triângulos . . .\033[m')

# Input das medidas
a = float(input('\nDigite a 1º medida: '))
b = float(input('Digite a 2º medida: '))
c = float(input('Digite a 3º medida: '))

print('\n\033[1;35mProcessando . . .\033[m')
sleep(0.5)

# Verificndo se é possível formr um triângulo
if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print('\nCom os valores de a = {} , b = {} e c = {}, podemos formar um triângulo.'.format(a, b, c))

else:
    print('Com os valores de a = {} , b = {} e c = {}, não podemos formar um triângulo.'.format(a, b, c))

# Verificando o tipo de triângulo formado
if a == b == c:
    print('Como todos os lados são \033[1;32mIGUAIS\033[m, podemos formamos um triângulo \033[1;34mEQUILÁTERO\033[m.')

elif a != b != c:
    print('Como todos os lados são \033[1;32mDIFERENTES\033[m, podemos formamos um triângulo \033[1;34mISÓSCELES\033[m.')

elif (a == b) or (a == c) or (b == c):
    print('Como um dos lados são \033[1;32mIGUAIS\033[m, podemos formamos um triângulo \033[1;34mESCALENO\033[m.')
