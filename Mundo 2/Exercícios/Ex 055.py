print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 055 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(p)))

    if p == 1:
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso

print('O maior peso lido foi {}Kg.'.format(maior))
print('O menor peso lido foi {}Kg.'.format(menor))
