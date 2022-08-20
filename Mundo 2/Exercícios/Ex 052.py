print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 052 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

num = int(input('Digite um número ineiro qualquer: '))
cont = 0

for c in range(1, num + 1):
    if num % c == 0:
        cont += 1
        print('\033[1;31m', end = ' ')
    else:
        print('\033[33m', end = ' ')
    print('[{}]'.format(c), end = ' ')

print('\n\033[mO número {} é divisível por {} outros números.'.format(num, cont))

if cont > 2:
    print('O número {} NÃO É PRRIMO.'.format(num))
else:
    print('O número {} é PRIMO!'.format(num))