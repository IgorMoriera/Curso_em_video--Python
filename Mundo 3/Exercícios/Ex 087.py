print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 087 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somac = num = 0

for l in range(0, 3):
    for c in range(0, 3):
        mat[l][c] = int(input(f'Valor da posição {[l, c]}: '))

        # Calculando a soma dos valoes pares digitados
        num = mat[l][c]
        if num % 2 == 0:
            soma += num

# Calculando a soma dos valoes da 3º coluna
for c in range(0, 3):
    for l in range(0, 3):
        if c == 2:
            somac += mat[l][c]

print('=-' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{mat[l][c]:^5}]', end='')
    print()

print('=-' * 30)
print(f'[ A ] - A soma de todos os valores pares digitados deu: {soma}.')
print(f'[ B ] - A soma dos valores da 3º coluna deu: {somac}.')
print(f'[ C ] - O maior valor da 2º linha é: {max(mat[1])}.')
