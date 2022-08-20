print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 051 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

a1 = int(input('Digite o 1º termo da P.A: '))
r = int(input('Digite a razão de desejada: '))
an = 0

print('\nSegue abaixo o resultado para a P.A:')

for n in range(1, 11):
    an = a1 + (n - 1) * r
    print(an, end = ' -> ')

print('FIM.')
