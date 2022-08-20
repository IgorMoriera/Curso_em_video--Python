print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 023 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

num = int(input('Escolha um número de 0 até 9999: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena:  {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar:  {}'.format(m))
