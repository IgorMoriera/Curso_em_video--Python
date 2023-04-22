# Exercício 086 #
#
# Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 086 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        if (l and c) != 3 and (l and c) == '':
            print('Entre com um valor válido.')
        else:
            mat[l][c] = int(input(f'Valor da posição {[l, c]}: '))

print('=-' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{mat[l][c]:^5}]', end='')
    print()
