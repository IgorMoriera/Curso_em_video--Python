# Exercício 060 #
#
# Faça um programa que leia um número qualquer e mostre o seu fatorial.


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 060 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

mult = 1

n = int(input('Fatoreal de qual número você deseja? '))

print('Calculando {}! = '.format(n), end='')
while n > 0:
    print('{}'.format(n), end=' ')
    print(' x ' if n > 1 else ' =  {}.'.format(mult), end=' ')
    mult *= n
    n -= 1
