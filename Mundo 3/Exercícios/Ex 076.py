# Exercício 076 #
#
# Crie um programa que tenha uma tupla único com nomes de produtos e seus respectivos preços, na sequência.
# No ifnla, mostre uma listagem de preços, organizando os dados em forma tabular.


print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 076 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

listagem = ('Lápis', 2.00,
            'Borracha', 15.90,
            'Estojo', 21,
            'Transfferidor', 9.99,
            'Compasso', 5.50,
            'Mochila', 200,
            'Caneta', 2.50,
            'Livros', 1500)

print('-' * 35)
print(f'{"LISTA DE PREÇOS":^35}')
print('-' * 35)

for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<25}', end=' ')
    else:
        print(f'R${listagem[posicao]:>.2f}')
print('-' * 35)
