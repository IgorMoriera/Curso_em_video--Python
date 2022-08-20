print('\033[1;33m-=' *19)
print('\033[1;34m-=-=-=-=-=- Exercício 068 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' *19)

from random import randint

cont = soma = 0

print('-=' * 20)
print('       Vamos Jogar PAR ou ÍMPAR     ')
print('=-' * 20)

while True:
    n = int(input('Digite um número: '))
    pc = randint(0, 10)
    soma = n + pc
    q = ' '

    while q not in 'PI':
        q = str(input('Par ou Ímpar [P/I]? ')).strip().upper()
        print('--' * 20)

    if q == 'P':
        if soma % 2 == 0:
            print(f'Você jogou {n} e o Computador {pc}. Total deu {soma} portanto o resultado é PAR.')
            print('--' * 20)
            print('Você VENCEU! Vamos jogar novamente ...')
            print('=-' * 20)
            cont += 1
        else:
            print(f'Você jogou {n} e o Computador {pc}. Total deu {soma}.')
            print('Você PERDEU!')
            break

    elif q == 'I':
        if soma % 2 == 1:
            print(f'Você jogou {n} e o Computador {pc}. Total deu {soma} portanto o resultado é ÍMPAR.')
            print('--' * 20)
            print('Você VENCEU! Vamos jogar novamente ...')
            print('=-' * 20)
            cont += 1
        else:
            print(f'Você jogou {n} e o Computador {pc}. Total deu {soma}.')
            print('Você PERDEU!')
            break

print(f'Você venceu {cont} vezes seguidas.')
print('=-' * 20)
print('GAME OVER! Volte sempre.')

