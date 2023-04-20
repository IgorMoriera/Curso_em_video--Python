# Exercício 047 #
#
# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 3 50.


print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 047 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

print('\nContando de 1 até 50 ...')

for c in range(1, 51, 1):
    #print('.'.format(c))
    if c % 2 == 0:
        print([c], end=' ')

print('\nOs acima são todos PARES.')
