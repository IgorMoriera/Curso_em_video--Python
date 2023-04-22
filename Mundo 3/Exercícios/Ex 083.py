# Exercício 083 #
#
# Crie um programa onde o usuário digite um expressão qualquer que use parênteses. Seu aplicativo dseverá analisar se
# a expressão passada está com os parênteses abertos e fechados na ordem correta.


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
