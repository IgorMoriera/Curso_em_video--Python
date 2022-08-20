print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 061 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

a1 = int(input('Digite o 1º termo da P.A: '))
r = int(input('Digite a razão de desejada: '))
an = 0
n = 0

while n <= 9:
    n += 1
    an = a1 + (n - 1) * r
    print(an, end=' -> ')

print('FIM.')
