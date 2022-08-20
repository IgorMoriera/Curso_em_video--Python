print('\033[1;33m-=' *19)
print('''\033[1;34m-=-=-=-=-=- Exercício 049 -=-=-=-=-=-
-=-=-=-=- Fazendo tabuada -=-=-=-=-''')

print('\033[1;33m-=\033[m' *19)

num = int(input('Digite um número: '))

print('A tabuada de {} é:'.format(num))
for n1 in range(1, 11):
    print('{} x {} = {}'.format(n1, num, n1 * num))
