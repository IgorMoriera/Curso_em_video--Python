print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 075 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

valores = (int(input('Digite o 1º núemero: ')), int(input('Digite o 2º núemero: ')),
            int(input('Digite o 3º núemero: ')), int(input('Digite o 4º núemero: ')))

print(f'Você digitou: {valores}')
print('--' * 15)

# A
print(f'O numero 9 apareceu {valores.count(9)} vezes.')
print('--' * 15)

# B
if 3 in valores:
    print(f'O número 3 aparece na posição {valores.index(3)+1}.')
    print('--' * 15)
else:
    print('Não foi digitado o números 3 nesta sequência.')
# C
print(f'Os valores pares digitados são: ', end=' ')
for n in valores:
    if n % 2 == 0:
        print([n], end=' ')
