print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 059 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

somar = 1
mult = 2
maior = 3
newnum = 4
sair = 5
n = 0

n1 = float(input('Digite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))

while n != 5:
    print('==================================')
    print('''          >>>>> Menu <<<<
    [ 1 ] soma
    [ 2 ] multiplicar
    [ 3 ] maior valor
    [ 4 ] inserir novos números
    [ 5 ] sair do programa''')
    print('==================================')

    n = int(input('>>> Escolha uma opão acima: '))

    if n == 1:
        soma = n1 + n2
        print('O valor da soma deu {}'.format(soma))

    elif n == 2:
        multi = n1 * n2
        print('O valor da multiplicação deu {}'.format(multi))

    elif n == 3:
        if n1 > n2:
            print('O maior valor entre {} e {} é: {}'.format(n1, n2, n1))
        else:
            print('O maior valor entre {} e {} é: {}'.format(n1, n2, n2))

    elif n == 4:
        print('Insira novos números...\n')
        n1 = float(input('Digite o 1º valor: '))
        n2 = float(input('Digite o 2º valor: '))

    elif n == 5:
        print('Fim do prrograma. Volte sempre!')

    else:
        print('Opção invalida. Tente novamente!')
