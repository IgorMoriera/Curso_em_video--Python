print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 038 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

n1 = int(input('Digite 1ª número: '))
n2 = int(input('Digite 2ª número: '))

if n1 > n2:
    print('\nO PRIMEIRO valor é maior.'.format(n1, n2))

elif n2 > n1:
    print('\nO SEGUNDO valor é maior.'.format(n2, n1))

elif n1 == n2:
    print('\nNão exeiste valor maior, os dois são \033[1;34mIGUAIS\033[m.')
