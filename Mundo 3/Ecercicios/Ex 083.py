print('\033[1;33m-=' * 19)
print('\033[1;34m-=-=-=-=-=- Exercício 083 -=-=-=-=-=-')
print('\033[1;33m-=\033[m' * 19)

cont = cont1 = 0

lista = list(str(input('Digite uma expressão: ')))

for val in lista:
    if val == '(':
        cont += 1

    if val == ')':
        cont1 += 1

if cont == cont1:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
