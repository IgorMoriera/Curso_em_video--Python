print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 065 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

q = 'Ss'

cont = med = soma = maior = menor = 0

while q in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    cont += 1


    if cont == 1:
        maior = menor = n

    else:
        if n > maior:
            maior = n

        if n < menor:
            menor = n

    q = str(input('Quer continuar [ S/N ]?  ')).strip().upper()[0]

med = soma / cont

print('''Você saiu!
 A média de todos os valores digitados deu {}.
 O maior valor é {} e o menor valor é {}.'''.format(med, maior, menor))
