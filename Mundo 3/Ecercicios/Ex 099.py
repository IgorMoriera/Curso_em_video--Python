print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 099 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

from time import sleep

def maior(* num):
    cont = maior = 0
    print('-=' * 20)
    print('Analisando os valores passados... ')

    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.3)

        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1

    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    print('-=' * 20)

#Programa Princípal
maior(2, 9, 4, 5, 7, 1)