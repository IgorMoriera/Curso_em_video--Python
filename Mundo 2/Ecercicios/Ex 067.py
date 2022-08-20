print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 067 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

cont = mult = 0

while True:
    n = int(input('Você quer a tauada de qual número? '))

    if n < 0:
        break

    print('--' * 15)
    for cont in range(1, 11):

        print(f'{n} x {cont} = {n*cont}')
    print('--' * 15)

print('Você saiu, volte sempre!')
